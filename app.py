import pandas as pd
import streamlit as st
from PIL import Image

st.title('Control de Temperatura y Humedad Huerta Urbana')
image = Image.open('grafana2.jpg')
st.image(image)
columnas = ["temperatura ESP32", "humedad ESP32"]

uploaded_file = st.file_uploader('Choose a file')

if uploaded_file is not None:
    df1 = pd.read_csv(uploaded_file)

    st.subheader('Perfil gráfico de la variable medida.')
    df1 = df1.set_index('Time')
    st.line_chart(df1)

    st.write(df1)
    st.subheader('Estadísticos básicos de los sensores.')

    if columnas == "temperatura ESP32":
        # Convertir esto en variable
        st.dataframe(df1["temperatura ESP32"].describe())

        min_temp = st.slider('Selecciona valor mínimo del filtro', min_value=-10, max_value=45, value=23, key=1)
        # Filtrar el DataFrame utilizando query
        filtrado_df_min = df1.query(f"`temperatura ESP32` > {min_temp}")
        # Mostrar el DataFrame filtrado
        st.subheader("Temperaturas superiores al valor configurado.")
        st.write('Dataframe Filtrado')
        st.write(filtrado_df_min)

        max_temp = st.slider('Selecciona valor máximo del filtro', min_value=-10, max_value=45, value=23, key=2)
        # Filtrar el DataFrame utilizando query
        filtrado_df_max = df1.query(f"`temperatura ESP32` < {max_temp}")
        # Mostrar el DataFrame filtrado
        st.subheader("Temperaturas Inferiores al valor configurado.")
        st.write('Dataframe Filtrado')
        st.write(filtrado_df_max)

    elif columnas == "humedad ESP32":
        st.dataframe(df1["humedad ESP32"].describe())

        min_hum = st.slider('Selecciona valor mínimo del filtro', min_value=-10, max_value=45, value=23, key=1)
        # Filtrar el DataFrame utilizando query
        filtrado_df_min = df1.query(f"`humedad ESP32` > {min_hum}")
        # Mostrar el DataFrame filtrado
        st.subheader("Humedades superiores al valor configurado.")
        st.write('Dataframe Filtrado')
        st.write(filtrado_df_min)

        max_hum = st.slider('Selecciona valor máximo del filtro', min_value=-10, max_value=45, value=23, key=2)
        # Filtrar el DataFrame utilizando query
        filtrado_df_max = df1.query(f"`humedad ESP32` < {max_hum}")
        # Mostrar el DataFrame filtrado
        st.subheader("Humedades Inferiores al valor configurado.")
        st.write('Dataframe Filtrado')
        st.write(filtrado_df_max)

else:
    st.warning('Necesitas cargar un archivo CSV de Excel.')
