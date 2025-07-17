import re


def shortlist_media(media, article, keywords):
    """Shortlist media by checking if any keyword or article word appears in title, description, or tags."""
    article_words = set(re.findall(r"\w+", article.lower()))
    keyword_set = set([k.lower() for k in keywords])
    shortlisted = []
    for item in media:
        text = f"{item['title']} {item['description']} {item['tags']}".lower()
        if keyword_set & set(re.findall(r"\w+", text)) or article_words & set(
            re.findall(r"\w+", text)
        ):
            shortlisted.append(item)
    return shortlisted


def shortlist_links(links, article, keywords):
    """Shortlist links by checking if any keyword or article word appears in title, description, or topic_tags."""
    article_words = set(re.findall(r"\w+", article.lower()))
    keyword_set = set([k.lower() for k in keywords])
    shortlisted = []
    for item in links:
        text = f"{item['title']} {item['description']} {item['topic_tags']}".lower()
        if keyword_set & set(re.findall(r"\w+", text)) or article_words & set(
            re.findall(r"\w+", text)
        ):
            shortlisted.append(item)
    return shortlisted
