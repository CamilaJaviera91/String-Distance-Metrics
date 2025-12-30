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