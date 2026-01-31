import random

# Mapa de teclas vecinas en un teclado QWERTY estándar (incluyendo ñ).

KEYBOARD_NEIGHBORS: dict[str, list[str]] = {
                                            "q": ["w", "a", "1", "2"],
                                            "w": ["q", "e", "a", "s", "2", "3"],
                                            "e": ["w", "r", "s", "d", "3", "4"],
                                            "r": ["e", "t", "d", "f", "4", "5"],
                                            "t": ["r", "y", "f", "g", "5", "6"],
                                            "y": ["t", "u", "g", "h", "6", "7"],
                                            "u": ["y", "i", "h", "j", "7", "8"],
                                            "i": ["u", "o", "j", "k", "8", "9"],
                                            "o": ["i", "p", "k", "l", "9", "0"],
                                            "p": ["o", "l", "ñ", "0"],
                                            
                                            "a": ["q", "w", "s", "z"],
                                            "s": ["a", "d", "w", "e", "z", "x"],
                                            "d": ["s", "f", "e", "r", "x", "c"],
                                            "f": ["d", "g", "r", "t", "c", "v"],
                                            "g": ["f", "h", "t", "y", "v", "b"],
                                            "h": ["g", "j", "y", "u", "b", "n"],
                                            "j": ["h", "k", "u", "i", "n", "m"],
                                            "k": ["j", "l", "i", "o", "m"],
                                            "l": ["k", "ñ", "o", "p"],
    "ñ": ["l", "p"],
 
    "z": ["a", "s", "x"],
    "x": ["z", "c", "s", "d"],
    "c": ["x", "v", "d", "f"],
    "v": ["c", "b", "f", "g"],
    "b": ["v", "n", "g", "h"],
    "n": ["b", "m", "h", "j"],
    "m": ["n", "j", "k"],
}

TYPO_TYPES: list[str] = ["keyboard", "drop", "dup", "swap", "replace_common"]

def generate_realistic_typo(text: str) -> str:

    """
    Genera un typo realista sobre un string de entrada, simulando errores
    comunes de escritura humana en teclado QWERTY.

    Los tipos de error posibles son:
        - ``keyboard``: reemplaza un carácter por uno vecino en el teclado.
        - ``drop``: elimina un carácter aleatorio.
        - ``dup``: duplica un carácter aleatorio.
        - ``swap``: intercambia un carácter con el siguiente.
        - ``replace_common``: reemplaza un carácter por una letra aleatoria del alfabeto.
    
    Args:
        text (str): Texto original sobre el que se aplicará el typo.
    
    Returns:
        str: Texto con un error tipográfico introducido. Si el texto está
             vacío, se devuelve sin modificaciones.

    Examples:
        >>> generate_realistic_typo("Laptop")
        'Lqptop'   # ejemplo con typo de teclado en 'a' → 'q'
    
    >>> generate_realistic_typo("Monitor")
        'Monitr'   # ejemplo con drop de 'o'
 
        >>> generate_realistic_typo("")
        ''         # texto vacío, sin cambios
    """

    if not text:
        return text
    
    text_list: list[str] = list(text)
    typo_type: str = random.choice(TYPO_TYPES)
    idx: int = random.randint(0, len(text_list) - 1)
    char: str = text_list[idx]

    if typo_type == "keyboard" and char.lower() in KEYBOARD_NEIGHBORS:
        text_list[idx] = random.choice(KEYBOARD_NEIGHBORS[char.lower()])

    elif typo_type == "drop":
        del text_list[idx]
    
    elif typo_type == "dup":
        text_list.insert(idx, char)
 
    elif typo_type == "swap" and idx < len(text_list) - 1:
        text_list[idx], text_list[idx + 1] = text_list[idx + 1], text_list[idx]
 
    elif typo_type == "replace_common":
        text_list[idx] = random.choice("abcdefghijklmnñopqrstuvwxyz")
 
    return "".join(text_list)
