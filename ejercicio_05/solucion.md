# Ejercicio 5

**a) Verdadero.** Θ es transitiva y simétrica: `f=Θ(g)` y `g=Θ(h)` implican `h=Θ(f)`.

**b) Verdadero.** Por transitividad, `f=O(h)`, equivalente a `h=Ω(f)`.

**c) Falso.** Se recorren Θ(n²) pares `(i,j)`, pero cortar la tupla y calcular el hash del segmento cuesta proporcionalmente a su longitud. La suma de longitudes de los segmentos es Θ(n³), de modo que el tiempo esperado habitual es **Θ(n³)**, no Θ(n!).