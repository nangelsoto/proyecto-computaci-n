import pandas as pd
import streamlit as st
from PIL import Image

st.title('Control de Temperatura y Humedad Huerta Urbana')
image = Image.open('grafana2.jpg')
st.image(image)

uploaded_file = st.file_uploader('Choose a file')

if uploaded_file is not None:
    # Leer el archivo CSV en un DataFrame de Pandas
    df = pd.read_csv(uploaded_file)

    # Verificar si hay una columna llamada "temperatura ESP32" y "humedad ESP32"
    has_temperature = "temperatura ESP32" in df.columns
    has_humidity = "humedad ESP32" in df.columns

    if has_temperature or has_humidity:
        st.subheader('Perfil gráfico de la variable medida.')
        df = df.set_index('Time')
        st.line_chart(df)

        st.write(df)
        st.subheader('Estadísticos básicos de los sensores.')

        if has_temperature:
            # Filtrar temperatura
            min_temp = st.slider('Selecciona valor mínimo del filtro de temperatura', min_value=-10, max_value=45, value=23, key=1)
            max_temp = st.slider('Selecciona valor máximo del filtro de temperatura', min_value=-10, max_value=45, value=23, key=2)

            filtrado_df_temp = df.query(f"`temperatura ESP32` > {min_temp} and `temperatura ESP32` < {max_temp}")
            st.subheader("Temperaturas dentro del rango configurado.")
            st.write('Dataframe Filtrado')
            st.write(filtrado_df_temp.describe())

        if has_humidity:
            # Filtrar humedad
            min_humidity = st.slider('Selecciona valor mínimo del filtro de humedad', min_value=0, max_value=100, value=50, key=3)
            max_humidity = st.slider('Selecciona valor máximo del filtro de humedad', min_value=0, max_value=100, value=50, key=4)

            filtrado_df_humidity = df.query(f"`humedad ESP32` > {min_humidity} and `humedad ESP32` < {max_humidity}")
            st.subheader("Humedades dentro del rango configurado.")
            st.write('Dataframe Filtrado')
            st.write(filtrado_df_humidity.describe())

    else:
        st.warning('El archivo no contiene datos de temperatura ni de humedad.')

else:
    st.warning('Necesitas cargar un archivo csv excel.')
