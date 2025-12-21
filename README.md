# String Distance Metrics

Este proyecto genera dos datasets sintéticos con información de productos, países, marcas y categorías, diseñados para simular escenarios reales donde existen errores tipográficos, inconsistencias de **formato y datos faltantes**.

<br>

- Los datasets permiten probar algoritmos y herramientas como:

    - Fuzzy Matching: Levenshtein, Soundex, Jaro-Winkler, LCS
    - Procesos de normalización y limpieza
    - Pipelines ETL
    - Data Quality
    - Modelos de ML afectados por ruido en los datos

---

## Estructura del Proyecto

```
..
String-Distance-Metrics/
│
├── string_distance_metrics/
│   ├── __init__.py
│   ├── generators/
│   │   ├── __init__.py
│   │   └── typo_generator.py
│   │
│   ├── distances/
│   │   ├── __init__.py
│   │   ├── levenshtein.py
│   │   ├── jaro_winkler.py
│   │   └── damerau_levenshtein.py
│   │
│   ├── cleaning/
│   │   ├── __init__.py
│   │   └── normalizer.py
│   │
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
│
├── tests/
│   ├── test_typo_generator.py
│   ├── test_levenshtein.py
│   └── test_normalizer.py
│
├── examples/
│   └── 01_basic_usage.ipynb
│
├── data/
│   ├── raw/
│   ├── dirty/
│   └── clean/
│
├── requirements.txt
└── README.md

```

---

## **Descripción de las Bases**

### **1. Base con precios (`base_categoria_con_precio.csv`)**
- Contiene:
    - `producto`
    - `categoria`
    - `pais`
    - `anio`
    - `marca`
    - `precio_usd`

- Los precios son generados de forma aleatoria pero **dependiendo del rango de cada categoría**, lo que agrega realismo.

| Categoría | Rango (USD) |
|-----------|-------------|
|Electrónica| 80 – 1500   |
|   Hogar   | 10 - 300    |
|  Deporte  | 15 - 400    |
|Juguetería | 5 - 120     |
|Computación| 90 – 2000   |
|  Belleza  | 5 – 200     |
|Automotriz | 20 - 800    |

### **2. Base sin precios y con typos (`base_categoria_sin_precio.csv`)**

- Contiene:
    - `producto`
    - `categoria` 
    - `pais`
    - `marca` *(con errores tipográficos en aprox. 30% de los registros)*

<br>

- Los typos son **realistas**, mezclando:
    - Teclas cercanas.
    - Eliminación de letras.
    - Duplicación.
    - Swap/intercambio de caracteres.
    - Reemplazos comunes reales:
        - Ejemplo: 
            - `SAMSUBG → SANSUNG`
            - `ADIDAS → ADIDSA`

<br>

- Esto simula un escenario real donde los datos provienen de múltiples fuentes y contienen inconsistencias.

<br>

- Ideal para fuzzy matching.

---

## **Lógica Principal del Código**

### **1. Generación de productos y categorías**
- Se crean 50 productos con una categoría asociada (Electrónica, Hogar, Deporte, etc.).

### **2. Generación de la base con precios**
- Combina todas las combinaciones de:
    - producto
    - país
    - año

- Asigna un precio coherente según su categoría.

### **3. Generación de la base sin precios**
- La misma estructura de combinaciones, pero sin la columna de `precio_usd`.

### ✔ **4. Inyección de typos**
- La función de typos utiliza:
    - Mapas de teclas cercanas de teclado
    - Manipulación directa de caracteres
    - Reemplazos frecuentes en la vida real
    - Aleatoriedad controlada (*~30%*)

---

## Pipeline de Limpieza 

1. Lectura de ambas bases desde `src/data/raw` mediante `read_csv_auto()`.
2. Creación de vistas RAW.
3. Normalización (*solo mayúsculas*) para facilitar fuzzy matching.
4. Exportación a `src/data/clean` como:
    - `productos_con_precio.csv`
    - `productos_sin_precio.csv`

- Este proceso permite ejecutar métricas de similitud de forma más efectiva.

---

## Autor

Camila Javiera Muñoz Navarro <br>
Ingeniera de Datos <br>
