import random
import pandas as pd

# ---------------------------------------------------
# Función para generar typos más realistas
# ---------------------------------------------------

def generar_typo_realista(texto):
    texto = list(texto)
    tipo = random.choice(["teclado", "drop", "dup", "swap", "replace_comun"])

    # Teclas cercanas (errores comunes de tipeo)
    teclas_cercanas = {
        "a": "qwsz",
        "s": "wedxza",