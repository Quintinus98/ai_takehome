"""
Loads the articles, brand rules, links & media.
"""
import sqlite3
from typing import List, Dict, Any


def load_article_rules(path: str) -> str:
    """Load articles or rules from file."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def load_keywords(path: str) -> List[str]:
    """Load keywords from file."""
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def load_media(path: str) -> List[Dict[str, Any]]:
    """Load media from file."""
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    # Get all features from images table
    cursor.execute("SELECT id, url, title, description, tags FROM images")
    images = [
        dict(zip(["id", "url", "title", "description", "tags"], row))
        for row in cursor.fetchall()
    ]

    # Get all features from videos table
    cursor.execute("SELECT id, url, title, description, tags FROM videos")
    videos = [
        dict(zip(["id", "url", "title", "description", "tags"], row))
        for row in cursor.fetchall()
    ]

    conn.close()
    return images + videos


def load_links(path: str) -> List[Dict[str, Any]]:
    """Load links from file."""
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    # Get all features from resources table
    cursor.execute(
        "SELECT id, url, title, description, topic_tags, type FROM resources"
    )
    links = [
        dict(zip(["id", "url", "title", "description", "topic_tags", "type"], row))
        for row in cursor.fetchall()
    ]

    conn.close()
    return links
