import pandas as pd
import streamlit as st
from PIL import Image

st.title('Control de Temperatura y Humedad Huerta Urbana')
image = Image.open('grafana2.jpg')
st.image(image)

uploaded_file = st.file_uploader('Choose a file')

if uploaded_file is not None:
    # Leer el archivo CSV
    df1 = pd.read_csv(uploaded_file)

    # Crear un selector para que el usuario elija entre 'temperatura ESP32' y 'humedad ESP32'
    columna = st.selectbox(
        'Seleccione la variable a visualizar',
        ('temperatura ESP32', 'Time,"humedad ESP32"')
    )

    st.subheader('Perfil gráfico de la variable medida.')
    df1 = df1.set_index('Time')
    st.line_chart(df1[columna])
    
    st.write(df1)
    st.subheader('Estadísticos básicos de los sensores.')
    st.dataframe(df1[columna].describe())
    
    # Filtros de valores mínimos y máximos basados en la columna seleccionada
    min_val = st.slider(f'Selecciona valor mínimo del filtro ({columna})', min_value=-10, max_value=100, value=23, key=1)
    filtrado_df_min = df1.query(f"`{columna}` > {min_val}")
    st.subheader(f"{columna.capitalize()} superiores al valor configurado.")
    st.write('Dataframe Filtrado')
    st.write(filtrado_df_min)
    
    max_val = st.slider(f'Selecciona valor máximo del filtro ({columna})', min_value=-10, max_value=100, value=23, key=2)
    filtrado_df_max = df1.query(f"`{columna}` < {max_val}")
    st.subheader(f"{columna.capitalize()} inferiores al valor configurado.")
    st.write('Dataframe Filtrado')
    st.write(filtrado_df_max)

else:
    st.warning('Necesitas cargar un archivo csv excel.')
