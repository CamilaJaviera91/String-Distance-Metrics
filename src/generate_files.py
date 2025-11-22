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
        i = random.randint(0, len(texto) - 2)
        texto[i], texto[i+1] = texto[i+1], texto[i]
        return "".join(texto)
    
    return "".join(texto)

# ---------------------------------------------------
# 1. Definir categorías y productos (50 productos)
# ---------------------------------------------------

categorias = ["Electrónica", "Hogar", "Deporte", "Juguetería", "Computación", "Belleza", "Automotriz"]

productos = [{"producto": f"Producto_{i}", "categoria": random.choice(categorias)}
             for i in range(1, 51)]

paises = ["Chile", "Peru", "Colombia", "Mexico", "Argentina", "Brasil"]

marcas = ["Samsung", "Apple", "Sony", "LG", "Xiaomi", "Huawei", "HP", "Dell"]

anios = list(range(2018, 2025))

# ---------------------------------------------------
# 2. Rango de precios por categoría
# ---------------------------------------------------

precios_categoria = {"Electrónica": (80, 1500),
                     "Hogar": (10, 300),
                     "Deporte": (15, 400),
                     "Juguetería": (5, 120),
                     "Computación": (90, 2000),
                     "Belleza": (5, 200),
                     "Automotriz": (20, 800),}

# ---------------------------------------------------
# 3. Crear base con precio
# ---------------------------------------------------

data1 = []
for p in productos:
    for pais in paises:
        for anio in anios:
            marca = random.choice(marcas)

            minimo, maximo = precios_categoria[p["categoria"]]

            precio = round(random.uniform(minimo, maximo), 2)

            data1.append({"producto": p["producto"],
                          "pais": pais,
                          "anio": anio,
                          "marca": marca,
                          "precio_usd": precio})

df1 = pd.DataFrame(data1)

# ---------------------------------------------------
# 4. Crear base sin precio (con typos en ~30%)
# ---------------------------------------------------

data2 = []
for p in productos:
    for pais in paises:
        for anio in anios:
            marca = random.choice(marcas)

            # 30% de probabilidad de typo
            if random.random() < 0.30:
                marca = generar_typo_realista(marca)

            data2.append({
                "producto": p["producto"],
                "categoria": p["categoria"],
                "pais": pais,
                "anio": anio,
                "marca": marca