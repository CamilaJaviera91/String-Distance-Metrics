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
        "d": "erfcxs",
        "e": "wsdfr",
        "o": "iklp",
        "n": "bhjm",
        "m": "njk",
        "p": "ol",
        "l": "kop",
        "g": "fhty",
         "u": "yhji",
        "i": "ujko"
    }

    # Reemplazos comunes manuales
    reemplazos_comunes = {
        "Samsung": "Sansung",
        "Apple": "Appel",
        "Sony": "Soni",
        "Huawei": "Huawe",
        "Xiaomi": "Xaiomi",
        "Dell": "Del",
        "HP": "HPP",
        "LG": "L-G"
    }

    # Opción: usar reemplazo típico real
    palabra_original = "".join(texto)
    if tipo == "replace_comun" and palabra_original in reemplazos_comunes:
        return reemplazos_comunes[palabra_original]