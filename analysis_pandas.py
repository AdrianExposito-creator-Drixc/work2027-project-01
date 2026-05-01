import pandas as pd


def main():
    df = pd.read_csv("data/ventas.csv")

    df["total"] = df["precio"] * df["cantidad"]

    total_ventas = df["total"].sum()
    total_items = df["cantidad"].sum()
    ventas_por_producto = df.groupby("producto")["total"].sum()

    print(f"Total ventas: {total_ventas}")
    print(f"Total items: {total_items}")
    print("Ventas por producto:")
    print(ventas_por_producto)


if __name__ == "__main__":
    main()
