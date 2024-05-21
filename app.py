import pandas as pd
import streamlit as st
from PIL import Image

st.title('Control de Temperatura y Humedad Huerta Urbana')
image = Image.open('grafana2.jpg')
st.image(image)

uploaded_file_temp = st.file_uploader('Elige un archivo de temperatura', key='temp')
uploaded_file_hum = st.file_uploader('Elige un archivo de humedad', key='hum')

def process_file(uploaded_file, variable):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.subheader(f'Perfil gráfico de la variable medida: {variable}.')
        df = df.set_index('Time')
        st.line_chart(df)
        st.write(df)
        st.subheader(f'Estadísticos básicos del sensor: {variable}.')
        st.dataframe(df[variable].describe())

        min_val = st.slider(f'Selecciona valor mínimo del filtro para {variable}', min_value=-10, max_value=100, value=23, key=f'min_{variable}')
        filtrado_df_min = df.query(f"`{variable}` > {min_val}")
        st.subheader(f"{variable.capitalize()} superiores al valor configurado.")
        st.write('Dataframe Filtrado')
        st.write(filtrado_df_min)

        max_val = st.slider(f'Selecciona valor máximo del filtro para {variable}', min_value=-10, max_value=100, value=23, key=f'max_{variable}')
        filtrado_df_max = df.query(f"`{variable}` < {max_val}")
        st.subheader(f"{variable.capitalize()} inferiores al valor configurado.")
        st.write('Dataframe Filtrado')
        st.write(filtrado_df_max)
    else:
        st.warning(f'Necesitas cargar un archivo de {variable}.')

if uploaded_file_temp:
    process_file(uploaded_file_temp, 'temperatura ESP32')

if uploaded_file_hum:
    process_file(uploaded_file_hum, 'humedad ESP32')
