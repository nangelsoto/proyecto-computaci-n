import pandas as pd
import streamlit as st
from PIL import Image


st.title('Control de Temperatura y Humedad Huerta Urbana')
image = Image.open('grafana2.jpg')
st.image(image)

uploaded_file = st.file_uploader('Choose a file')

import streamlit as st
import pandas as pd

# Función para cargar el archivo CSV y mostrar las estadísticas descriptivas
def mostrar_estadisticas_descriptivas(df, columna):
    st.write(df[columna].describe())

    # Filtrar el DataFrame utilizando un slider para seleccionar el valor mínimo
    min_valor = st.slider(f'Selecciona valor mínimo del filtro para {columna}', min_value=df[columna].min(), max_value=df[columna].max(), value=df[columna].min(), key=1)
    filtrado_df_min = df.query(f"`{columna}` > {min_valor}")

    # Mostrar el DataFrame filtrado para valores superiores al valor configurado
    st.subheader(f"{columna.capitalize()} superiores al valor configurado.")
    st.write('Dataframe Filtrado')
    st.write(filtrado_df_min)

    # Filtrar el DataFrame utilizando un slider para seleccionar el valor máximo
    max_valor = st.slider(f'Selecciona valor máximo del filtro para {columna}', min_value=df[columna].min(), max_value=df[columna].max(), value=df[columna].max(), key=2)
    filtrado_df_max = df.query(f"`{columna}` < {max_valor}")

    # Mostrar el DataFrame filtrado para valores inferiores al valor configurado
    st.subheader(f"{columna.capitalize()} inferiores al valor configurado.")
    st.write('Dataframe Filtrado')
    st.write(filtrado_df_max)

# Cargar el archivo CSV
uploaded_file = st.file_uploader("Cargar archivo CSV", type=["csv"])

if uploaded_file is not None:
    # Leer el archivo CSV
    df = pd.read_csv(uploaded_file)

    # Determinar si el archivo contiene datos de temperatura o de humedad
    columnas = df.columns
    if "temperatura ESP32" in columnas:
        mostrar_estadisticas_descriptivas(df, "temperatura ESP32")
    elif "humedad ESP32" in columnas:
        mostrar_estadisticas_descriptivas(df, "humedad ESP32")
    else:
        st.write("El archivo no contiene columnas de temperatura ESP32 o humedad ESP32.")
