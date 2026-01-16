import os
import random

import pandas as pd

from typo_generator import generate_realistic_typo

# ---------------------------------------------------------------------------
# Configuración global de categorías y datos de muestra
# ---------------------------------------------------------------------------

# Rango de precios (USD) por categoría: (precio_min, precio_max)
CONFIG_CATEGORIAS: dict[str, tuple[float, float]] = {
    "Electrónica": (80, 1500),
    "Hogar": (10, 300),
    "Deporte": (15, 400),
    "Juguetería": (5, 120),
    "Computación": (90, 2000),
    "Belleza": (5, 200),
    "Automotriz": (20, 800),
}

PAISES: list[str] = ["Chile", "Argentina", "México", "Colombia", "Perú"]
MARCAS: list[str] = ["Generic", "Premium", "EcoLine", "MasterTech", "Ultra"]
ANIOS: list[int] = [2023, 2024, 2025]

# Productos disponibles por categoría
PRODUCTOS_BASE: dict[str, list[str]] = {
    "Electrónica": ["Audífonos", "Televisor", "Cámara", "Parlante"],
    "Hogar": ["Lámpara", "Silla", "Mesa", "Espejo"],
    "Deporte": ["Mancuernas", "Balón", "Bicicleta", "Cuerda"],
    "Juguetería": ["Muñeca", "Auto control remoto", "Legos", "Peluche"],
    "Computación": ["Laptop", "Monitor", "Teclado Mecánico", "Mouse Pad"],
    "Belleza": ["Perfume", "Crema Facial", "Secador", "Maquillaje"],
    "Automotriz": ["Neumático", "Aceite Motor", "Radio Auto", "Frenos"],
}

