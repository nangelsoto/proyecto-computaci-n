import pandas as pd
import streamlit as st
from PIL import Image

st.title('Control de Temperatura y Humedad Huerta Urbana')
image = Image.open('grafana2.jpg')
st.image(image)

st.header("Cargar archivos CSV")
uploaded_file_temp = st.file_uploader('Elige un archivo de temperatura', type=['csv'])
uploaded_file_hum = st.file_uploader('Elige un archivo de humedad', type=['csv'])

def process_file(file, column_name):
    df = pd.read_csv(file)
    df = df.set_index('Time')
    return df[[column_name]]

# Procesar archivo de temperatura
if uploaded_file_temp is not None:
    df_temp = process_file(uploaded_file_temp, "temperatura ESP32")

    st.subheader('Perfil gráfico de la temperatura.')
    st.line_chart(df_temp)
    
    st.write(df_temp)
    st.subheader('Estadísticos básicos del sensor de temperatura.')
    st.dataframe(df_temp["temperatura ESP32"].describe())
    
    min_temp = st.slider('Selecciona valor mínimo del filtro de temperatura', min_value=-10, max_value=45, value=23, key='min_temp')
    filtrado_temp_min = df_temp.query(f"`temperatura ESP32` > {min_temp}")
    st.subheader("Temperaturas superiores al valor configurado.")
    st.write('Dataframe Filtrado')
    st.write(filtrado_temp_min)
    
    max_temp = st.slider('Selecciona valor máximo del filtro de temperatura', min_value=-10, max_value=45, value=23, key='max_temp')
    filtrado_temp_max = df_temp.query(f"`temperatura ESP32` < {max_temp}")
    st.subheader("Temperaturas inferiores al valor configurado.")
    st.write('Dataframe Filtrado')
    st.write(filtrado_temp_max)
else:
    st.warning('Necesitas cargar un archivo csv de temperatura.')

# Procesar archivo de humedad
if uploaded_file_hum is not None:
    df_hum = process_file(uploaded_file_hum, "humedad ESP32")

    st.subheader('Perfil gráfico de la humedad.')
    st.line_chart(df_hum)
    
    st.write(df_hum)
    st.subheader('Estadísticos básicos del sensor de humedad.')
    st.dataframe(df_hum["humedad ESP32"].describe())
    
    min_hum = st.slider('Selecciona valor mínimo del filtro de humedad', min_value=0, max_value=100, value=50, key='min_hum')
    filtrado_hum_min = df_hum.query(f"`humedad ESP32` > {min_hum}")
    st.subheader("Humedades superiores al valor configurado.")
    st.write('Dataframe Filtrado')
    st.write(filtrado_hum_min)
    
    max_hum = st.slider('Selecciona valor máximo del filtro de humedad', min_value=0, max_value=100, value=50, key='max_hum')
    filtrado_hum_max = df_hum.query(f"`humedad ESP32` < {max_hum}")
    st.subheader("Humedades inferiores al valor configurado.")
    st.write('Dataframe Filtrado')
    st.write(filtrado_hum_max)
else:
    st.warning('Necesitas cargar un archivo csv de humedad.')
