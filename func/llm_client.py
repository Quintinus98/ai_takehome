from openai import OpenAI
from dotenv import load_dotenv
import os
from func.logger import initialize_logger


def initialize_llm(prompt: str) -> str:
    load_dotenv()
    logger = initialize_logger()

    api_key = os.getenv("OPENROUTER_API_KEY")
    base_url = os.getenv("BASE_URL")
    if not api_key or not base_url:
        raise EnvironmentError("OPENROUTER_API_KEY environment variable not set.")
    client = OpenAI(base_url=base_url, api_key=api_key)

    logger.info("Prompt sent to openai, awaiting response...")
    try:
        completion = client.chat.completions.create(
            model="openai/gpt-4o",
            temperature=0.7,
            # max_tokens=1024,
            messages=[{"role": "user", "content": prompt}],
        )
        content = completion.choices[0].message.content
        logger.info("Response received.")
        
        if content is None:
            logger = initialize_logger()
            logger.error("OpenRouter API returned no content in the response.")
            raise RuntimeError("OpenRouter API returned no content in the response.")
        return content
    except Exception as e:
        logger.error(f"OpenRouter API call failed: {e}")
        raise RuntimeError(f"OpenRouter API call failed: {e}")
