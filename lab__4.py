import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ventas.csv")
df["Ganancia"] = df["Ventas"] - df["Gastos"]

plt.plot(df["Mes"], df["Ventas"], label="Ventas", color="red", linestyle="dashed", marker="o")
plt.plot(df["Mes"], df["Gastos"], label="Gastos", color="blue", linestyle="solid", marker="x")
plt.xlabel("Mes")
plt.ylabel("Cantidad")
plt.title("Evolución mensual de las ventas y los gastos")
plt.legend()
plt.show()