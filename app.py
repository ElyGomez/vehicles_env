import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos del CSV
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header('Análisis de vehículos en venta')

# MODIFICADO: Reemplazo del botón por una casilla de verificación
build_histogram = st.checkbox('Construir histograma')

if build_histogram:
    st.write('Creación de un histograma para el odómetro')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# MODIFICADO: Nueva casilla de verificación para el gráfico de dispersión
build_scatter = st.checkbox('Construir gráfico de dispersión')

if build_scatter:
    st.write('Creación de un gráfico de dispersión: precio vs odómetro')
    fig_scatter = px.scatter(car_data, x='odometer', y='4price')
    st.plotly_chart(fig_scatter, use_container_width=True)
