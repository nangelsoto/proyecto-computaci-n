import pandas as pd
import streamlit as st

# Título de la aplicación
st.title('Control de Temperatura y Humedad Huerta Urbana')

# Cargar imagen
image = Image.open('grafana2.jpg')
st.image(image)

# Función para cargar archivos
uploaded_file = st.file_uploader('Choose a file')

# Verificar si se ha cargado un archivo
if uploaded_file is not None:
    # Leer el archivo CSV
    df = pd.read_csv(uploaded_file)

    # Mostrar gráfico de línea para ambas variables
    st.subheader('Perfil gráfico de la variable medida.')
    st.line_chart(df.set_index('Time'))

    # Mostrar DataFrame
    st.write(df)

    # Estadísticas básicas para temperatura ESP32
    st.subheader('Estadísticos básicos para Temperatura ESP32.')
    st.dataframe(df["temperatura ESP32"].describe())

    # Filtrar datos para temperatura ESP32
    min_temp = st.slider('Selecciona el valor mínimo del filtro para Temperatura ESP32', min_value=df["temperatura ESP32"].min(), max_value=df["temperatura ESP32"].max(), value=df["temperatura ESP32"].min())
    max_temp = st.slider('Selecciona el valor máximo del filtro para Temperatura ESP32', min_value=df["temperatura ESP32"].min(), max_value=df["temperatura ESP32"].max(), value=df["temperatura ESP32"].max())

    filtrado_temp_df = df[(df["temperatura ESP32"] >= min_temp) & (df["temperatura ESP32"] <= max_temp)]
    st.subheader('Temperaturas filtradas:')
    st.write(filtrado_temp_df)

    # Estadísticas básicas para humedad ESP32
    st.subheader('Estadísticos básicos para Humedad ESP32.')
    st.dataframe(df["humedad ESP32"].describe())

    # Filtrar datos para humedad ESP32
    min_humedad = st.slider('Selecciona el valor mínimo del filtro para Humedad ESP32', min_value=df["humedad ESP32"].min(), max_value=df["humedad ESP32"].max(), value=df["humedad ESP32"].min())
    max_humedad = st.slider('Selecciona el valor máximo del filtro para Humedad ESP32', min_value=df["humedad ESP32"].min(), max_value=df["humedad ESP32"].max(), value=df["humedad ESP32"].max())

    filtrado_humedad_df = df[(df["humedad ESP32"] >= min_humedad) & (df["humedad ESP32"] <= max_humedad)]
    st.subheader('Humedades filtradas:')
    st.write(filtrado_humedad_df)

else:
    st.warning('Necesitas cargar un archivo CSV.')
