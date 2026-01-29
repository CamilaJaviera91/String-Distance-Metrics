"""
distances
=========

Submódulo que agrupa los algoritmos de distancia y similitud entre strings.

Módulos disponibles:
    - ``levenshtein``: distancia de edición clásica y ratio de similitud normalizado.

Ejemplo de uso::

    from distances.levenshtein import levenshtein_distance, levenshtein_ratio

    levenshtein_distance("kitten", "sitting")  # → 3
    