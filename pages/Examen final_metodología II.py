import streamlit as st
import csv
import random
import psycopg2
import datetime
import pandas as pd

#Base de datos
conn = psycopg2.connect(
                        host="dpg-cokdc7gl5elc73c3klp0-a.oregon-postgres.render.com",
                        database="bajacaltec_ciencia",
                        user="bajacaltec_ciencia_user",
                        password="QnVGnpcQGxEr7q9W3YDiPS4ABxSTkAVn"
                    )
cursor=conn.cursor()

#cursor.execute('''COPY examen FROM 'Examen.csv' DELIMITER ',' CSV HEADER''')

st.sidebar.caption('By Baja Caltec')

Desactivar = False
nombre = st.sidebar.number_input('clave de alumno', step=1)
contra = st.sidebar.text_input('Contraseña', type='password')
claves = [1258, 1705, 2019, 2810, 3471, 3568, 4269, 5024, 5937, 6357, 6893, 7149, 7412, 8532, 8731, 9175, 9186, 9275, 9624, 9803, 1111, 9999]

ingresar = st.sidebar.toggle('Ingresar', disabled=Desactivar)
usuarios = ('189',)  # Asegurarse de que 'usuarios' sea una tupla

if ingresar and contra in usuarios and nombre in claves:
    st.subheader('Evaluación final')

    secciones = st.selectbox('Sección', ['Teoría', 'Análisis de artículo'])



    if secciones == 'Teoría':
        dfu = pd.read_csv('examen.csv')
        preguntas_csv = dfu.values.tolist()

        # Ordenar las preguntas aleatoriamente
        random.shuffle(preguntas_csv)

        respuestas_usuario = []
        calificacion_total = 0

    if secciones == 'Teoría':
        dfu = pd.read_csv('examen_II.csv')
        preguntas_csv = dfu.values.tolist()

        # Ordenar las preguntas aleatoriamente
        random.shuffle(preguntas_csv)

        respuestas_usuario = []
        calificacion_total = 0

        with st.form("examen_form"):
            for i, pregunta in enumerate(preguntas_csv[:20], start=1):
                opciones = pregunta[1].split('_')
                respuesta_usuario = st.radio(f'{i}.- {pregunta[0]}', opciones, key=f'pregunta_{i-1}')

                # Crear un mapeo de opciones a índices
                indice_opciones = {opcion: indice for indice, opcion in enumerate(opciones)}

                # Crear un diccionario con la pregunta, respuesta y calificación
                calificacion_pregunta = 1 if indice_opciones[respuesta_usuario] == int(pregunta[2]) else 0
                pregunta_con_respuesta = {
                    "Pregunta": pregunta[0],
                    "Respuesta": respuesta_usuario,
                    "Calificación": calificacion_pregunta
                }

                # Agregar el diccionario a la lista y actualizar la calificación total
                respuestas_usuario.append(pregunta_con_respuesta)
                calificacion_total += calificacion_pregunta

            enviar = st.form_submit_button('Enviar')

        if enviar==True:

            cursor.execute('''CREATE TABLE IF NOT EXISTS resultados_1examen (
                id_usuario INT PRIMARY KEY NOT NULL,
                pregunta TEXT NOT NULL,
                respuesta TEXT NOT NULL,
                calificacion_pregunta INT NOT NULL,
                calificacion_total INT NOT NULL
            )''')
            conn.commit()
            resp=str(respuestas_usuario)
        
            consulta = """
                INSERT INTO resultados_1examen (id_usuario, pregunta,respuesta,calificacion_pregunta, calificacion_total)
                VALUES (%s, %s, %s,%s,%s)
            """
            valores = (nombre,resp,resp,1,calificacion_total)
            cursor.execute(consulta,valores)
        
            conn.commit()
            conn.close()

            st.success('Se han enviado tus respuestas')
            st.balloons()

#Falta hacer que califique automaticamente