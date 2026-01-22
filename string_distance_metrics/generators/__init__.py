"""
string_distance_metrics
=======================

Paquete para la generación y evaluación de métricas de distancia y similitud
entre cadenas de texto.

Módulos principales:
    - ``typo_generator``: genera errores tipográficos realistas sobre strings.
    - ``dataset_generator``: produce datasets sintéticos limpios y con typos.

Ejemplo de uso rápido::

    from string_distance_metrics import generate_realistic_typo

    original = "Laptop"
    con_typo = generate_realistic_typo(original)
    