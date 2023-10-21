import streamlit as st
import pandas as pd

# Cargar el conjunto de datos (reemplaza 'saber11.csv' con el nombre de tu archivo CSV)
df = pd.read_csv('/pruebas.csv')

# Filtrar 1: Filtrar por año
year = st.selectbox('Filtrar por año', df['Año'].unique())
df_filtro1 = df[df['Año'] == year]

# Filtrar 2: Filtrar por área de conocimiento
area_conocimiento = st.selectbox('Filtrar por área de conocimiento', df['Área de Conocimiento'].unique())
df_filtro2 = df[df['Área de Conocimiento'] == area_conocimiento]

# Filtrar 3: Filtrar por género
genero = st.selectbox('Filtrar por género', df['Género'].unique())
df_filtro3 = df[df['Género'] == genero]

# Filtrar 4: Filtrar por tipo de institución
tipo_institucion = st.selectbox('Filtrar por tipo de institución', df['Tipo de Institución'].unique())
df_filtro4 = df[df['Tipo de Institución'] == tipo_institucion]

# Filtrar 5: Filtrar por puntaje promedio
puntaje_promedio = st.slider('Filtrar por puntaje promedio', min_value=0, max_value=100, value=(0, 100))
df_filtro5 = df[(df['Puntaje Promedio'] >= puntaje_promedio[0]) & (df['Puntaje Promedio'] <= puntaje_promedio[1])]

# Mostrar los resultados en una tabla
st.dataframe(df_filtro1)
st.dataframe(df_filtro2)
st.dataframe(df_filtro3)
st.dataframe(df_filtro4)
st.dataframe(df_filtro5)
