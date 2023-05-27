#importamos librerias
import streamlit as st
import pandas as pd 
import plotly.graph_objects as go
import plotly.express as px



# Cargamos la data
data = pd.read_csv("C:\\Users\\luisr\\proyecto2\\pages\\Tota_victimas_por_ano.csv")

# grafico interactivo de victimas por año
total_victimas = data.groupby('Año')[['Total de Fallecidos', 'Numero de personas con lesiones menores', 'Personas Fallecidas en Tierra']].sum()


total_victimas['Total Víctimas'] = total_victimas['Total de Fallecidos'] + total_victimas['Numero de personas con lesiones menores'] + total_victimas["Personas Fallecidas en Tierra"]

fig = go.Figure()
fig.add_trace(go.Scatter(x=total_victimas.index, y=total_victimas['Total de Fallecidos'], name='Fallecidos',
                         line=dict(color='#2196F3', width=3)))
fig.add_trace(go.Scatter(x=total_victimas.index, y=total_victimas['Numero de personas con lesiones menores'], name='Heridos leves',
                         line=dict(color='#1976D2', width=3)))
fig.add_trace(go.Scatter(x=total_victimas.index, y=total_victimas['Personas Fallecidas en Tierra'], name='Fallecidos en tierra',
                         line=dict(color='#1565C0', width=3)))
fig.update_layout(title='Total de Víctimas por Año',
                  xaxis_title='Años (1980-2022)',
                  yaxis_title='Número de Víctimas')

fig.update_layout(
    title=dict(text='Total de Víctimas por Año', x=0.5),  # Centrar el título
    xaxis_title='Años (1980-2022)',
    yaxis_title='Número de Víctimas',
    title_font=dict(size=24),  # Aumentar el tamaño del título
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(size=14, color='white'),
    legend_title_font=dict(color='white', size=14),
    xaxis=dict(tickfont=dict(size=12), title_font=dict(color='white', size=14)),
    yaxis=dict(tickfont=dict(size=12), title_font=dict(color='white', size=14)),
)


fig.update_xaxes(tickvals=total_victimas.index[::2])
fig.update_yaxes(tickfont=dict(size=12))


fig.update_layout(yaxis_range=[-100, 3000])

#Mostramos el grafico 
st.plotly_chart(fig)

########################################
 #Total de victimas
# Agregarmos columnas para la cantidad total de víctimas
data["Total_Victimas"] = data["Total de Fallecidos"] + data["Numero de personas con lesiones menores"] + data["Personas Fallecidas en Tierra"]

tipo_victima = st.selectbox("Seleccione el tipo de víctima", 
                            options=["Total de Fallecidos", "Personas Fallecidas en Tierra", "Numero de personas con lesiones menores"])

filtered_data = data[["Año", tipo_victima]]

#agregamos los colores que quiero para cada grafica 
colors = {'Total de Fallecidos': '#2196F3', 
          'Numero de personas con lesiones menores': '#1976D2', 
          'Personas Fallecidas en Tierra': '#1565C0'}

fig_tipo_victima = px.bar(filtered_data,
            x=tipo_victima,
            y='Año',
            orientation='h',
            color_discrete_sequence=['#2196F3','#1976D2','#1565C0']
        )

fig_tipo_victima.update_layout(
    title="Cantidad de víctimas por tipo",
    xaxis_title="Cantidad",
    yaxis_title="Año",
    plot_bgcolor="rgba(0,0,0,0)",
)
#Mostramos la grafica
st.plotly_chart(fig_tipo_victima)

