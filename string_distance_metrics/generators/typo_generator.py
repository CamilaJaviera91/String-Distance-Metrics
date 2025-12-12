import random

def generate_realistic_typo(text: str) -> str:
        
    text_list = list(text)

    typo_type = random.choice(["keyboard", "drop", "dup", "swap", "replace_common"])

    keyboard_neighbors = {"a": ["s", "q", "z"], 
                          "s": ["a", "d", "w", "x"],
                          "e": ["w", "r", "d"], 
                          "o": ["i", "p", "l"],
        "n": ["b", "m", "h"],
    }

    if not text_list:
        return text

    idx = random.randint(0, len(text_list) - 1)
    char = text_list[idx]

    if typo_type == "keyboard" and char.lower() in keyboard_neighbors:
        text_list[idx] = random.choice(keyboard_neighbors[char.lower()])

    elif typo_type == "drop":
        del text_list[idx]

    elif typo_type == "dup":
        text_list.insert(idx, char)
    
    elif typo_type == "swap" and idx < len(text_list) - 1:
        text_list[idx], text_list[idx + 1] = text_list[idx + 1], text_list[idx]

    elif typo_type == "replace_common":
        text_list[idx] = random.choice("abcdefghijklmnñopqrstuvwxyz")

    return "".join(text_list)
