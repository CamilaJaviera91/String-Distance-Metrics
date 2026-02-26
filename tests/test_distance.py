import pytest
from string_distance_metrics.distances.levenshtein import levenshtein_distance, levenshtein_ratio

class TestLevenshteinDistance:
    """Tests para la función levenshtein_distance."""

    def test_strings_identicos(self):
        """Strings idénticos deben tener distancia 0."""
        assert levenshtein_distance("hola", "hola") == 0

    def test_ambos_vacios(self):
        """Dos strings vacíos tienen distancia 0."""
        assert levenshtein_distance("", "") == 0

    