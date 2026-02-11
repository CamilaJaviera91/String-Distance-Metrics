"""
distances
=========

Submódulo que agrupa los algoritmos de distancia y similitud entre strings.

Módulos disponibles:
    - ``levenshtein``: distancia de edición clásica y ratio de similitud normalizado.
    - ``jaro_winkler``: similitud de Jaro, Jaro-Winkler y su distancia complementaria.
      Especialmente útil para comparar nombres o productos con typos al inicio del string.

Ejemplo de uso::

    from distances.levenshtein import levenshtein_distance, levenshtein_ratio
    from distances.jaro_winkler import jaro_winkler_similarity, jaro_winkler_distance

    