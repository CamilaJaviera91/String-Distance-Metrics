import pandas as pd
import random
from faker import Faker
from typing import List, Tuple
import os

# Inicializar Faker
fake = Faker('es_ES')

def apply_typo(text: str) -> str:
    """Aplica una pequeña variación (alta similitud, Distancia de Edición 1 o 2)."""
    if len(text) < 3:
        return text
    
    # 70% de probabilidad de aplicar un cambio
    if random.random() < 0.7:
        choice = random.choice(['swap', 'delete', 'substitute'])
        
        if choice == 'swap':
            # Transposición (alta similitud)
            idx = random.randint(0, len(text) - 2)
            return text[:idx] + text[idx+1] + text[idx] + text[idx+2:]
        
        elif choice == 'delete':
            # Omisión de un caracter
            idx = random.randint(0, len(text) - 1)
            return text[:idx] + text[idx+1:]
        
        elif choice == 'substitute':
             # Sustitución de un caracter
            idx = random.randint(0, len(text) - 1)
            char_pool = 'aeiousdtrg'
            return text[:idx] + random.choice(char_pool) + text[idx+1:]
            
    return text