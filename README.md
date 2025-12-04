# String Distance Metrics

Este proyecto genera dos datasets sintéticos con información de productos, países, marcas y categorías, diseñados para simular escenarios reales donde existen errores tipográficos, inconsistencias de **formato y datos faltantes**.

<br>

Los datasets permiten probar algoritmos y herramientas como:

- ✨ Fuzzy Matching: Levenshtein, Soundex, Jaro-Winkler, LCS

---

## 📂 **Descripción de las Bases**

### **1. Base con precios (`base_categoria_con_precio.csv`)**
- Contiene:
    - `producto`
    - `categoria`
    - `pais`
    - `anio`
    - `marca`
    - `precio_usd`

Los precios son generados de forma aleatoria pero **dependiendo del rango de cada categoría**, lo que agrega realismo.

- Rangos:
    - Electrónica: 80 – 1500 USD.
    - Hogar: 10 - 300 USD.
    - Deporte: 15 - 400 USD.
    - Juguetería: 5 - 120 USD.
    - Computación: 90 – 2000 USD.
    - Belleza: 5 – 200 USD.
    - Automotriz: 20 - 800 USD.

### **2. Base sin precios y con typos (`base_categoria_sin_precio.csv`)**

- Contiene:
    - `producto`
    - `categoria` 
    - `pais`
    - `marca` *(con errores tipográficos en aprox. 30% de los registros)*

<br>

Los typos son **realistas**, mezclando:
- Teclas cercanas.
- Eliminación de letras.
- Duplicación.
- Swap/intercambio de caracteres.
- Reemplazos comunes reales:
    - Ejemplo: `SAMSUBG → SANSUNG`, `ADIDAS → ADIDSA`

<br>

Esto simula un escenario real donde los datos provienen de múltiples fuentes y contienen inconsistencias.

---

## 🧠 **Lógica Principal del Código**

### ✔ **1. Generación de productos y categorías**
Se crean 50 productos con una categoría asociada (Electrónica, Hogar, Deporte, etc.).

### ✔ **2. Generación de la base con precios**
- Combina todas las combinaciones de:
    - producto
    - país
    - año

y asigna un precio coherente según su categoría.

### ✔ **3. Generación de la base sin precios**
La misma estructura de combinaciones, pero sin la columna de `precio_usd`.

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

Este proceso permite ejecutar métricas de similitud de forma más efectiva.

---

## ✨ Autor

Camila Javiera Muñoz Navarro <br>
Ingeniera de Datos <br>