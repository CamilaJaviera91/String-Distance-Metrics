![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)

---

# String Distance Metrics

Este repositorio contiene una **colección de métodos y algoritmos de métricas de distancia y similitud entre cadenas de texto**, diseñados para cuantificar qué tan similares o diferentes son dos strings (*string matching / string similarity*).

Estas métricas son especialmente útiles en tareas de **limpieza de datos, fuzzy matching, deduplicación, data quality** y en escenarios donde los datos textuales contienen **errores tipográficos, diferencias de formato y ruido**, algo común en datasets reales provenientes de múltiples fuentes.

---

## Documentación Visual de Algoritmos

**Sugerencia:**
| Métrica | Caso de Uso Ideal |
| :--- | :--- |
| **Levenshtein** | Errores de escritura general (inserción, borrado). |
| **Damerau-Levenshtein** | Útil para intercambios de letras adyacentes (transposiciones). |
| **Jaro-Winkler** | Ideal para nombres propios o strings cortos. |
| **Soundex / Metaphone** | Similitud fonética (como suenan las palabras). |

---

## Descripción

El proyecto ofrece una implementación centralizada de algoritmos de **distancia entre cadenas de texto**, junto con utilidades para:

- Generar datasets sintéticos.
- Inyectar errores tipográficos realistas.
- Normalizar texto para mejorar la comparación.
- Medir similitud entre campos textuales.

Este tipo de herramientas se utiliza comúnmente en procesos de *data cleaning*, *record linkage*, *entity matching* y en la integración de datos heterogéneos.

---

## Características

- Generación de typos realistas que simulan errores humanos.
- Implementaciones propias de métricas de distancia.
- Funciones de normalización textual.
- Arquitectura modular para extender métricas o pipelines.
- Tests automatizados para asegurar calidad de código.

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

## Descripción de las Bases de Datos

### Base con precios (`base_categoria_con_precio.csv`)

Contiene los siguientes campos:

    - `producto`
    - `categoria`
    - `pais`
    - `anio`
    - `marca`
    - `precio_usd`

Los precios se generan de forma aleatoria, pero respetando **rangos realistas por categoría**, lo que permite simular escenarios cercanos a datos reales.


| Categoría | Rango (USD) |
|-----------|-------------|
|Electrónica| 80 – 1500   |
|   Hogar   | 10 - 300    |
|  Deporte  | 15 - 400    |
|Juguetería | 5 - 120     |
|Computación| 90 – 2000   |
|  Belleza  | 5 – 200     |
|Automotriz | 20 - 800    |

---

### Base sin precios y con typos (`base_categoria_sin_precio.csv`)

- Contiene:
    - `producto`
    - `categoria` 
    - `pais`
    - `marca` 

Aproximadamente un **30% de los registros contienen errores tipográficos realistas**, tales como:

- Teclas cercanas en el teclado
- Eliminación de caracteres
- Duplicación de letras
- Intercambio de caracteres (swap)
- Reemplazos comunes en la vida real

**Ejemplos:**

- `SAMSUNG → SANSUNG`
- `ADIDAS → ADIDSA`

Este dataset simula un escenario real donde los datos provienen de distintas fuentes con inconsistencias, siendo ideal para pruebas de **fuzzy matching y record linkage**.

---

## Lógica Principal del Código

### Generación de productos y categorías

- Se generan **50** productos asociados a una categoría:
  - Electrónica
  - Hogar
  - Deporte
  - Juguetería
  - Computación
  - Belleza
  - Automotriz

### Generación de la base con precios

- Se crean combinaciones de:
  - producto
  - país
  - año
- Se asigna un precio coherente según la categoría del producto.

### Generación de la base sin precios

- Se utiliza la misma lógica de combinaciones, excluyendo la columna `precio_usd`.

### Inyección de typos

- Se aplica una función de generación de errores basada en:
  - mapas de teclas cercanas
  - manipulación directa de caracteres
  - reglas comunes de error humano
  - aleatoriedad controlada (~30%)

---

## Pipeline de Limpieza y Normalización

1. Lectura de ambas bases desde `data/raw`.
2. Creación de vistas RAW.
3. Normalización del texto (mayúsculas, limpieza básica).
4. Exportación a `data/clean`:
   - `productos_con_precio.csv`
   - `productos_sin_precio.csv`

Este pipeline facilita la aplicación posterior de métricas de similitud de manera más efectiva.

---

## Autor

**Camila Javiera Muñoz Navarro**  
Ingeniera de Datos  

---

## Contribuciones

¡Las contribuciones son bienvenidas!

1. Haz un fork del repositorio
2. Crea una rama con tu feature
3. Abre un Pull Request con una descripción clara de los cambios

---

## Licencia

Este proyecto está bajo la licencia **MIT**.