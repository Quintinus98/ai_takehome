from openai import OpenAI
from dotenv import load_dotenv
import os
from func.logger import initialize_logger


def initialize_llm(prompt: str):
    load_dotenv()
    api_key = os.getenv("OPENROUTER_API_KEY")
    base_url = os.getenv("BASE_URL")
    if not api_key or not base_url:
        raise EnvironmentError("OPENROUTER_API_KEY environment variable not set.")
    client = OpenAI(base_url=base_url, api_key=api_key)

    try:
        completion = client.chat.completions.create(
            model="openai/gpt-4o",
            temperature=0.7,
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}],
        )
        return completion.choices[0].message.content
    except Exception as e:
        logger = initialize_logger()
        logger.error(f"OpenRouter API call failed: {e}")
        print(f"OpenRouter API call failed: {e}")
        return ""
