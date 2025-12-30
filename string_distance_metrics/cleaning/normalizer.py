import unicodedata

def normalize_string(text: str) -> str:

    if not isinstance(text, str):
        return text
    
    text = text.lower()
    text = unicodedata.normalize("NFD", text)
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    text = " ".join(text.split())

    return text