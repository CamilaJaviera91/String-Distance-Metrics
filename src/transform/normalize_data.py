import duckdb
import os

# ------------------------------------------------
# 1. Connect to DuckDB
# ------------------------------------------------
con = duckdb.connect('data/warehouse.db')


# ------------------------------------------------
# 2. Create RAW views (reading the CSVs)
# ------------------------------------------------
con.execute("""
CREATE OR REPLACE VIEW productos_con_precio AS
SELECT *
FROM read_csv_auto('src/data/base_categoria_con_precio.csv');
""")

con.execute("""
CREATE OR REPLACE VIEW productos_sin_precio AS
SELECT *
FROM read_csv_auto('src/data/base_categoria_sin_precio.csv');
""")

# ------------------------------------------------
# 3. Normalize data (UPPERCASE)
# ------------------------------------------------

# Productos con precio
con.execute("""
CREATE OR REPLACE TABLE productos_con_precio AS
SELECT
    UPPER(producto) AS producto
    , UPPER(categoria) AS categoria
    , UPPER(pais) AS pais
    , UPPER(marca) AS marca
    , anio
    , precio_usd
FROM productos_con_precio;
""")

# Productos sin precio
con.execute("""
CREATE OR REPLACE TABLE productos_sin_precio AS
SELECT
    UPPER(producto) AS producto
    , UPPER(categoria) AS categoria
    , UPPER(pais) AS pais
    , UPPER(marca) AS marca
    , anio
FROM productos_sin_precio;
""")
