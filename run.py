import argparse
from func.data_loader import load_article_rules, load_keywords, load_links, load_media
from func.integrator import shortlist_links, shortlist_media
from func.llm_client import initialize_llm
from func.create_markdown import create_markdown
from func.prompter import build_prompt, parse_llm_response
from func.logger import initialize_logger


def main(article_path, keywords_path):
    logger = initialize_logger()
    try:
        # 1. Data Retrieval
        article = load_article_rules(article_path)
        keywords = load_keywords(keywords_path)
        brand_rules = load_article_rules("data/brand_rules.txt")
        media_candidates = load_media("data/media.db")
        link_candidates = load_links("data/links.db")

        shortlisted_media = shortlist_media(media_candidates, article, keywords)
        shortlisted_links = shortlist_links(link_candidates, article, keywords)

        # 2. Prompt Engineering
        prompt = build_prompt(
            article, shortlisted_media, shortlisted_links, keywords, brand_rules
        )
        llm_response = initialize_llm(prompt)
        enrichment_plan = parse_llm_response(llm_response)

        # 3. Content Assembly
        enriched_markdown = create_markdown(article, enrichment_plan)

        # 4. Output
        output_path = article_path.replace(".md", "_enriched.md")
        with open(output_path, "w") as f:
            f.write(enriched_markdown)
        logger.info(f"Enriched article saved to {output_path}")

    except Exception as e:
        logger.error(f"Pipeline failed: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--article_path", required=True)
    parser.add_argument("--keywords_path", required=True)
    args = parser.parse_args()
    main(args.article_path, args.keywords_path)
