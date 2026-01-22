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

# Ruta de salida para los CSV generados
RUTA_SALIDA: str = "string_distance_metrics/data"

# ---------------------------------------------------------------------------
# Funciones
# ---------------------------------------------------------------------------

def _crear_ruta_si_no_existe(ruta: str) -> None:
    """
    Crea el directorio indicado si aún no existe.

    Args:
        ruta (str): Ruta del directorio a verificar o crear.

    Returns:
        None
    """
    if not os.path.exists(ruta):
        os.makedirs(ruta)
        print(f"Ruta '{ruta}' creada con éxito.")
    else:
        print(f"La ruta '{ruta}' ya existe.")

def _generar_registro_base(idx: int) -> tuple[dict, str]:
    """
    Genera un registro base con campos comunes y el nombre del producto original.

    Selecciona aleatoriamente una categoría, un producto dentro de ella,
    un país, un año y una marca, y calcula un precio aleatorio dentro del
    rango definido para la categoría.

    Args:
        idx (int): Identificador numérico único del registro (``id_referencia``).

    Returns:
        tuple[dict, str]: Una tupla con:
            - ``comun`` (dict): Campos compartidos entre el registro limpio y el
              registro con typo (id, categoría, país, año, marca, precio).
            - ``nombre_original`` (str): Nombre del producto sin errores tipográficos.
    """
    cat: str = random.choice(list(CONFIG_CATEGORIAS.keys()))
    rango: tuple[float, float] = CONFIG_CATEGORIAS[cat]
    nombre_original: str = random.choice(PRODUCTOS_BASE[cat])

    comun: dict = {
        "id_referencia": idx,
        "categoria": cat,
        "pais": random.choice(PAISES),
        "anio": random.choice([2024, 2025]),
        "marca": random.choice(MARCAS),
        "precio_usd": round(random.uniform(rango[0], rango[1]), 2),
    }

    return comun, nombre_original

def generate_base_data(n_rows: int = 100) -> None: 
    """
    Genera dos datasets sintéticos de productos y los exporta como archivos CSV.
 
    Crea ``n_rows`` registros con datos ficticios de productos (categoría, país,
    marca, precio, año). A partir de cada registro produce dos versiones:
 
    - **base_maestra_limpia.csv**: contiene el nombre del producto sin errores.
    - **base_usuario_con_typos.csv**: contiene el nombre del producto con un
      error tipográfico realista generado por :func:`generate_realistic_typo`.
 
    Ambos archivos se guardan en ``string_distance_metrics/data/``.
 
    Args:
        n_rows (int): Número de filas a generar. Por defecto, 100.
 
    Returns:
        None
 
    Raises:
        OSError: Si no es posible crear el directorio de salida.
 
    Examples:
        >>> generate_base_data(50)
        La ruta 'string_distance_metrics/data' ya existe.
        ✅ Generadas 50 filas en 'base_maestra_limpia.csv' y 'base_usuario_con_typos.csv'
    """
    data_clean: list[dict] = []
    data_typo: list[dict] = []
 
    for i in range(n_rows):
        comun, nombre_original = _generar_registro_base(i)
 
        reg_clean: dict = {**comun, "producto": nombre_original}
        reg_typo: dict = {**comun, "producto": generate_realistic_typo(nombre_original)}
 
        data_clean.append(reg_clean)
        data_typo.append(reg_typo)
 
    df_clean: pd.DataFrame = pd.DataFrame(data_clean)
    df_typo: pd.DataFrame = pd.DataFrame(data_typo)
 
    _crear_ruta_si_no_existe(RUTA_SALIDA)
 
    df_clean.to_csv(f"{RUTA_SALIDA}/base_maestra_limpia.csv", index=False, encoding="utf-8")
    df_typo.to_csv(f"{RUTA_SALIDA}/base_usuario_con_typos.csv", index=False, encoding="utf-8")
 
    print(f"✅ Generadas {n_rows} filas en 'base_maestra_limpia.csv' y 'base_usuario_con_typos.csv'")
 
 