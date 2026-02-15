import pytest
from jaro_winkler import jaro_similarity, jaro_winkler_similarity, jaro_winkler_distance

# ===========================================================================
# jaro_similarity
# ===========================================================================

class TestJaroSimilarity:

    def test_strings_identicos(self):
        """Strings idénticos deben retornar similitud perfecta."""
        assert jaro_similarity("laptop", "laptop") == 1.0

    def test_ambos_vacios(self):
        """Dos strings vacíos se consideran idénticos."""
        assert jaro_similarity("", "") == 1.0

    def test_uno_vacio(self):
        """Un string vacío contra uno no vacío retorna 0.0."""
        assert jaro_similarity("", "laptop") == 0.0
        assert jaro_similarity("laptop", "") == 0.0

    def test_sin_coincidencias(self):
        """Strings sin caracteres en común retornan 0.0."""
        assert jaro_similarity("abc", "xyz") == 0.0

    def test_transposicion_clasica(self):
        """Caso clásico de la literatura: 'martha' vs 'marhta'."""
        result = jaro_similarity("martha", "marhta")
        assert round(result, 4) == 0.9444

    