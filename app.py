import pandas as pd
import streamlit as st
from PIL import Image

st.title('Control de Temperatura y Humedad Huerta Urbana')
image = Image.open('grafana2.jpg')
st.image(image)

uploaded_file = st.file_uploader('Elige un archivo')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Verificar qué tipo de archivo se ha cargado
    if 'temperatura ESP32' in df.columns:
        sensor_type = 'temperatura ESP32'
    elif 'humedad ESP32' in df.columns:
        sensor_type = 'humedad ESP32'
    else:
        st.error('El archivo cargado no tiene las columnas esperadas.')
        st.stop()

    st.subheader(f'Perfil gráfico de {sensor_type}.')
    df = df.set_index('Time')
    st.line_chart(df)

    st.write(df)
    st.subheader('Estadísticos básicos de los sensores.')
    st.dataframe(df[sensor_type].describe())

    min_value = st.slider('Selecciona valor mínimo del filtro', min_value=df[sensor_type].min(), max_value=df[sensor_type].max(), value=df[sensor_type].min())
    max_value = st.slider('Selecciona valor máximo del filtro', min_value=df[sensor_type].min(), max_value=df[sensor_type].max(), value=df[sensor_type].max())

    # Filtrar el DataFrame utilizando query
    filtrado_df_min = df.query(f"`{sensor_type}` > {min_value}")
    filtrado_df_max = df.query(f"`{sensor_type}` < {max_value}")

    # Mostrar el DataFrame filtrado
    st.subheader(f'{sensor_type} superiores al valor configurado.')
    st.write('Dataframe Filtrado')
    st.write(filtrado_df_min)

    st.subheader(f'{sensor_type} inferiores al valor configurado.')
    st.write('Dataframe Filtrado')
    st.write(filtrado_df_max)

else:
    st.warning('Necesitas cargar un archivo CSV.')
