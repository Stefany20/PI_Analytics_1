#Importamos las librerias
import streamlit as st
import pandas as pd
import plotly.graph_objects as go


# Cargamos los datos
data = pd.read_csv("C:\\Users\\luisr\\proyecto2\\pages\\data3_accidentes_aereos.csv") 

# Calculamos la cantidad total de accidentes por pais
accidentes_por_pais = data['Pais del accidente'].value_counts().reset_index()
accidentes_por_pais.columns = ['Pais', 'Accidentes']

#Grafica

fig = go.Figure(data=go.Choropleth(
    locations=accidentes_por_pais['Pais'],
    z=accidentes_por_pais['Accidentes'],
    locationmode='country names',
    colorscale='Blues',  # Escala de colores azules
    reversescale=True,  # Invertimos la escala de colores para destacar los valores más altos
    colorbar_title='Cantidad de Accidentes'
))

fig.update_layout(
    title='Países con más Accidentes Aéreos',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='natural earth'  
    )
)

# Añadimos un estilo adicional al mapa
fig.update_traces(marker_line_color='white',  # Color de linea blanco para los marcadores de los paises
                  marker_line_width=0.5)  # Grosor de linea de los marcadores

fig.update_layout(
    title_font_size=24,  # Tamaño de fuente del titulo
    font_family='Arial',  # Tipo de fuente
    plot_bgcolor='rgba(0,0,0,0)',  # Fondo transparente
    paper_bgcolor='rgba(0,0,0,0)',  # Fondo del gráfico transparente
)

# Mostramos el grafico
st.plotly_chart(fig)




