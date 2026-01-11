import pandas as pd
import random
from generators.typo_generator import generate_realistic_typo

def generate_base_data(n_rows=100):

    config_categorias = {
        "Electrónica": (80, 1500),
        "Hogar": (10, 300),
        "Deporte": (15, 400),
        "Juguetería": (5, 120),
        "Computación": (90, 2000),
        "Belleza": (5, 200),
        "Automotriz": (20, 800)
    }

    paises = ["Chile", "Argentina", "México", "Colombia", "Perú"]
    marcas = ["Generic", "Premium", "EcoLine", "MasterTech", "Ultra"]
    anios = [2023, 2024, 2025]

    productos_base = {
        "Electrónica": ["Audífonos", "Televisor", "Cámara", "Parlante"],
        "Hogar": ["Lámpara", "Silla", "Mesa", "Espejo"],
        "Deporte": ["Mancuernas", "Balón", "Bicicleta", "Cuerda"],
        "Juguetería": ["Muñeca", "Auto control remoto", "Legos", "Peluche"],
        "Computación": ["Laptop", "Monitor", "Teclado Mecánico", "Mouse Pad"],
        "Belleza": ["Perfume", "Crema Facial", "Secador", "Maquillaje"],
        "Automotriz": ["Neumático", "Aceite Motor", "Radio Auto", "Frenos"]
    }

    data = []

    for _ in range(n_rows):

        cat = random.choice(list(config_categorias.keys()))
        rango = config_categorias[cat]
        
        nombre_base = random.choice(productos_base[cat])
        producto_con_error = generate_realistic_typo(nombre_base)
        
        registro = {
            "producto": producto_con_error,
            "producto_original": nombre_base, 
            "categoria": cat,
            "pais": random.choice(paises),
            "anio": random.choice(anios),
            "marca": random.choice(marcas),
            "precio_usd": round(random.uniform(rango[0], rango[1]), 2)
        }
        data.append(registro)

    df = pd.DataFrame(data)
    df.to_csv("base_categoria_con_precio.csv", index=False, encoding='utf-8')
    return df