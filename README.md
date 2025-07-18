# LLM-Powered Content Enrichment

A system that uses a Large Language Model (LLM) to automatically enrich draft articles with media and hyperlinks, focusing on robust data handling, effective prompt engineering, and clean, well-documented code.

## Features
- **Hero Image**: Automatically selects and inserts a prominent image at the top of each article.
- **In-Context Media**: Intelligently places a relevant image or video at the most contextually valuable spot in the article.
- **Contextual Hyperlinks**: Adds two informative hyperlinks with LLM-generated anchor text around provided target keywords.
- **Fuzzy Placement Matching**: Uses fuzzy string matching to robustly locate placement text in the article, handling formatting and Unicode differences.
- **Brand Guidelines**: All enrichments adhere to provided brand rules for voice, accessibility, and alt-text.
- **Logging & Error Handling**: Key steps and errors are logged for observability and debugging.

## Environment Setup
1. **Install dependencies**:
   ```bash
   uv pip install -r requirements.txt
   ```
2. **Create a `.env` file** at the project root with:
   ```
   OPENROUTER_API_KEY=<your OpenRouter API key>
   BASE_URL=https://openrouter.ai/api/v1
   ```

## How to Run
Run the enrichment pipeline on an article and its keywords:
```bash
python run.py --article_path path/to/article.md --keywords_path path/to/keywords.txt
```
- Replace the paths with your actual article and keywords files.
- The output will be an enriched Markdown file with media and links integrated.

## Logic Overview
- **Data Retrieval**: Shortlists candidate media and links from provided SQLite databases based on article content and keywords.
- **Prompt Engineering**: Crafts structured prompts for the LLM to select the best assets, generate anchor text, and specify placements. LLM output is expected in JSON for reliable parsing.
- **Fuzzy Placement**: Uses fuzzy matching (via rapidfuzz) to robustly insert media/links at the most contextually appropriate location, even if the article text has formatting or Unicode differences.
- **Content Assembly**: Integrates the LLM's choices into the Markdown article, preserving original formatting.
- **Quality Assurance**: Logs key steps and warnings if placement text is not found. Handles and reports LLM or data errors gracefully.

## Notes
- The system is designed to generalize to unseen articles and keywords—no hardcoded asset IDs or insertion points.
- All enrichments strictly follow the brand guidelines in `brand_rules.txt`.
- Efficient use of the OpenRouter API is encouraged to conserve credits.

## More to follow...
