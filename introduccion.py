#importamos las librerias
import streamlit as st
from PIL import Image
import urllib.request


#Colocamos el logo de OACI  
image_url = "https://derechoaeronauticoiuac.files.wordpress.com/2013/02/tcbtweet2c2a11.png"
image_path = "oaci_logo.png"
urllib.request.urlretrieve(image_url, image_path)

image = Image.open(image_path)
st.image(image, caption="Organización de Aviación Civil Internacional (OACI)")

#Titulo y descripcion 
st.title("Análisis de Accidentes de Aviones")
st.subheader("Introducción")


st.write("Bienvenidoal análisis de accidentes de aviones. En este trabajo, exploraremos datos relacionados con accidentes aéreos para obtener información valiosa sobre la seguridad en la industria de la aviación.")

st.write("Los accidentes de aviones son eventos trágicos que pueden tener un impacto significativo en la seguridad y la confianza de los viajes aéreos. Comprender los factores que contribuyen a estos accidentes y analizar sus consecuencias es fundamental para mejorar la seguridad en la industria.")

st.write("En este análisis, utilizaremos datos recopilados sobre accidentes de aviones para examinar diferentes aspectos, como el total de víctimas, la tasa de mortalidad, los países con más accidentes y las aeronaves más seguras e inseguras. A través de visualizaciones y estadísticas, obtendremos una visión más completa de la situación y las tendencias en la seguridad de la aviación.")




