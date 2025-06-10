import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos del CSV
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header('Análisis de Vehículos en Venta')

# =============================
# Sección 1: Visualización de la base de datos
# =============================
st.subheader('Vista previa del conjunto de datos')
st.write('A continuación se muestra una tabla con los primeros registros del dataset:')
st.dataframe(car_data)

# =============================
# Sección 2: Gráfica interactiva de barras por tipo
# =============================
st.subheader('Conteo de vehículos por tipo (filtrado)')

types = car_data['type'].dropna().unique()
selected_types = st.multiselect(
    'Selecciona tipo(s) de vehículo', types, default=types)

filtered_data = car_data[car_data['type'].isin(selected_types)]

# Contar ocurrencias de cada tipo
type_counts = filtered_data['type'].value_counts().reset_index()
type_counts.columns = ['Tipo de vehículo', 'Cantidad']

fig_bar = px.bar(type_counts,
                 x='Tipo de vehículo', y='Cantidad',
                 title='Cantidad de Vehículos por Tipo')
st.plotly_chart(fig_bar, use_container_width=True)

# =============================
# Sección 3: Histograma de condition vs model
# =============================
st.subheader('Distribución de modelos por condición del vehículo')

conditions = car_data['condition'].dropna().unique()
selected_conditions = st.multiselect(
    'Selecciona condición(es)', conditions, default=conditions)

condition_data = car_data[car_data['condition'].isin(selected_conditions)]

fig_hist_condition = px.histogram(condition_data, x='model', color='condition',
                                  title='Distribución de Modelos por Condición')
st.plotly_chart(fig_hist_condition, use_container_width=True)

# =============================
# Sección 4: Comparación de distribución de precios por tipo, extra: cambio de boton por selectbox
# =============================
st.subheader('Comparación de distribución de precios entre tipos de vehículo')

types_for_price = car_data['type'].dropna().unique()

col1, col2 = st.columns(2)
with col1:
    type_1 = st.selectbox('Tipo 1', types_for_price)
with col2:
    type_2 = st.selectbox('Tipo 2', types_for_price, index=1)

compare_button = st.button('Comparar Distribuciones')

if compare_button:
    data_1 = car_data[car_data['type'] == type_1]
    data_2 = car_data[car_data['type'] == type_2]

    combined = pd.concat([
        data_1.assign(source=type_1),
        data_2.assign(source=type_2)
    ])

    fig_compare = px.histogram(combined, x='4price', color='source', barmode='overlay',
                               title='Distribución de Precios entre dos Tipos de Vehículo')
    st.plotly_chart(fig_compare, use_container_width=True)

# =============================
# Sección 5: Construcioón de histograma y gráfica dispersión
# =============================
st.subheader('Construcción de histogramas y gráficos de dispersión')

# Reemplazo del botón por una casilla de verificación
build_histogram = st.checkbox('Construir histograma de las millas recorridas')
if build_histogram:
    st.write('Creación de un histograma para las millas recorridas (odómetro)')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# MODIFICADO: Nueva casilla de verificación para el gráfico de dispersión
build_scatter = st.checkbox(
    'Construir gráfico de dispersión precio vs millas recorridas')

if build_scatter:
    st.write(
        'Creación de un gráfico de dispersión: precio vs millas recorridas (odómetro)')
    fig_scatter = px.scatter(car_data, x='odometer', y='4price')
    st.plotly_chart(fig_scatter, use_container_width=True)
