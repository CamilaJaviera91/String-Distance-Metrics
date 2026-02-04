def jaro_similarity(a: str, b: str) -> float:
    """
    Calcula la similitud de Jaro entre dos strings.

    La similitud de Jaro mide cuántos caracteres coinciden entre dos strings,
    tomando en cuenta también las transposiciones (caracteres que coinciden
    pero están en distinto orden).

    