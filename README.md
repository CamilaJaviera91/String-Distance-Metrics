# String Distance Metrics

Este proyecto genera dos bases de datos sintéticas relacionadas con productos, marcas y países. <br>
El objetivo es simular escenarios reales donde existen inconsistencias en los datos, como **errores tipográficos (typos)** en marcas, variación de categorías, y precios dependientes del tipo de producto.

<br>

Este dataset es útil para pruebas de:
- Normalización y limpieza de datos.
- Fuzzy matching.
- Detección y corrección de typos.
- Procesos ETL y validación.
- Modelos de ML basados en calidad de datos.

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

- Ejemplo de rangos:
    