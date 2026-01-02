# String Distance Metrics

- Este repositorio contiene una **colección de métodos y algoritmos de métricas de distancia y similitud** diseñados para cuantificar qué tan similares o diferentes son dos cadenas de texto (*string matching* / *string similarity*). Estas métricas son útiles para tareas como limpieza de datos, fuzzy matching, deduplicación y análisis de calidad de datos.

- Las métricas incluidas permiten comparar textos que pueden contener **errores tipográficos, diferencias de formato y ruido de datos**, lo cual es común cuando se trabaja con datasets reales.

- se Utilizará:

    - Fuzzy Matching: 
        - Levenshtein.
        - Soundex.
        - Jaro-Winkler.
        - LCS.
        - Metaphone.
    - Procesos de normalización y limpieza.
    - Pipelines ETL.
    - Data Quality.
    - Modelos de ML afectados por ruido en los datos.

---

## Descripción

Este proyecto ofrece una implementación centralizada de algoritmos de **distancia entre cadenas de texto**, además de utilidades para:

- Generar datasets sintéticos  
- Introducir errores tipográficos realistas  
- Normalizar texto para mejor comparación  
- Medir similitud entre campos de datos

Este tipo de herramientas se utiliza en *data cleaning*, *record linkage*, *entity matching*, y procesos de integración de datos donde los valores de texto no coinciden exactamente.

---

## Características

- Generación de typos realistas para simular errores humanos
- Implementaciones propias de algoritmos de distancia
- Funciones de normalización de texto
- Arquitectura modular para integrar más métricas o pipelines
- Tests automatizados para asegurar calidad de código

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

### **Base con precios (`base_categoria_con_precio.csv`)**
- Contiene:
    - `producto`
    - `categoria`
    - `pais`
    - `anio`
    - `marca`
    - `precio_usd`

- Los precios son generados de forma aleatoria pero dependiendo del **rango de cada categoría**, lo que agrega realismo.

| Categoría | Rango (USD) |
|-----------|-------------|
|Electrónica| 80 – 1500   |
|   Hogar   | 10 - 300    |
|  Deporte  | 15 - 400    |
|Juguetería | 5 - 120     |
|Computación| 90 – 2000   |
|  Belleza  | 5 – 200     |
|Automotriz | 20 - 800    |

### **Base sin precios y con typos (`base_categoria_sin_precio.csv`)**

- Contiene:
    - `producto`
    - `categoria` 
    - `pais`
    - `marca` 
    - *(con errores tipográficos en aprox. 30% de los registros)*

- Los typos son **realistas**:
    - Teclas cercanas.
    - Eliminación de letras.
    - Duplicación.
    - Swap/intercambio de caracteres.
    - Reemplazos comunes reales:
        - Ejemplo: 
            - `SAMSUBG → SANSUNG`
            - `ADIDAS → ADIDSA`

- Esto simula un **escenario real** donde los datos provienen de múltiples fuentes y contienen inconsistencias.

- Ideal para **fuzzy matching**.

---

## **Lógica Principal del Código**

### **Generación de productos y categorías**
- Se crean 50 productos con una categoría asociada:
    - Electrónica
    - Hogar
    - Deporte
    - Juguetería
    - Computación
    - Belleza
    - Automotriz

### **Generación de la base con precios**
- Combina todas las combinaciones de:
    - producto
    - país
    - año

- Asigna un precio coherente según su categoría.

### **Generación de la base sin precios**
- La misma estructura de combinaciones, pero sin la columna de `precio_usd`.

### **Inyección de typos**
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
4. Exportación a `src/data/clean`:
    - `productos_con_precio.csv`
    - `productos_sin_precio.csv`

- Este proceso permite ejecutar métricas de similitud de forma más efectiva.

---

## Autor

Camila Javiera Muñoz Navarro <br>
Ingeniera de Datos <br>

---

## Contribuciones

- ¡Las contribuciones son bienvenidas!
- Si quieres agregar nuevas métricas, mejorar documentación o ampliar tests:
    1. Haz un fork del repositorio
    2. Crea una rama con tu feature
    3. Abre un *Pull Request* con descripción clara de los cambios

---