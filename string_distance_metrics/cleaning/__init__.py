"""
normalizer
==========

Submódulo encargado de la normalización de strings antes de aplicar
métricas de distancia o similitud.

Preprocesar los textos con este módulo mejora la precisión de las
comparaciones al eliminar diferencias superficiales como tildes,
capitalización o espacios extra.

Funciones disponibles:
    - :func:`normalize_string`: normaliza un string a minúsculas, sin
      diacríticos y con espacios simples.

Ejemplo de uso::

    from normalizer import normalize_string

    normalize_string("Teclado Mecánico")  # → 'teclado mecanico'
    normalize_string("  ÑOÑO  ")         # → 'nono'
"""

from .normalizer import normalize_string

