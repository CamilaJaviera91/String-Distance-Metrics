import duckdb
import os

# ------------------------------------------------
# 1. Conectarse a la base DuckDB
# ------------------------------------------------
# Se crea (o abre) el archivo warehouse.db donde se guardarán las tablas
con = duckdb.connect('data/warehouse.db')

# ------------------------------------------------
# 2. Crear vistas RAW leyendo los archivos CSV originales
# ------------------------------------------------
# Estas vistas permiten consultar los CSV sin cargarlos permanentemente

con.execute("""
CREATE OR REPLACE VIEW productos_raw AS
SELECT *
FROM read_csv_auto('src/data/raw/productos.csv');
""")

con.execute("""
CREATE OR REPLACE VIEW clientes_raw AS
SELECT *
FROM read_csv_auto('src/data/raw/clientes.csv');
""")

# ------------------------------------------------
# 3. Normalizar los datos (solo convertir a MAYÚSCULAS)
# ------------------------------------------------
# Esto facilita el matching con algoritmos como Levenshtein o Soundex

# Normalización del archivo de productos
con.execute("""
CREATE OR REPLACE TABLE productos_normalizados AS
SELECT
    UPPER(producto) AS producto,
    UPPER(categoria) AS categoria,
    UPPER(pais) AS pais,
    UPPER(marca) AS marca,
    anio -- se mantiene igual porque es numérico
FROM productos_raw;
""")

# Normalización del archivo de clientes
con.execute("""
CREATE OR REPLACE TABLE clientes_normalizados AS
SELECT
    UPPER(nombre) AS nombre,
    UPPER(apellido) AS apellido,
    UPPER(pais) AS pais,
    UPPER(email) AS email,
    edad -- dato numérico, no se transforma
FROM clientes_raw;
""")

# ------------------------------------------------
# 4. Crear carpeta 'clean' si no existe
# ------------------------------------------------
# Asegura que la carpeta de salida esté disponible antes de exportar
os.makedirs("src/data/clean", exist_ok=True)

# ------------------------------------------------
# 5. Exportar los archivos limpios (CSV CLEAN)
# ------------------------------------------------

# Exportar productos normalizados con precio
con.execute("""
COPY productos_normalizados
TO 'src/data/clean/productos_con_precio.csv'
WITH (HEADER, DELIMITER ',');
""")

# Exportar clientes normalizados o productos sin precio (ajusta nombre según tu caso)
con.execute("""
COPY clientes_normalizados
TO 'src/data/clean/productos_sin_precio.csv'
WITH (HEADER, DELIMITER ',');
""")

print("CSV clean generados correctamente.")
