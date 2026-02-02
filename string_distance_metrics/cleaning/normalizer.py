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
    4. **Normalización de espacios**: colapsa múltiples espacios consecutivos
       en uno solo y elimina espacios al inicio y al final.

    Args:
        text (str): Texto de entrada a normalizar. Si no es un string,
                    se devuelve sin modificaciones.

    Returns:
        str: Texto normalizado en minúsculas, sin tildes ni diacríticos y
             con espacios simples. Si ``text`` no es de tipo ``str``, se
             retorna el valor original sin cambios.

    Examples:
        >>> normalize_string("Teclado Mecánico")
            'teclado mecanico'

        >>> normalize_string("  Ñoño  ")
            'nono'

        >>> normalize_string("CRÈME BRÛLÉE")
            'creme brulee'

        >>> normalize_string(None)
            None  # no es str, se retorna tal cual

        >>> normalize_string(123)
        123   # no es str, se retorna tal cual
    """
    if not isinstance(text, str):
        return text

    # 1. Convertir a minúsculas
    text = text.lower()

    # 2. Descomponer caracteres acentuados en carácter base + diacrítico (NFD)
    text = unicodedata.normalize("NFD", text)

    # 3. Eliminar todos los diacríticos (categoría Unicode "Mn": Mark, Nonspacing)
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")

    # 4. Colapsar espacios múltiples y eliminar espacios al inicio/fin
    text = " ".join(text.split())

    return text