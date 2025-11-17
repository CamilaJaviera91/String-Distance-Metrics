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
    
    # Error tipo teclado
    if tipo == "teclado":
        i = random.randint(0, len(texto) - 1)
        letra = texto[i].lower()
        if letra in teclas_cercanas:
            texto[i] = random.choice(teclas_cercanas[letra])
        return "".join(texto)
    
    # Eliminar una letra
    if tipo == "drop":
        i = random.randint(0, len(texto) - 1)
        return "".join(texto[:i] + texto[i+1:])
    
    # Duplicar una letra
    if tipo == "dup":
        i = random.randint(0, len(texto) - 1)
        return "".join(texto[:i] + [texto[i]] + texto[i:])
    
    # Intercambiar letras vecinas
    if tipo == "swap" and len(texto) >= 2: