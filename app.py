import pandas as pd
import streamlit as st
from PIL import Image

st.title('Control de Temperatura y Humedad Huerta Urbana')
image = Image.open('grafana2.jpg')
st.image(image)

uploaded_file = st.file_uploader('Elige un archivo')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader('Perfil gráfico de la variable medida.')
    df = df.set_index('Time')
    st.line_chart(df)

    st.write(df)
    st.subheader('Estadísticos básicos de los sensores.')

    # Filtrar por temperatura
    min_temp = st.slider('Selecciona el valor mínimo del filtro de temperatura', min_value=-10, max_value=45, value=23, key=1)
    filtrado_temp_min = df.query(f"`temperatura ESP32` > {min_temp}")
    st.subheader("Temperaturas superiores al valor configurado.")
    st.write('Dataframe Filtrado (Temperatura)')
    st.write(filtrado_temp_min)

    max_temp = st.slider('Selecciona el valor máximo del filtro de temperatura', min_value=-10, max_value=45, value=23, key=2)
    filtrado_temp_max = df.query(f"`temperatura ESP32` < {max_temp}")
    st.subheader("Temperaturas inferiores al valor configurado.")
    st.write('Dataframe Filtrado (Temperatura)')
    st.write(filtrado_temp_max)

    # Filtrar por humedad
    min_hum = st.slider('Selecciona el valor mínimo del filtro de humedad', min_value=0, max_value=100, value=50, key=3)
    filtrado_hum_min = df.query(f"`humedad ESP32` > {min_hum}")
    st.subheader("Humedades superiores al valor configurado.")
    st.write('Dataframe Filtrado (Humedad)')
    st.write(filtrado_hum_min)

    max_hum = st.slider('Selecciona el valor máximo del filtro de humedad', min_value=0, max_value=100, value=50, key=4)
    filtrado_hum_max = df.query(f"`humedad ESP32` < {max_hum}")
    st.subheader("Humedades inferiores al valor configurado.")
    st.write('Dataframe Filtrado (Humedad)')
    st.write(filtrado_hum_max)

else:
    st.warning('Necesitas cargar un archivo CSV de Excel.')
