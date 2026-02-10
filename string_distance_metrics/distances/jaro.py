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

    # --- Paso 1: encontrar caracteres coincidentes ---
    for i in range(len_a):
        start: int = max(0, i - match_distance)
        end: int = min(i + match_distance + 1, len_b)

        for j in range(start, end):
            if matches_b[j] or a[i] != b[j]:
                continue
            matches_a[i] = True
            matches_b[j] = True
            matches += 1
            break

    if matches == 0:
        return 0.0

    # --- Paso 2: contar transposiciones ---
    k: int = 0
    for i in range(len_a):
        if not matches_a[i]:
            continue
        while not matches_b[k]:
            k += 1
        if a[i] != b[k]:
            transpositions += 1
        k += 1

    return (
        matches / len_a +
        matches / len_b +
        (matches - transpositions / 2) / matches
    ) / 3


def jaro_winkler_similarity(a: str, b: str, p: float = 0.1) -> float:
    """
    Calcula la similitud de Jaro-Winkler entre dos strings.

    Extiende la similitud de Jaro otorgando un **bonus adicional** a los
    strings que comparten un prefijo común, bajo la premisa de que los
    errores tipográficos son menos frecuentes al inicio de las palabras.

    La fórmula es::

        jaro_winkler = jaro + (l × p × (1 - jaro))

    donde:
        - ``jaro`` = similitud de Jaro entre ``a`` y ``b``.
        - ``l``    = longitud del prefijo común (máximo 4 caracteres).
        - ``p``    = factor de escala del prefijo (por convención, ``p ≤ 0.25``
          para garantizar que el resultado no supere ``1.0``).

    Args:
        a (str): Primer string a comparar.
        b (str): Segundo string a comparar.
        p (float): Factor de escala del prefijo. Por defecto ``0.1``,
                   que es el valor estándar propuesto por Winkler.
                   Debe estar en el rango ``[0.0, 0.25]``.

    Returns:
        float: Similitud de Jaro-Winkler en el rango [0.0, 1.0].
               Valores cercanos a ``1.0`` indican mayor similitud.
               Siempre es mayor o igual a la similitud de Jaro pura.

    Raises:
        ValueError: Si ``p`` no está en el rango ``[0.0, 0.25]``.

    Examples:
        >>> jaro_winkler_similarity("martha", "marhta")
        0.9611111111111111

        >>> jaro_winkler_similarity("Laptop", "Lqptop")
        0.9222222222222222

        >>> jaro_winkler_similarity("igual", "igual")
        1.0

        >>> jaro_winkler_similarity("abc", "xyz")
        0.0

        >>> jaro_winkler_similarity("Laptop", "Lqptop", p=0.0)
        0.888...  # sin bonus de prefijo, equivale a Jaro puro
    """
    if not 0.0 <= p <= 0.25:
        raise ValueError(f"El factor de escala 'p' debe estar en [0.0, 0.25], se recibió: {p}")

    jaro: float = jaro_similarity(a, b)

    # Calcular longitud del prefijo común (máximo 4 caracteres)
    prefix_len: int = 0
    for a_char, b_char in zip(a[:4], b[:4]):
        if a_char == b_char:
            prefix_len += 1
        else:
            break

    return jaro + (prefix_len * p * (1 - jaro))

def jaro_winkler_distance(a: str, b: str, p: float = 0.1) -> float:
    """
    Calcula la distancia de Jaro-Winkler entre dos strings.

    