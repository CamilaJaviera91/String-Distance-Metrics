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

    donde:
        - ``m`` = número de caracteres coincidentes.
        - ``t`` = número de transposiciones (pares coincidentes fuera de orden).
        - ``|a|``, ``|b|`` = longitud de cada string.

    Args:
        a (str): Primer string a comparar.
        b (str): Segundo string a comparar.

    Returns:
        float: Similitud de Jaro en el rango [0.0, 1.0].
               ``1.0`` indica strings idénticos; ``0.0`` indica sin coincidencias.
               Retorna ``1.0`` si ambos strings son vacíos.

    Examples:
        >>> jaro_similarity("martha", "marhta")
        0.9444444444444445

        >>> jaro_similarity("kitten", "sitting")
        0.746031746031746

        >>> jaro_similarity("igual", "igual")
        1.0

        >>> jaro_similarity("", "")
        1.0

        >>> jaro_similarity("abc", "xyz")
        0.0
    """
    if a == b:
        return 1.0

    len_a: int = len(a)
    len_b: int = len(b)

    if len_a == 0 or len_b == 0:
        return 0.0

    # Ventana máxima dentro de la cual dos caracteres se consideran coincidentes
    match_distance: int = max(len_a, len_b) // 2 - 1

    matches_a: list[bool] = [False] * len_a
    matches_b: list[bool] = [False] * len_b

    matches: int = 0
    transpositions: int = 0

    