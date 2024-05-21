import pandas as pd
import streamlit as st
from PIL import Image

# Función para mostrar las estadísticas básicas y realizar el filtrado
def mostrar_estadisticos_y_filtrado(df, columna, min_valor_default, max_valor_default):
    st.subheader('Estadísticos básicos de los sensores.')
    st.dataframe(df[columna].describe())

    # Filtrar el DataFrame utilizando un slider para seleccionar el valor mínimo
    min_valor = st.slider(f'Selecciona valor mínimo del filtro para {columna}', min_value=float(df[columna].min()), max_value=float(df[columna].max()), value=min_valor_default, key=1)
    filtrado_df_min = df.query(f"`{columna}` > {min_valor}")

    # Mostrar el DataFrame filtrado para valores superiores al valor configurado
    st.subheader(f"{columna.capitalize()} superiores al valor configurado.")
    st.write('Dataframe Filtrado')
    st.write(filtrado_df_min)

    # Filtrar el DataFrame utilizando un slider para seleccionar el valor máximo
    max_valor = st.slider(f'Selecciona valor máximo del filtro para {columna}', min_value=float(df[columna].min()), max_value=float(df[columna].max()), value=max_valor_default, key=2)
    filtrado_df_max = df.query(f"`{columna}` < {max_valor}")

    # Mostrar el DataFrame filtrado para valores inferiores al valor configurado
    st.subheader(f"{columna.capitalize()} inferiores al valor configurado.")
    st.write('Dataframe Filtrado')
    st.write(filtrado_df_max)

# Título y carga de imagen
st.title('Control de Temperatura y Humedad Huerta Urbana')
image = Image.open('grafana2.jpg')
st.image(image)

# Cargar archivo CSV
uploaded_file = st.file_uploader('Choose a file')

if uploaded_file is not None:
    # Leer el archivo CSV
    df = pd.read_csv(uploaded_file)

    # Intentar convertir la columna 'Time' a formato datetime
    df['Time'] = pd.to_datetime(df['Time'], errors='coerce')
    df = df.dropna(subset=['Time'])  # Eliminar filas con valores NaT en 'Time'
    
    # Establecer la columna 'Time' como índice
    df = df.set_index('Time')

    # Verificar si hay datos de temperatura o humedad
    if "temperatura ESP32" in df.columns:
        columna = "temperatura ESP32"
        min_valor_default = 23  # Valor por defecto para el filtro de temperatura
        max_valor_default = 23
    elif "humedad ESP32" in df.columns:
        columna = "humedad ESP32"
        min_valor_default = 50  # Valor por defecto para el filtro de humedad
        max_valor_default = 50
    else:
        st.warning("El archivo no contiene columnas de temperatura ESP32 o humedad ESP32.")
        st.stop()

    st.subheader('Perfil gráfico de la variable medida.')
    st.line_chart(df[columna])

    st.write(df)
    mostrar_estadisticos_y_filtrado(df, columna, min_valor_default, max_valor_default)

else:
    st.warning('Necesitas cargar un archivo csv excel.')
