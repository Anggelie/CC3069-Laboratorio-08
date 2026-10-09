# Ejercicio 1

Ciclo exterior: `n - floor(n/2) + 1 = Θ(n)` iteraciones.

Ciclo intermedio: `n - floor(n/2) = Θ(n)` iteraciones.

Ciclo interior: `floor(log2(n)) + 1 = Θ(log n)` iteraciones, porque `k` se duplica.

Por producto: **T(n) = Θ(n² log n)**, luego **O(n² log n)**.

El programa genera `resultados.csv` y `grafica.png` con las ejecuciones realizadas; los tamaños demasiado costosos se indican como no ejecutados.