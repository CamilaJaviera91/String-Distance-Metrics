import random

def generate_realistic_typo(text: str) -> str:
        
    text_list = list(text)

    typo_type = random.choice(["keyboard", "drop", "dup", "swap", "replace_common"])

    keyboard_neighbors = {"q": ["w", "a", "1", "2"],
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
                          "ñ": ["l", "p"],}

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
