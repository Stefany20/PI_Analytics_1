#importamos librerias
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargamos los datos 
accident_data = pd.read_csv("C:\\Users\\luisr\\proyecto2\\pages\\data3_accidentes_aereos.csv")   

# Obtenemos las cuatro aeronaves mas seguras
safest_aircraft = accident_data.groupby('Tipo de Aeronave')['Total de Fallecidos'].sum().sort_values().index[:4]

# Obtenemos las aeronaves menos seguras 
most_dangerous_aircraft = accident_data.groupby('Tipo de Aeronave')['Total de Fallecidos'].sum().sort_values().index[-4:]

safest_aircraft_data = accident_data[accident_data['Tipo de Aeronave'].isin(safest_aircraft)]

most_dangerous_aircraft_data = accident_data[accident_data['Tipo de Aeronave'].isin(most_dangerous_aircraft)]

# Eliminamos los "Sin Datos" del gráfico de la aeronave menos segura
most_dangerous_aircraft_data = most_dangerous_aircraft_data[most_dangerous_aircraft_data['Tipo de Aeronave'] != 'Sin Datos']

# Creamos una visualización de las aeronaves mas seguras en forma de pastel
plt.figure(figsize=(6, 6))
sns.set_palette('Blues')
safest_aircraft_data['Tipo de Aeronave'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title('Aeronaves más seguras')
plt.ylabel('')
st.pyplot(plt.gcf())

# Creamos una visualización de las aeronaves menos seguras en forma de pastel
plt.figure(figsize=(6, 6))
sns.set_palette('Blues')
most_dangerous_aircraft_data['Tipo de Aeronave'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title('Aeronaves menos seguras')
plt.ylabel('')

#Mostramos la grafica 
st.pyplot(plt.gcf())




