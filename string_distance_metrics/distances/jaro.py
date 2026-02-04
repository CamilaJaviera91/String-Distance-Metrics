def jaro_similarity(a: str, b: str) -> float:
    """
    Calcula la similitud de Jaro entre dos strings.

    La similitud de Jaro mide cuántos caracteres coinciden entre dos strings,
    tomando en cuenta también las transposiciones (caracteres que coinciden
    pero están en distinto orden).

    Dos caracteres se consideran **coincidentes** si son iguales y están a una
    distancia máxima de ``floor(max(len(a), len(b)) / 2) - 1`` posiciones.

    La fórmula es::

        jaro = (m/|a| + m/|b| + (m - t/2) / m) / 3

    