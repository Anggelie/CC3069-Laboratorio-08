# Ejercicio 2

Para `n <= 1` se retorna inmediatamente: **Θ(1)**.

Para `n > 1`, el ciclo exterior realiza `n` iteraciones y el interior se interrumpe en la primera por `break`. Por tanto hay `n` impresiones y **T(n) = Θ(n)**, luego **O(n)**.

El programa conserva las impresiones y redirige su salida durante el profiling.