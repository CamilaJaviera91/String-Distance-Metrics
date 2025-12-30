def levenshtein_distance(a: str, b: str) -> int:

    if len(a) < len(b):
        return levenshtein_distance(b, a)