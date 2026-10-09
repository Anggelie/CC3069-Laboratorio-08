"""Ejercicio 3: implementación y profiling."""
import csv
import contextlib
import os
import time
from pathlib import Path

def algoritmo(n):
    for i in range(1, n // 3 + 1):
        for j in range(1, n + 1, 4):
            print("Sequence")

VALORES = (1, 10, 100, 1000, 10000, 100000, 1000000)
PRESUPUESTO = 5_000_000

def main():
    resultados = []
    for n in VALORES:
        operaciones = (n // 3) * ((n + 3) // 4)
        if operaciones > PRESUPUESTO:
            resultados.append((n, "", operaciones, "no ejecutado: costo elevado"))
            continue
        inicio = time.perf_counter()
        with open(os.devnull, "w", encoding="utf-8") as salida:
            with contextlib.redirect_stdout(salida):
                algoritmo(n)
        segundos = time.perf_counter() - inicio
        resultados.append((n, f"{segundos:.9f}", operaciones, "medido"))
        print(f"n={n}: {segundos:.9f} s")
    carpeta = Path(__file__).resolve().parent
    with (carpeta / "resultados.csv").open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(("n", "segundos", "operaciones_estimadas", "estado"))
        escritor.writerows(resultados)
    import matplotlib.pyplot as plt
    puntos = [(int(n), float(t)) for n, t, _, estado in resultados if estado == "medido"]
    plt.plot([n for n, _ in puntos], [t for _, t in puntos], marker="o")
    plt.xlabel("Tamaño de entrada n")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Ejercicio 3")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(carpeta / "grafica.png", dpi=150)

if __name__ == "__main__":
    main()
