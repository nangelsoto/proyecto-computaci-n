import pandas as pd
import streamlit as st
from PIL import Image

st.title('Control de Temperatura y Humedad Huerta Urbana')

# Cargar los archivos CSV
uploaded_temp_file = st.file_uploader('Selecciona un archivo de temperatura (CSV)', type=['csv'])
uploaded_hum_file = st.file_uploader('Selecciona un archivo de humedad (CSV)', type=['csv'])

if uploaded_temp_file is not None and uploaded_hum_file is not None:
    # Leer los archivos CSV
    df_temp = pd.read_csv(uploaded_temp_file, parse_dates=['Time'], index_col='Time')
    df_hum = pd.read_csv(uploaded_hum_file, parse_dates=['Time'], index_col='Time')

    # Convertir la columna de tiempo a formato uniforme
    df_temp.index = df_temp.index.strftime('%Y-%m-%d %H:%M:%S')
    df_hum.index = df_hum.index.strftime('%Y-%m-%d %H:%M:%S')

    # Visualización de temperatura
    st.subheader('Perfil gráfico de la temperatura')
    st.line_chart(df_temp['temperatura ESP32'])

    # Estadísticas básicas de temperatura
    st.subheader('Estadísticos básicos de la temperatura')
    st.dataframe(df_temp['temperatura ESP32'].describe())

    # Visualización de humedad
    st.subheader('Perfil gráfico de la humedad')
    st.line_chart(df_hum['humedad ESP32'])

    # Estadísticas básicas de humedad
    st.subheader('Estadísticos básicos de la humedad')
    st.dataframe(df_hum['humedad ESP32'].describe())

else:
    st.warning('Necesitas cargar ambos archivos CSV (temperatura y humedad).')
