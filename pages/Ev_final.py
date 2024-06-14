import streamlit as st 
import pandas as pd 
import streamlit.components.v1 as components
import openpyxl
import psycopg2
from streamlit_lottie import st_lottie as stl
import datetime
import time


#Base de datos
conn = psycopg2.connect(
                        host="dpg-cokdc7gl5elc73c3klp0-a.oregon-postgres.render.com",
                        database="bajacaltec_ciencia",
                        user="bajacaltec_ciencia_user",
                        password="QnVGnpcQGxEr7q9W3YDiPS4ABxSTkAVn"
                    )
cursor=conn.cursor()

st.sidebar.caption('By Baja Caltec')

Desactivar=False
#from streamlit_lottie import st_lottie
nombre=st.sidebar.number_input('clave de alumno',step=1,)

contra = st.sidebar.text_input('Contraseña', type='password')
claves=[1258, 1705, 2019, 2810, 3471, 3568, 4269, 5024, 5937, 6357, 6893, 7149, 7412, 8532, 8731, 9175, 9186, 9275, 9624, 9803]

falcho=False
ingresar=st.sidebar.toggle('Ingresar',disabled=Desactivar)
counting = False

usuarios = ('189')
if ingresar ==True and contra in usuarios and nombre in claves:

    # Carga el DataFrame de preguntas
    df = pd.read_csv('examen.csv')

    # Obtiene el nombre del usuario
    nombre_usuario = st.text_input('Introduce tu nombre:')

    # Crea una lista para almacenar las respuestas del usuario
    respuestas_usuario = []

    # Muestra cada pregunta y opciones al usuario
    for index, row in df.iterrows():
        pregunta = row['Pregunta']
        opcion_1 = row['Opcion_1']
        opcion_2 = row['Opcion_2']
        opcion_3 = row['Opcion_3']
        opcion_4 = row['Opcion_4']

        # Crea un widget de radio para que el usuario seleccione la respuesta
        respuesta_usuario = st.radio(pregunta, [opcion_1, opcion_2, opcion_3, opcion_4])

        # Almacena la respuesta seleccionada por el usuario
        respuestas_usuario.append(respuesta_usuario)

    # Calcula la puntuación del usuario
    puntuacion = 0
    for i, respuesta in enumerate(respuestas_usuario):
        if respuesta == df.loc[i, 'Respuesta_correcta']:
            puntuacion += 1

    # Muestra la puntuación del usuario
    st.title('¡Examen finalizado!')
    st.write(f'Nombre: {nombre_usuario}')
    st.write(f'Puntuación: {puntuacion}/{len(df)}')
