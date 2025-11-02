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

def generate_controlled_data(n_records=50):
    
    print(f"Generando {n_records} registros base...")
    
    # Generar la data base (Archivo A)
    base_data: List[Tuple[int, str, str, str]] = []
    
    for i in range(n_records):
        record_id = i + 1
        #Generar nombres base de compañía y productos
        company = fake.unique.company()
        product_name = fake.sentence(nb_words=3)[:-1]
        year = fake.year()
        base_data.append((record_id, company, product_name, year))
        
    df_a = pd.DataFrame(base_data, columns=['ID', 'Compania', 'Nombre_Producto', 'Anio_Lanzamiento'])
    
    # Generar la data de prueba (Archivo B)
    data_b_list: List[Tuple[int, str, str, str]] = []
    
    for index, row in df_a.iterrows():
        
        compania_b = apply_typo(row['Compania'])
        
        if random.random() < 0.2: 
            producto_b = row['Nombre_Producto']
        else: 
            producto_b = fake.sentence(nb_words=4)[:-1]
            
        if random.random() < 0.8:
            anio_b = row['Anio_Lanzamiento']
        else:
            anio_b = str(int(row['Anio_Lanzamiento']) + random.randint(1, 2))
            
        data_b_list.append((row['ID'], compania_b, producto_b, anio_b))

    df_b = pd.DataFrame(data_b_list, columns=['ID', 'Compania', 'Nombre_Producto', 'Anio_Lanzamiento'])
    
    df_a.to_csv('src/data/file_a.csv', index=False)
    df_b.to_csv('src/data/file_b.csv', index=False)
    
    print("✅ Archivos generados exitosamente en la carpeta 'data/':")
    print(" - 'file_a.csv' (Base de datos)")
    print(" - 'file_b.csv' (Base de datos con variaciones controladas)")

if __name__ == "__main__":
    if not os.path.exists('src/data/'):
        os.makedirs('src/data/')
    generate_controlled_data(n_records=100)