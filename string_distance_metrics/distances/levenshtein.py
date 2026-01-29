def levenshtein_distance(a: str, b: str) -> int:
    """
    Calcula la distancia de Levenshtein entre dos strings.

    La distancia de Levenshtein es el número mínimo de operaciones de edición
    (inserción, eliminación o sustitución de un carácter) necesarias para
    transformar el string ``a`` en el string ``b``.

    La implementación utiliza programación dinámica con una sola fila de estado
    (O(n) en espacio), en lugar de la matriz completa O(n×m).

    Args:
        a (str): Primer string a comparar.
        b (str): Segundo string a comparar.

    Returns:
        int: Número mínimo de ediciones para transformar ``a`` en ``b``.
             Siempre es un valor >= 0. Retorna 0 si ambos strings son iguales.

    Examples:
        >>> levenshtein_distance("kitten", "sitting"): 3

        >>> levenshtein_distance("Laptop", "Lqptop")
        1

        >>> levenshtein_distance("", "abc")
        3

        >>> levenshtein_distance("igual", "igual")
        0
    """
    # Garantiza que `a` sea siempre el string más largo para reducir iteraciones
    if len(a) < len(b):
        return levenshtein_distance(b, a)

    if len(b) == 0:
        return len(a)

    previous_row: range = range(len(b) + 1)

    for i, ca in enumerate(a):
        current_row: list[int] = [i + 1]

        for j, cb in enumerate(b):
            insert: int = previous_row[j + 1] + 1      # Costo de insertar en `a`
            delete: int = current_row[j] + 1            # Costo de eliminar de `a`
            substitute: int = previous_row[j] + (ca != cb)  # Costo de sustituir (0 si son iguales)
            current_row.append(min(insert, delete, substitute))

        previous_row = current_row

    return previous_row[-1]

def levenshtein_ratio(a: str, b: str) -> float:
    """
    Calcula la similitud normalizada entre dos strings usando la distancia de Levenshtein.

    El ratio se calcula como::

        ratio = 1 - (distancia / max(len(a), len(b)))

    Un valor de ``1.0`` indica strings idénticos; un valor de ``0.0`` indica
    que no comparten ningún carácter en común (máxima distancia posible).

    Args:
        a (str): Primer string a comparar.
        b (str): Segundo string a comparar.

    Returns:
        float: Valor de similitud en el rango [0.0, 1.0].
               Retorna ``1.0`` si ambos strings son vacíos (se consideran idénticos).

    Examples:
        >>> levenshtein_ratio("Laptop", "Laptop")
        1.0

        >>> levenshtein_ratio("Laptop", "Lqptop")
        0.8333333333333334

        >>> levenshtein_ratio("", "")
        1.0

        >>> levenshtein_ratio("abc", "xyz")
        0.0
    """
    dist: int = levenshtein_distance(a, b)
    max_len: int = max(len(a), len(b))

    if max_len == 0:
        return 1.0  # Ambos strings vacíos se consideran idénticos

    return 1 - (dist / max_len)