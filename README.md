# CC3069 — Laboratorio No. 8

Análisis matemático y experimental de complejidad temporal.

## Estructura
- `ejercicio_01/`: programa y análisis de O(n² log n).
- `ejercicio_02/`: programa y análisis de O(n).
- `ejercicio_03/`: programa y análisis de O(n²).
- `ejercicio_04/`: búsqueda lineal, tres casos.
- `ejercicio_05/`: verdadero/falso justificado.

## Ejecución
Requiere Python 3.10 o superior.

```bash
pip install -r requirements.txt
python ejercicio_01/main.py
python ejercicio_02/main.py
python ejercicio_03/main.py
```

Cada programa genera `resultados.csv` y `grafica.png` en su carpeta al ejecutarse. Se conserva el `print` de los ejercicios 2 y 3, redirigiendo la salida a un dispositivo nulo para evitar inundar la consola.

## Límites experimentales
Los scripts usan un presupuesto de cinco millones de operaciones estimadas. Si una entrada excede el presupuesto, se registra como **no ejecutada**, no como medición. Esto permite documentar los siete valores solicitados sin presentar tiempos inventados. Las gráficas incluyen únicamente mediciones completadas. Los resultados dependen del equipo donde se ejecuten.

## Análisis
Los archivos Markdown contienen los procedimientos. La versión descargable del laboratorio incluye también PDFs por ejercicio.

## Video de demostración
**Pendiente:** añadir aquí el enlace a YouTube no listado (duración máxima de 10 minutos) después de grabar la ejecución real.

## Colaboradores
**Pendiente:** invitar al catedrático y auxiliares indicados en Canvas.
