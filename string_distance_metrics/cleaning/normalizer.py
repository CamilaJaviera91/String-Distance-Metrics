import unicodedata

def normalize_string(text: str) -> str:
    """
    Normaliza un string para facilitar comparaciones de similitud entre textos.

    Aplica las siguientes transformaciones en orden:

    1. **Conversión a minúsculas**: elimina diferencias por capitalización.
    2. **Descomposición Unicode (NFD)**: separa los caracteres base de sus
       diacríticos (e.g. ``é`` → ``e`` + acento).
    3. **Eliminación de diacríticos**: remueve todos los caracteres de la
       categoría Unicode ``Mn`` (Mark, Nonspacing), como tildes y diéresis.
    