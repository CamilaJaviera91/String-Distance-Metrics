import pandas as pd
import random
from typo_generator import generate_realistic_typo
import os

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

    data_clean = []
    data_typo = []

    for i in range(n_rows):
        cat = random.choice(list(config_categorias.keys()))
        rango = config_categorias[cat]
        nombre_original = random.choice(productos_base[cat])
        
        comun = {
            "id_referencia": i,
            "categoria": cat,
            "pais": random.choice(paises),
            "anio": random.choice([2024, 2025]),
            "marca": random.choice(marcas),
            "precio_usd": round(random.uniform(rango[0], rango[1]), 2)
        }

        reg_clean = comun.copy()
        reg_clean["producto"] = nombre_original
        data_clean.append(reg_clean)

        reg_typo = comun.copy()
        reg_typo["producto"] = generate_realistic_typo(nombre_original)
        data_typo.append(reg_typo)

    df_clean = pd.DataFrame(data_clean)
    df_typo = pd.DataFrame(data_typo)

    ruta = "string_distance_metrics/data"

    if not os.path.exists(ruta):
        os.makedirs(ruta)
        print("Ruta creada con éxito.")
    else:
        print("La ruta ya existe.")

    df_clean.to_csv(f"{ruta}/base_maestra_limpia.csv", index=False, encoding='utf-8')
    df_typo.to_csv(f"{ruta}/base_usuario_con_typos.csv", index=False, encoding='utf-8')

    print(f"✅ Generadas {n_rows} filas en 'base_maestra_limpia.csv' y 'base_usuario_con_typos.csv'")

if __name__ == "__main__":
    generate_base_data(100)