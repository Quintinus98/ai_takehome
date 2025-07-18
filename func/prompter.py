import json
from typing import List, Dict, Any


def build_prompt(
    article: str,
    media: List[Dict[str, Any]],
    links: List[Dict[str, Any]],
    keywords: List[str],
    brand_rules: str,
) -> str:
    """Build a prompt for the LLM to select enrichments and generate anchor text."""
    prompt = f"""
You are an expert content editor. Your task is to enrich the following article with media and hyperlinks, following these rules:
- Select ONE hero image (from media list) for the top of the article.
- Select ONE in-context image or video (from media list) and specify where to insert it (quote a sentence or paragraph from the article).
- Select TWO links (from links list), and for each, generate anchor text (using the provided keywords) and specify where to insert it (quote a sentence or paragraph from the article).
- Follow these brand guidelines: {brand_rules}
- Output your plan as valid JSON in this format:
{{
  "hero_image": {{"id": ..., "alt_text": ..., "url": ...}},
  "in_context_media": {{"id": ..., "alt_text": ..., "placement_text": ..., "url": ...}},
  "links": [
    {{"id": ..., "anchor_text": ..., "placement_text": ..., "url": ...}},
    {{"id": ..., "anchor_text": ..., "placement_text": ..., "url": ...}}
  ]
}}

Article:
"""
    prompt += article + "\n\n"
    prompt += f"Media candidates (JSON):\n{json.dumps(media, indent=2)}\n\n"
    prompt += f"Link candidates (JSON):\n{json.dumps(links, indent=2)}\n\n"
    prompt += f"Target keywords: {keywords}\n"

    return prompt


def parse_llm_response(response: str) -> Dict[str, Any]:
    """Parse the LLM's JSON response, handling minor formatting issues."""
    try:
        # Try to find the first JSON object in the response
        start = response.find("{")
        end = response.rfind("}") + 1
        json_str = response[start:end]
        return json.loads(json_str)
    except Exception as e:
        raise ValueError(
            f"Failed to parse LLM response as JSON: {e}\nResponse: {response}"
        )
