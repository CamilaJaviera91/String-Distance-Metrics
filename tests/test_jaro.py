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

    def test_caso_asimetrico(self):
        """El orden de los argumentos no debe afectar el resultado."""
        assert jaro_similarity("kitten", "sitting") == jaro_similarity("sitting", "kitten")

    def test_resultado_en_rango(self):
        """El resultado siempre debe estar en [0.0, 1.0]."""
        result = jaro_similarity("random", "string")
        assert 0.0 <= result <= 1.0

    def test_un_caracter_igual(self):
        """Un solo carácter idéntico."""
        assert jaro_similarity("a", "a") == 1.0

    def test_un_caracter_diferente(self):
        """Un solo carácter diferente retorna 0.0."""
        assert jaro_similarity("a", "b") == 0.0

    def test_typo_tipico(self):
        """Typo de teclado en un producto debe tener similitud alta."""
        result = jaro_similarity("Laptop", "Lqptop")
        assert result > 0.8

# ===========================================================================
# jaro_winkler_similarity
# ===========================================================================

class TestJaroWinklerSimilarity:

    def test_strings_identicos(self):
        """Strings idénticos deben retornar 1.0."""
        assert jaro_winkler_similarity("laptop", "laptop") == 1.0

    def test_ambos_vacios(self):
        