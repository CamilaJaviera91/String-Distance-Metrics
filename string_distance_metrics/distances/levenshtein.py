def levenshtein_distance(a: str, b: str) -> int:
    """
    Calcula la distancia de Levenshtein entre dos strings.

    La distancia de Levenshtein es el número mínimo de operaciones de edición
    (inserción, eliminación o sustitución de un carácter) necesarias para
    transformar el string ``a`` en el string ``b``.

    La implementación utiliza programación dinámica con una sola fila de estado
    (O(n) en espacio), en lugar de la matriz completa O(n×m).

    