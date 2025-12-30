from typing import  Dict
from util import word_count, summarize_text, detect_intent


def process_prompt(text: str) -> Dict[str, str | int]:
    return{
        "original_text": text,
        "word_count": word_count(text),
        "summary": summarize_text(text),
        "intent": detect_intent(text)
    }