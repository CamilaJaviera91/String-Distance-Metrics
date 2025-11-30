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
CREATE OR REPLACE VIEW con_precio AS
SELECT *
FROM read_csv_auto('src/data/raw/base_categoria_con_precio.csv');
""")

con.execute("""
CREATE OR REPLACE VIEW sin_precio AS
SELECT *
FROM read_csv_auto('src/data/raw/base_categoria_sin_precio.csv');
""")

# ------------------------------------------------
# 3. Normalizar los datos (solo convertir a MAYÚSCULAS)
# ------------------------------------------------
# Esto facilita el matching con algoritmos como Levenshtein o Soundex

# Normalización del archivos
con.execute("""
            CREATE OR REPLACE TABLE con_precio_normalizados AS
            SELECT
            UPPER(producto) AS producto
            , UPPER(categoria) AS categoria
            , UPPER(pais) AS pais
            , UPPER(marca) AS marca
            , anio
            , precio_usd
            FROM con_precio;
            """)

con.execute("""
            CREATE OR REPLACE TABLE sin_precio_normalizados AS
            SELECT
            UPPER(producto) AS producto
            , UPPER(categoria) AS categoria
            , UPPER(pais) AS pais
            , UPPER(marca) AS marca
            , anio
            FROM sin_precio;
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

# Exportar productos normalizados sin precio
con.execute("""
COPY clientes_normalizados
TO 'src/data/clean/productos_sin_precio.csv'
WITH (HEADER, DELIMITER ',');
""")

print("CSV clean generados correctamente.")
