import pandas as pd
import streamlit as st
from PIL import Image

st.title('Control de Temperatura y Humedad Huerta Urbana')
image = Image.open('grafana2.jpg')
st.image(image)

uploaded_file_temp = st.file_uploader('Elige un archivo de temperatura', key='temp')
uploaded_file_hum = st.file_uploader('Elige un archivo de humedad', key='hum')

def process_file(uploaded_file, variable, variable_name):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        # Verificar que las columnas esperadas existan
        if 'Time' not in df.columns or variable not in df.columns:
            st.error(f"El archivo debe contener las columnas 'Time' y '{variable}'")
            return
        
        st.subheader(f'Perfil gráfico de la variable medida: {variable_name}.')
        df = df.set_index('Time')
        st.line_chart(df)
        st.write(df)
        st.subheader(f'Estadísticos básicos del sensor: {variable_name}.')
        st.dataframe(df[variable].describe())

        min_val = st.slider(f'Selecciona valor mínimo del filtro para {variable_name}', min_value=-10, max_value=100, value=23, key=f'min_{variable}')
        filtrado_df_min = df.query(f"`{variable}` > {min_val}")
        st.subheader(f"{variable_name.capitalize()} superiores al valor configurado.")
        st.write('Dataframe Filtrado')
        st.write(filtrado_df_min)

        max_val = st.slider(f'Selecciona valor máximo del filtro para {variable_name}', min_value=-10, max_value=100, value=23, key=f'max_{variable}')
        filtrado_df_max = df.query(f"`{variable}` < {max_val}")
        st.subheader(f"{variable_name.capitalize()} inferiores al valor configurado.")
        st.write('Dataframe Filtrado')
        st.write(filtrado_df_max)
    else:
        st.warning(f'Necesitas cargar un archivo de {variable_name}.')

if uploaded_file_temp:
    process_file(uploaded_file_temp, 'temperatura ESP32', 'temperatura')

if uploaded_file_hum:
    process_file(uploaded_file_hum, 'humedad ESP32', 'humedad')
