import numpy as np

def calculate_levenshtein_distance(s1: str, s2: str) -> int:
    
    # Asegurar que ambas cadenas son minúsculas 
    s1 = s1.lower().strip()
    s2 = s2.lower().strip()
    
    len_s1 = len(s1)
    len_s2 = len(s2)

    # Crear una matriz.
    matrix = np.zeros((len_s1 + 1, len_s2 + 1), dtype=int)

    # Representa el costo de transformar una cadena vacía en la otra.
    for i in range(len_s1 + 1):
        matrix[i, 0] = i
    for j in range(len_s2 + 1):
        matrix[0, j] = j

    # Rellenar la matriz
    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            
            # Determinar el costo de la sustitución
            cost = 0 if s1[i-1] == s2[j-1] else 1
            
            # Aplicar la fórmula de Levenshtein:
            matrix[i, j] = min(matrix[i - 1, j] + 1, matrix[i, j - 1] + 1, matrix[i - 1, j - 1] + cost)
            
        return matrix[len_s1, len_s2]

def calculate_levenshtein_similarity(s1: str, s2: str) -> float:
    """
    Calcula la similitud normalizada (de 0.0 a 1.0) basada en la distancia.
    """
    distance = calculate_levenshtein_distance(s1, s2)
    max_len = max(len(s1.strip()), len(s2.strip()))
    
    # Si la longitud máxima es 0 (cadenas vacías), la similitud es 1.0
    if max_len == 0:
        return 1.0
        
    # Fórmula de similitud normalizada: 1 - (Distancia / Longitud Máxima)
    return 1.0 - (distance / max_len)