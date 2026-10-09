# Ejercicio 4: búsqueda lineal

- **Mejor caso:** clave en primera posición, 1 comparación: **Θ(1)**.
- **Caso promedio:** suponiendo que la clave existe y cada posición es equiprobable, comparaciones esperadas `(1+...+n)/n = (n+1)/2`: **Θ(n)**.
- **Peor caso:** clave al final o ausente, `n` comparaciones: **Θ(n)**.

Si hay probabilidad constante de búsquedas fallidas, el caso promedio continúa siendo Θ(n).