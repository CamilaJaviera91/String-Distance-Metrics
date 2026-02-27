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

    def test_uno_vacio(self):
        """La distancia a un string vacío es la longitud del otro."""
        assert levenshtein_distance("abc", "") == 3
        assert levenshtein_distance("", "abc") == 3

    def test_sustitucion_simple(self):
        """Un carácter diferente requiere una sustitución."""
        assert levenshtein_distance("gato", "pato") == 1

    def test_insercion(self):
        """Insertar un carácter incrementa la distancia en 1."""
        assert levenshtein_distance("gato", "gaato") == 1

    