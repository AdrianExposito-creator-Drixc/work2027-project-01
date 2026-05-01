import csv
from collections import defaultdict
from pathlib import Path


def analizar_csv(ruta):
    total_ventas = 0.0
    total_items = 0
    ventas_por_producto = defaultdict(float)

    with open(ruta, newline="") as archivo:
        reader = csv.DictReader(archivo)

        for fila in reader:
            precio = float(fila["precio"])
            cantidad = int(fila["cantidad"])
            producto = fila["producto"]

            total_ventas += precio * cantidad
            total_items += cantidad
            ventas_por_producto[producto] += precio * cantidad

    return total_ventas, total_items, ventas_por_producto


def exportar_resumen(ruta_salida, total, items, por_producto):
    Path(ruta_salida).parent.mkdir(parents=True, exist_ok=True)

    with open(ruta_salida, "w") as archivo:
        archivo.write(f"Total ventas: {total}\n")
        archivo.write(f"Total items: {items}\n")
        archivo.write("Ventas por producto:\n")

        for producto, venta in por_producto.items():
            archivo.write(f"{producto},{venta}\n")


def main():
    ruta = "data/ventas.csv"
    salida = "output/resumen.txt"

    total, items, por_producto = analizar_csv(ruta)

    print(f"Total ventas: {total}")
    print(f"Total items vendidos: {items}")
    print("Ventas por producto:")

    for producto, venta in por_producto.items():
        print(f"  {producto}: {venta}")

    exportar_resumen(salida, total, items, por_producto)
    print(f"Resumen guardado en {salida}")


if __name__ == "__main__":
    main()
