import pytest
from jaro_winkler import jaro_similarity, jaro_winkler_similarity, jaro_winkler_distance

# ===========================================================================
# jaro_similarity
# ===========================================================================

class TestJaroSimilarity:

    def test_strings_identicos(self):
        """Strings idénticos deben retornar similitud perfecta."""
        assert jaro_similarity("laptop", "laptop") == 1.0

    