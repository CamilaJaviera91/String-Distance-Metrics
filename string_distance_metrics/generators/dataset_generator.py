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