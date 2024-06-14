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
        dfu = pd.read_csv('Examen.csv')
        preguntas_csv = dfu.values.tolist()

        # Ordenar las preguntas aleatoriamente
        random.shuffle(preguntas_csv)

        respuestas_usuario = []

        with st.form("examen_form"):
            for i, pregunta in enumerate(preguntas_csv[:35], start=1):
                opciones = pregunta[1].split('_')
                respuesta_usuario = st.radio(f'{i}.- {pregunta[0]}', opciones, key=f'pregunta_{i-1}')
                respuestas_usuario.append((pregunta[0], respuesta_usuario))

            if st.form_submit_button('Enviar'):
                st.success('Se han enviado tus respuestas')
                st.balloons()






















    elif secciones=='Análisis de artículo':
        st.markdown('El siguiente ejercicio tiene como propósito evaluar la capacidad del estudiante para analizar las diferentes partes de un artículo de investigación y aplicar los conocimientos teóricos')
        st.caption('Lee con atención el artículo de investigación y responde las preguntas, el valor de este ejercicio es de 20 puntos de tu examen (35 puntos teóricos/20 puntos del análisis del artículo)')
        artículo=st.toggle('Ver artículo')
        if artículo==True:
            pdf_url='https://docs.google.com/document/d/e/2PACX-1vRPG6brmZTCJ4bbmUF_xa_od7XyTHBL6B6Cmqa8LVQBiQF6nF51z9NFOojbWauKUj0k-fr8IQrIwRyC/pub '

            st.markdown(f"""
            <iframe src="{pdf_url}" width="800" height="600" frameborder="0">
            <p>Este navegador no es compatible con la visualización de PDF. Descarga el PDF para verlo.</p>
            </iframe>
            """, unsafe_allow_html=True)
        with st.form('Escribe lo mas extensamente que puedas lo siguientes'):
            respuesta=st.text_area('Responde lo mejor posible en tu análisis del artículo, incluye lo siguiente: objetivos del estudio, justificación, problema, hipótesis, tipo de enfoque (experimental, no experimental, que tipo), consideras que es un estudio exploratorio, descriptivo, correlacional, explicativo, que variables independientes y dependiente observas, utilizaron muestreo, que caracteristicas tiene la población, identificas criterios de inclusión y exclusión, alguna observacion respecto a la metodología',height=600)
            enviar=st.form_submit_button('Enviar respuesta')


            if enviar==True:
                # Obtener la fecha actual
                fecha = datetime.datetime.now()

                # Preparar la consulta SQL
                query = "INSERT INTO ult_ev1_analisis (usuario,fecha_evaluacion, resultado_analisis) VALUES (%s,%s, %s)"

                # Ejecutar la consulta SQL
                cursor.execute(query, (nombre,fecha, respuesta))

                # Hacer commit de la transacción
                conn.commit()

                st.success('Se ha enviado tu respuesta')
                st.balloons()
