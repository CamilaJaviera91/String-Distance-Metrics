def levenshtein_distance(a: str, b: str) -> int:

    if len(a) < len(b):
        return levenshtein_distance(b, a)
    
    if len(b) == 0:
        return len(a)
    
    previous_row = range(len(b) + 1)

    for i, ca in enumerate(a):
        current_row = [i + 1]
        for j, cb in enumerate(b):
            insert = previous_row[j + 1] + 1
            delete = current_row[j] + 1
            substitute = previous_row[j] + (ca != cb)
            current_row.append(min(insert, delete, substitute))
        previous_row = current_row

    return previous_row[-1]

def levenshtein_ratio(a: str, b: str) -> float:
    dist = levenshtein_distance(a, b)
    max_len = max(len(a), len(b))
    
    if max_len == 0:
        return 1.0 # Cadenas vacías son idénticas
        
    return 1 - (dist / max_len)