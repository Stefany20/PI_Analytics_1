#Importamos las librerias
import streamlit as st
import pandas as pd 
import plotly.express as px

#importamos la data que usaremos 
data = pd.read_csv("C:\\Users\\luisr\\PI°2\\pages\\Tasa_de_Mortalidad.csv")



# Calculamos la tasa de mortalidad para cada accidente
data['Tasa de Mortalidad'] = data['Total de Fallecidos'] / data['Total A Bordo']

# Agrupar los datos por año y calcular la tasa de mortalidad promedio
tasa_mortalidad = data.groupby('Año')['Tasa de Mortalidad'].mean().reset_index()

paleta_colores = px.colors.sequential.Blues

# Crear figura de barras horizontales
fig = px.bar(tasa_mortalidad, x='Tasa de Mortalidad', y='Año', orientation='h',
             title='Tasa de Mortalidad Promedio por Año', color='Tasa de Mortalidad',
             template="plotly_white", color_continuous_scale=paleta_colores)

# Mostrarmos la grafica
st.plotly_chart(fig)


##########################


# Crearmos un selector de años
selected_years = st.multiselect('Selecciona dos años:', options=data['Año'].unique(), default=[data['Año'].unique()[0], data['Año'].unique()[1]])

# Filtrar los datos para los años seleccionados
filtered_df = data[data['Año'].isin(selected_years)]

# Funcion para calcular la diferencia porcentual entre dos valores
def calcular_diferencia_porcentual(valor_anterior, valor_actual):
    if valor_anterior == 0:
        return 0
    return ((valor_actual - valor_anterior) / valor_anterior) * 100


filtered_df = filtered_df.sort_values('Año')  # Ordenam,os por año para asegurar el calculo correcto
filtered_df['Diferencia Porcentual'] = filtered_df['Tasa de Mortalidad'].diff().shift(-1)
filtered_df['Diferencia Porcentual'] = filtered_df.apply(lambda row: calcular_diferencia_porcentual(row['Tasa de Mortalidad'], row['Diferencia Porcentual']), axis=1)

diferencia_porcentual = filtered_df['Diferencia Porcentual'].values[-2]  # Usar el penultimo valor

# Generamos grafico interactivo 
fig = px.scatter(filtered_df, x='Año', y='Tasa de Mortalidad', color='Diferencia Porcentual',
                 hover_data=['Tasa de Mortalidad', 'Diferencia Porcentual'], trendline="ols",
                 color_continuous_scale='Blues')


titulo_linea_tendencia = f'Tasa de mortalidad por año.'
fig.update_layout(title=titulo_linea_tendencia,
                  xaxis_title='Año',
                  yaxis_title='Tasa de Mortalidad')

# Mostramos el grafico
st.plotly_chart(fig)




