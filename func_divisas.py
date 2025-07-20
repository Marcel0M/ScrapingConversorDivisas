import requests
from bs4 import BeautifulSoup
import re


#Función: obtener valor del dólar
@st.cache_data
def obtener_valor_dolar():
    url = "https://www.bcentral.cl/inicio"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "lxml")
    contenedor = soup.find("div", {"class": "tooltip-wrap", "title": "USD: Valor Dólar Observado del Día"})
    if not contenedor:
        raise ValueError("No se encontró el contenedor con el valor del dólar.")
    texto_valor = contenedor.get_text()
    match = re.search(r"\$([0-9]+,[0-9]+)", texto_valor)
    if not match:
        raise ValueError("No se pudo extraer el valor del dólar.")
    valor_str = match.group(1).replace(",", ".")
    return float(valor_str)

#Función: obtener valor del euro
@st.cache_data
def obtener_valor_euro():
    import requests
    from bs4 import BeautifulSoup
    import re

    url = "https://www.bcentral.cl/inicio"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "lxml")

    #Buscar el div del euro en la pagina
    contenedor = soup.find("div", {"title": "Euro"})
    if not contenedor:
        raise ValueError("No se encontró el contenedor con el valor del euro.")

    #Buscar cualquier texto con $ dentro del contenedor medida desesperada 
    texto = contenedor.get_text()
    match = re.search(r"\$([0-9]+\.[0-9]+|\$[0-9]+,[0-9]+|\$[0-9]+)", texto.replace(".", "").replace(",", "."))

    if not match:
        raise ValueError("No se pudo extraer el valor numérico del euro.")

    valor_str = match.group(1).replace(",", ".")
    return float(valor_str)