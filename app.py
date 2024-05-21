import pandas as pd
import streamlit as st
from PIL import Image

    cols = ["Time", "temperatura ESP32", "humedad ESP32"]
    df1 = pd.read_csv(uploaded_file, usecols=cols)
    
    st.subheader('Perfil gráfico de la variable medida.')
    df1 = df1.set_index('Time')
    st.line_chart(df1)
    
    st.write(df1)
    st.subheader('Estadísticos básicos de los sensores.')
    # convertir esto en variable
    st.dataframe(df1["temperatura ESP32"].describe())
    
    min_temp = st.slider('Selecciona valor mínimo del filtro ', min_value=-10, max_value=45, value=23, key=1)
    min_hum = st.slider('Selecciona valor mínimo del filtro de humedad', min_value=0, max_value=100, value=50, key=2)
    
    # Filtrar el DataFrame utilizando query
    filtrado_df_min_temp = df1.query(f"`temperatura ESP32` > {min_temp}")
    filtrado_df_min_hum = df1.query(f"`humedad ESP32` > {min_hum}")
    
    # Mostrar el DataFrame filtrado
    st.subheader("Temperaturas superiores al valor configurado.")
    st.write('Dataframe Filtrado para Temperatura')
    st.write(filtrado_df_min_temp)
    
    st.subheader("Humedad superior al valor configurado.")
    st.write('Dataframe Filtrado para Humedad')
    st.write(filtrado_df_min_hum)
