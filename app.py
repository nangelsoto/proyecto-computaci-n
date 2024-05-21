import pandas as pd
import streamlit as st
from PIL import Image

st.title('Control de Temperatura y Humedad Huerta Urbana')
image = Image.open('grafana2.jpg')
st.image(image)

uploaded_file = st.file_uploader('Choose a file')

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file, sheet_name=None)

    # Filtrar las hojas de datos de temperatura y humedad si existen
    df_temperatura = None
    df_humedad = None
    for sheet_name, sheet_df in df.items():
        if 'temperatura ESP32' in sheet_df.columns:
            df_temperatura = sheet_df.set_index('Time')
        elif 'humedad ESP32' in sheet_df.columns:
            df_humedad = sheet_df.set_index('Time')

    if df_temperatura is not None:
        st.subheader('Perfil gráfico de la variable medida (Temperatura).')
        st.line_chart(df_temperatura)
        
        st.subheader('Estadísticos básicos de los sensores de Temperatura.')
        st.dataframe(df_temperatura["temperatura ESP32"].describe())
        
        min_temp = st.slider('Selecciona valor mínimo del filtro de Temperatura', min_value=-10, max_value=45, value=23, key='temp_min')
        filtrado_df_min_temp = df_temperatura.query(f"`temperatura ESP32` > {min_temp}")
        st.subheader("Temperaturas superiores al valor configurado.")
        st.write(filtrado_df_min_temp)
        
        max_temp = st.slider('Selecciona valor máximo del filtro de Temperatura', min_value=-10, max_value=45, value=23, key='temp_max')
        filtrado_df_max_temp = filtrado_df_min_temp.query(f"`temperatura ESP32` < {max_temp}")
        st.subheader("Temperaturas inferiores al valor configurado.")
        st.write(filtrado_df_max_temp)
        
    if df_humedad is not None:
        st.subheader('Perfil gráfico de la variable medida (Humedad).')
        st.line_chart(df_humedad)
        
        st.subheader('Estadísticos básicos de los sensores de Humedad.')
        st.dataframe(df_humedad["humedad ESP32"].describe())
        
        min_hum = st.slider('Selecciona valor mínimo del filtro de Humedad', min_value=0, max_value=100, value=50, key='hum_min')
        filtrado_df_min_hum = df_humedad.query(f"`humedad ESP32` > {min_hum}")
        st.subheader("Humedades superiores al valor configurado.")
        st.write(filtrado_df_min_hum)
        
        max_hum = st.slider('Selecciona valor máximo del filtro de Humedad', min_value=0, max_value=100, value=50, key='hum_max')
        filtrado_df_max_hum = filtrado_df_min_hum.query(f"`humedad ESP32` < {max_hum}")
        st.subheader("Humedades inferiores al valor configurado.")
        st.write(filtrado_df_max_hum)
        
else:
    st.warning('Necesitas cargar un archivo excel.')

