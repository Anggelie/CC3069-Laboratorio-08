# Ejercicio 3

El ciclo exterior ejecuta `floor(n/3)` iteraciones. El interior recorre `1, 5, 9, ...` hasta `n`, es decir `ceil(n/4)` iteraciones.

**T(n) = Θ(floor(n/3) · ceil(n/4)) = Θ(n²)**, luego **O(n²)**.

El programa conserva las impresiones y redirige su salida durante el profiling.