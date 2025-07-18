from typing import Dict, Any
import re


def create_markdown(article: str, enrichment_plan: Dict[str, Any]) -> str:
    """Integrate hero image, in-context media, and links into the article Markdown."""
    # Insert hero image at the top
    print(enrichment_plan)
    hero = enrichment_plan.get("hero_image", {})
    hero_md = ""
    if hero:
        hero_md = f"![{hero.get('alt_text', '')}](<{hero.get('url', '')}>)\n\n"
    # Replace placeholder with actual URL later

    # Insert in-context media
    in_media = enrichment_plan.get("in_context_media", {})
    in_media_md = ""
    if in_media:
        in_media_md = f"[{in_media.get('alt_text', '')}]({in_media.get('url', '')})\n"
        placement_text = in_media.get("placement_text", "")
        # Insert after the first occurrence of placement_text
        article = re.sub(
            re.escape(placement_text),
            placement_text + "\n\n" + in_media_md,
            article,
            count=1,
        )

    # Insert links
    links = enrichment_plan.get("links", [])
    for link in links:
        anchor = link.get("anchor_text", "")
        placement_text = link.get("placement_text", "")
        # Replace first occurrence of placement_text with anchor text as a link
        link_md = f"[{anchor}]({link.get("url","")})"
        article = re.sub(re.escape(placement_text), link_md, article, count=1)

    # Add hero image at the top
    return hero_md + article
