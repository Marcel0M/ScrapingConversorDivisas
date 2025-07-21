import pandas as pd

from func_divisas import obtener_valor_dolar, obtener_valor_euro

#Cargar archivo Excel o CSV
archivo = input("Ingresa el nombre del archivo (ej: datos.xlsx o datos.csv): ")

if archivo.endswith(".csv"):
    df = pd.read_csv(archivo)
else:
    df = pd.read_excel(archivo)

print("Archivo cargado exitosamente.\nPrimeras filas:")
print(df.head())


#Solicitar porcentaje de comisión
try:
    comision = float(input("\nIngresa el % de comisión que se aplicará (ej: 3): "))
except ValueError:
    print("Entrada no válida. Se usará comisión por defecto: 3%")
    comision = 3.0

#Realizar cálculos
try:
    valor_dolar = obtener_valor_dolar()
    valor_euro = obtener_valor_euro()
    print(f"Dólar observado: ${valor_dolar:.2f}")
    print(f"Euro observado: ${valor_euro:.2f}")
except Exception as e:
    print(f"Error al obtener valores desde el Banco Central: {e}")
    exit(1)

columnas_numericas = df.select_dtypes(include=["number"]).columns.tolist()
if not columnas_numericas:
    print("No se encontraron columnas numéricas para calcular.")
    exit(1)

df["Total_CLP"] = df[columnas_numericas].sum(axis=1)
df["CLP_a_USD"] = df["Total_CLP"] / valor_dolar
df["CLP_a_EUR"] = df["Total_CLP"] / valor_euro

factor = 1 - (comision / 100)
df["CLP_a_USD_con_comision"] = (df["CLP_a_USD"] * factor).round(2)
df["CLP_a_EUR_con_comision"] = (df["CLP_a_EUR"] * factor).round(2)

#Mostrar resumen final
print("Resultados:")
print(df[["Total_CLP", "CLP_a_USD_con_comision", "CLP_a_EUR_con_comision"]])

#Guardar resultado
nombre_salida = archivo.replace(".xlsx", "_resultado.xlsx").replace(".csv", "_resultado.xlsx")
df.to_excel(nombre_salida, index=False)
print(f"Archivo guardado como: {nombre_salida}")