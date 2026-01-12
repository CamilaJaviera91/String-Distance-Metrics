import random

# Mapa de teclas vecinas en un teclado QWERTY estándar (incluyendo ñ).

EYBOARD_NEIGHBORS: dict[str, list[str]] = {
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
