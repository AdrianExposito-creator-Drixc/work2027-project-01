# Work2027 – Project 01

## Descripción

Proyecto básico de análisis de ventas con Python.

Incluye:

- Lectura de CSV
- Cálculo de métricas
- Agrupación por producto
- Exportación de resultados
- Versión con pandas
- Visualización

## Tecnologías

- Python 3
- pandas
- matplotlib

## Estructura

```text
project_01/
├── data/
│   └── ventas.csv
├── output/
│   ├── resumen.txt
│   └── ventas.png
├── main.py
├── analysis_pandas.py
├── plot.py
├── requirements.txt
└── README.md
cd ~/work2027/projects/project_01

cat > README.md <<'EOF'
# Work2027 – Project 01

## Descripción

Proyecto básico de análisis de ventas con Python.

Incluye:

- Lectura de archivo CSV
- Cálculo de ventas totales
- Cálculo de productos vendidos
- Agrupación por producto
- Exportación de resultados a archivo
- Versión con pandas
- Generación de gráficos con matplotlib

## Tecnologías

- Python 3
- pandas
- matplotlib

## Estructura del proyecto

    project_01/
    ├── data/
    │   └── ventas.csv
    ├── output/
    │   ├── resumen.txt
    │   └── ventas.png
    ├── main.py
    ├── analysis_pandas.py
    ├── plot.py
    ├── requirements.txt
    └── README.md

## Ejecución

Activar entorno virtual:

    source .venv/bin/activate

Ejecutar versión básica:

    python main.py

Ejecutar versión con pandas:

    python analysis_pandas.py

Generar gráfico:

    python plot.py

## Resultados

- Resumen: output/resumen.txt
- Gráfico: output/ventas.png

## Objetivo

Primer proyecto Work2027 orientado a análisis de datos, estructura profesional de repositorio y preparación de portfolio técnico.

## Próximos pasos

- Añadir CLI
- Validar datos de entrada
- Añadir logging
- Exportar a CSV/Excel
- Automatizar todo en un solo script
