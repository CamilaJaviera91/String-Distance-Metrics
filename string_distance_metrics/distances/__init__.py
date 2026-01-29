"""
distances
=========

Submódulo que agrupa los algoritmos de distancia y similitud entre strings.

Módulos disponibles:
    - ``levenshtein``: distancia de edición clásica y ratio de similitud normalizado.

Ejemplo de uso::

    from distances.levenshtein import levenshtein_distance, levenshtein_ratio

    levenshtein_distance("kitten", "sitting")  # → 3
    levenshtein_ratio("Laptop", "Lqptop")      # → 0.833...
"""

from .levenshtein import levenshtein_distance, levenshtein_ratio

__all__ = ["levenshtein_distance", "levenshtein_ratio"]