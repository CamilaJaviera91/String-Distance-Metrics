import random

def generate_realistic_typo(text: str) -> str:
        
    text_list = list(text)

    typo_type = random.choice(["keyboard", "drop", "dup", "swap", "replace_common"])

    keyboard_neighbors = {
        "a": ["s", "q", "z"], "s": ["a", "d", "w", "x"],
        "e": ["w", "r", "d"], "o": ["i", "p", "l"],
        "n": ["b", "m", "h"],
    }
