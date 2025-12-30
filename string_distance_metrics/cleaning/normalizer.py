import unicodedata

def normalize_string(text: str) -> str:

    if not isinstance(text, str):
        return text
    
    text = text.lower()