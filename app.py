import pandas as pd
import plotly.express as px
import streamlit as st

# Encabezado
st.header("Cuadro de mandos de análisis de anuncios de coches usados")

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Botón para histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión: precio vs kilometraje')
    fig2 = px.scatter(car_data, x="odometer", y="4price",
                      title="Precio vs Kilometraje")
    st.plotly_chart(fig2, use_container_width=True)
