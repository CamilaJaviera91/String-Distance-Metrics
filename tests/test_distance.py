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

    def test_eliminacion(self):
        """Eliminar un carácter incrementa la distancia en 1."""
        assert levenshtein_distance("gatos", "gato") == 1

    def test_transposicion(self):
        """Intercambiar dos caracteres requiere al menos 1 operación."""
        # Levenshtein no penaliza transposiciones especialmente (usa Damerau para eso)
        assert levenshtein_distance("ab", "ba") == 2

    def test_completamente_diferente(self):
        """Strings sin caracteres en común."""
        assert levenshtein_distance("abc", "xyz") == 3

    def test_caso_sensiblidad(self):
        """Mayúsculas y minúsculas se consideran caracteres diferentes."""
        assert levenshtein_distance("Hola", "hola") == 1

    def test_asimetria(self):
        """El orden no debe importar (distancia es simétrica)."""
        assert levenshtein_distance("kitten", "sitting") == levenshtein_distance("sitting", "kitten")

    def test_caso_clasico(self):
        """Caso clásico de la literatura: 'kitten' a 'sitting'."""
        assert levenshtein_distance("kitten", "sitting") == 3

    def test_un_caracter(self):
        """Comparar caracteres únicos."""
        assert levenshtein_distance("a", "a") == 0
        assert levenshtein_distance("a", "b") == 1

    