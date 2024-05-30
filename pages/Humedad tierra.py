import pandas as pd
import streamlit as st
from PIL import Image

# Título de la aplicación
st.title('Humedad de la Tierra)
image = Image.open('tierra.jpeg')
st.image(image)

# Cargador de archivos
uploaded_file = st.file_uploader('Choose a file')

if uploaded_file is not None:
    df1 = pd.read_csv(uploaded_file)

    # Subtítulo y gráfico de línea
    st.subheader('Humedad y Tiempo.')
    df1 = df1.set_index('Time')
    st.line_chart(df1)

    st.write(df1)
    st.subheader('Estadísticos básicos de los sensores.')
    st.dataframe(df1["humedadtierra ESP32"].describe())

    # Slider para el valor mínimo del filtro
    min_humti = st.slider('Selecciona valor mínimo del filtro ', min_value=-10, max_value=45, value=23, key=1)
    # Filtrar el DataFrame utilizando query
    filtrado_df_min = df1.query(f"`humedadtierra ESP32` > {min_humti}")
    # Alerta si el valor máximo es 45
    if min_humti == -10:
        st.write('<p style="color:red; font-size: 20px;">Alerta: valor mínimo seleccionado!</p>', unsafe_allow_html=True)
        # Ruta al archivo de audio
        audio_file = open('alarma.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')
    # Mostrar el DataFrame filtrado
    st.subheader("Humedades superiores al valor configurado.")
    st.write('Dataframe Filtrado')
    st.write(filtrado_df_min)

    # Slider para el valor máximo del filtro
    max_humti = st.slider('Selecciona valor máximo del filtro ', min_value=-10, max_value=45, value=23, key=2)
    # Filtrar el DataFrame utilizando query
    filtrado_df_max = df1.query(f"`humedadtierra ESP32` < {max_humti}")
        # Alerta si el valor máximo es 45
    if max_humti == 45:
        st.write('<p style="color:red; font-size: 20px;">Alerta: valor máximo seleccionado!</p>', unsafe_allow_html=True)
        # Ruta al archivo de audio
        audio_file = open('alerta.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')
    # Mostrar el DataFrame filtrado
    st.subheader("Humedades Inferiores al valor configurado.")
    st.write('Dataframe Filtrado')
    st.write(filtrado_df_max)





else:
    st.warning('Necesitas cargar un archivo csv excel.')
