import pandas as pd
import streamlit as st
from PIL import Image

st.title('Control de Temperatura y Humedad Huerta Urbana')
image = Image.open('grafana2.jpg')
st.image(image)

uploaded_file = st.file_uploader('Choose a file')

if uploaded_file is not None:
    df1 = pd.read_csv(uploaded_file)

    # Selección del nombre de la columna
    columna = st.selectbox('Selecciona la columna que deseas visualizar:', options=['temperatura ESP32', 'humedad ESP32'])

    if 'Time' in df1.columns:
        df1 = df1.set_index('Time')

    if columna in df1.columns:
        st.subheader('Perfil gráfico de la variable medida.')
        st.line_chart(df1[columna])
        
        st.write(df1)
        st.subheader('Estadísticos básicos de los sensores.')
        st.dataframe(df1[columna].describe())
        
        min_value = st.slider(f'Selecciona valor mínimo del filtro ({columna})', min_value=-10.0, max_value=100.0, value=23.0, key=1)
        # Filtrar el DataFrame utilizando query
        filtrado_df_min = df1.query(f"`{columna}` > {min_value}")
        # Mostrar el DataFrame filtrado
        st.subheader(f"{columna} superiores al valor configurado.")
        st.write('Dataframe Filtrado')
        st.write(filtrado_df_min)
        
        max_value = st.slider(f'Selecciona valor máximo del filtro ({columna})', min_value=-10.0, max_value=100.0, value=23.0, key=2)
        # Filtrar el DataFrame utilizando query
        filtrado_df_max = df1.query(f"`{columna}` < {max_value}")
        # Mostrar el DataFrame filtrado
        st.subheader(f"{columna} inferiores al valor configurado.")
        st.write('Dataframe Filtrado')
        st.write(filtrado_df_max)
    else:
        st.error(f"La columna seleccionada '{columna}' no se encuentra en el archivo cargado.")

else:
    st.warning('Necesitas cargar un archivo csv excel.')
