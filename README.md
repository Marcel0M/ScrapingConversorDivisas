# 💱 Calculadora de Divisas con Scrapping (CLP → USD / EUR)

Este proyecto permite **cargar un Excel o CSV con valores (CLP)** y calcular su equivalencia en **dólares (USD)** y **euros (EUR)**, con opción de aplicar una comisión personalizada.


---

## 🚀 Requisitos

- Python 3.8+

Instala dependencias:

- pip install -r requirements.txt

- pip install pandas requests beautifulsoup4 lxml openpyxl streamlit


---

## ✅ Modo consola (`proto_divisas.py`)

### 🔹 Uso


- python proto_divisas.py


### 🔹 Qué hace

1. Te pedirá ingresar el nombre de un archivo Excel o CSV (ej: `calculoPrueba.xlsx`)
2. Detectará automáticamente las columnas numéricas.
3. Obtendrá el valor **actual del dólar y euro** desde el sitio del Banco Central de Chile.
4. Te pedirá un porcentaje de comisión (ej: 3.0)
5. Realizará el cálculo y mostrará los resultados en consola.
6. Guardará un nuevo archivo con los resultados, agregando las columnas:
   - `Total_CLP`
   - `CLP_a_USD_con_comision`
   - `CLP_a_EUR_con_comision`

---

## 🌐 Modo web (`app_divisas.py`)

### 🔹 Uso


- streamlit run app_divisas.py


### 🔹 Qué hace

1. Carga archivos `.xlsx` o `.csv` mediante interfaz visual.
2. Vista previa del archivo cargado.
3. Permite ingresar el porcentaje de comisión.
4. Obtiene automáticamente el valor del dólar y euro (scraping).
5. Muestra los resultados con formato amigable.
6. Permite descargar el archivo actualizado con los cálculos.

---

## 📤 Entrada esperada

Un archivo Excel o CSV con estructura como:

| Nombre Empresa | Junio    | Julio    | Agosto   |
|----------------|----------|----------|----------|
| Empresa A      | 2000000  | 3500000  | 4000     |
| Empresa B      | 1000000  | 1500000  | 8000     |
| Empresa C      | 4500000  | 2000000  | 700      |

---

## 📥 Salida generada

El sistema agrega columnas calculadas:

| Total_CLP | CLP_a_USD_con_comision | CLP_a_EUR_con_comision |
|-----------|------------------------|-------------------------|
| 5504000   | $5,408.47              | $4,668.57               |
| ...       | ...                    | ...                     |

---

## ⚠️ Notas

- El valor del dólar y euro se obtiene en tiempo real desde [https://www.bcentral.cl/inicio](https://www.bcentral.cl/inicio)
- En consola no se necesita Streamlit. Usa `proto_divisas.py`.

---
