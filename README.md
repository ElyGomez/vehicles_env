# vehicles_env
Proyecto Sprint 7, herramientas de desarrollo 

## Ejecutar app de Render
https://vehicles-env-9ena.onrender.com


# Análisis de Vehículos en Venta con Streamlit

Este proyecto es una aplicación web interactiva construida con **Streamlit**, que permite explorar un conjunto de datos de vehículos usando gráficos dinámicos.

## Estructura del Proyecto
mi_proyectvehicles_env/
├── app.py # Aplicación principal de Streamlit
├── vehicles_us.csv # Conjunto de datos de vehículos
├── requirements.txt # Lista de dependencias para desplegar la app
├── README.md # Este archivo
├── gitignore # archivo para indicar que no rastrear o subir al repositorio
└── notebooks # Carpeta cor archivo .ipynb (solo practica no requerido para la app)


## Funcionalidades de la App

- Visualización de los datos en tabla.
- Histograma del odómetro de los vehículos.
- Diagrama de dispersión: precio vs odómetro.
- Gráfico de barras de cantidad de vehículos por marca.
- Filtros dinámicos por tipo y condición de vehículo.
- Comparación de precios entre fabricantes.

## Cómo Ejecutar la App Localmente

1. Clona el repositorio:

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio

streamlit run app.py
