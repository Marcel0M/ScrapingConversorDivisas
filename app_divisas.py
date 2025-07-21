
import streamlit as st
import pandas as pd
from io import BytesIO

from func_divisas import obtener_valor_dolar, obtener_valor_euro


#Interfaz 
st.set_page_config(page_title="Calculadora de divisas", layout="centered")
st.title("Calculadora divisas automático 💱")

archivo = st.file_uploader("📂 Sube tu archivo Excel o CSV", type=["xlsx", "csv"])

if archivo:
    if archivo.name.endswith(".csv"):
        df = pd.read_csv(archivo)
    else:
        df = pd.read_excel(archivo)

    st.subheader("📄 Vista previa del archivo")
    st.dataframe(df.head())

    comision = st.number_input("💰 Ingresa el % de comisión que se aplicara al cambio", min_value=0.0, max_value=100.0, value=3.0)

    if st.button("🧮 Calcular"):
        try:
            #Obtener valores externos
            valor_dolar = obtener_valor_dolar()
            valor_euro = obtener_valor_euro()

            #Identificar columnas con numeros
            columnas_numericas = df.select_dtypes(include=["number"]).columns.tolist()
            if not columnas_numericas:
                st.warning("No se encontraron columnas numéricas para calcular.")
                st.stop()

            #Sumar columnas por fila
            df["Total_CLP"] = df[columnas_numericas].sum(axis=1)

            #Conversión de divisas
            df["CLP_a_USD"] = df["Total_CLP"] / valor_dolar
            df["CLP_a_EUR"] = df["Total_CLP"] / valor_euro

            #Aplicar comisión
            factor = 1 - (comision / 100)
            df["CLP_a_USD_con_comision"] = (df["CLP_a_USD"] * factor).round(2)
            df["CLP_a_EUR_con_comision"] = (df["CLP_a_EUR"] * factor).round(2)

            #Mostrar resultados con formato
            df_mostrar = df.copy()
            df_mostrar["CLP_a_USD_con_comision"] = df_mostrar["CLP_a_USD_con_comision"].apply(lambda x: f"${x:,.2f}")
            df_mostrar["CLP_a_EUR_con_comision"] = df_mostrar["CLP_a_EUR_con_comision"].apply(lambda x: f"${x:,.2f}")

            st.success(f"Cálculo exitoso dólar: ${valor_dolar:.2f} y euro: ${valor_euro:.2f}")
            st.dataframe(df_mostrar)

            #Descargar archivo Excel
            output = BytesIO()
            with pd.ExcelWriter(output, engine="openpyxl") as writer:
                df.to_excel(writer, index=False)

            st.download_button(
                "📥 Descargar archivo con resultados",
                output.getvalue(),
                file_name="resultado.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        except Exception as e:
            st.error(f"❌ Error: {e}")
