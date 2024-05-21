import pandas as pd
import streamlit as st
from PIL import Image

st.title('Control de Temperatura y Humedad Huerta Urbana')
image = Image.open('grafana2.jpg')
st.image(image)

uploaded_file = st.file_uploader('Choose a file')

if uploaded_file is not None:
    df1 = pd.read_csv(uploaded_file)
    
    st.write("Contenido del archivo cargado:")
    st.write(df1.head())

    if 'Time' not in df1.columns:
        st.error("El archivo CSV no contiene una columna llamada 'Time'. Por favor, verifica el archivo y vuelve a cargarlo.")
    else:
        df1['Time'] = pd.to_datetime(df1['Time'], errors='coerce')
        df1 = df1.dropna(subset=['Time'])  # Eliminar filas con valores NaT en 'Time'
        df1 = df1.set_index('Time')
        
        # Verificar si hay datos de temperatura o humedad
        if "temperatura ESP32" in df1.columns:
            columna = "temperatura ESP32"
            min_valor_default = 23
            max_valor_default = 23
        elif "humedad ESP32" in df1.columns:
            columna = "humedad ESP32"
            min_valor_default = 50
            max_valor_default = 50
        else:
            st.warning("El archivo no contiene columnas de temperatura ESP32 o humedad ESP32.")
            st.stop()

        st.subheader('Perfil gráfico de la variable medida.')
        st.line_chart(df1[columna])

        st.write(df1)
        st.subheader('Estadísticos básicos de los sensores.')
        st.dataframe(df1[columna].describe())

        min_valor = st.slider(f'Selecciona valor mínimo del filtro para {columna}', min_value=float(df1[columna].min()), max_value=float(df1[columna].max()), value=min_valor_default, key=1)
        filtrado_df_min = df1.query(f"`{columna}` > {min_valor}")

        st.subheader(f"{columna.capitalize()} superiores al valor configurado.")
        st.write('Dataframe Filtrado')
        st.write(filtrado_df_min)

        max_valor = st.slider(f'Selecciona valor máximo del filtro para {columna}', min_value=float(df1[columna].min()), max_value=float(df1[columna].max()), value=max_valor_default, key=2)
        filtrado_df_max = df1.query(f"`{columna}` < {max_valor}")

        st.subheader(f"{columna.capitalize()} inferiores al valor configurado.")
        st.write('Dataframe Filtrado')
        st.write(filtrado_df_max)

else:
    st.warning('Necesitas cargar un archivo csv excel.')
