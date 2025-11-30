COPY productos_normalizados
TO 'src/data/clean/productos_con_precio.csv'
WITH (HEADER, DELIMITER ',');

COPY clientes_normalizados
TO 'src/data/clean/productos_sin_precio.csv'
WITH (HEADER, DELIMITER ',');
