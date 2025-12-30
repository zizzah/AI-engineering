from typing import Dict, List


def word_count(text: str) -> int:
    """Returns the number of words in the given text."""
    return len(text.split())



def summarize_text(text: str, max_sentences: int = 3) -> str:
    if len(text.strip()) <20:
        return "text`s too short to summarize"
    return text[:50]+"..."

def detect_intent(text:str)-> str:
    if "summarize" in text.lower():
        return "summarization"
    elif "count words" in text.lower():
        return "word_count"
    else:
        return "unknown"