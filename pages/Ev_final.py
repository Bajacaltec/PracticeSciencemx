import streamlit as st
import csv
import random
import streamlit.components.v1 as components
import openpyxl
import psycopg2
from streamlit_lottie import st_lottie as stl
import datetime
import time
import csv
from streamlit_pdf_viewer import pdf_viewer


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
    st.subheader('Evaluación final')

    secciones=st.selectbox('Sección',['Teoría','Análisis de artículo'])
    if secciones=='Teoría':

        # Carga el archivo CSV
        with open('Examen.csv') as f:
            lector = csv.reader(f)

            # Salta la primera fila (encabezados)
            next(lector)

            # Convierte las filas en una lista
            preguntas_csv = list(lector)

        # Ordena las preguntas aleatoriamente
        random.shuffle(preguntas_csv)

        # Crea el formulario
        with st.form("Examen de opción múltiple"):
            # Muestra preguntas aleatorias
            try:
                for i in range(45):
                    numero_pregunta = i + 1  # Suma 1 para que el número empiece en 1
                    pregunta = preguntas_csv[i][0]
                    opciones = preguntas_csv[i][1].split('_')
                    respuesta_correcta = int(preguntas_csv[i][2])

                    respuesta_usuario = st.radio(f' {numero_pregunta}.- {pregunta}', opciones)

                    

                boton_enviar = st.form_submit_button("Enviar respuestas")

                # Muestra el resultado si se ha enviado el formulario
                if boton_enviar:
                    st.success('Haz finalizado y enviado tus respuestas')
                    st.balloons()

            except:
                st.error('Error')
    elif secciones=='Análisis de artículo':
        st.markdown('El siguiente ejercicio tiene como propósito evaluar la capacidad del estudiante para analizar las diferentes partes de un artículo de investigación y aplicar los conocimientos teóricos')
        st.caption('Lee con atención el artículo de investigación y responde las preguntas, el valor de este ejercicio es de 20 puntos de tu examen (35 puntos teóricos/20 puntos del análisis del artículo)')
        artículo=st.toggle('Ver artículo')
        pdf_url = "https://url_de_tu_pdf.com"  # Reemplaza con la URL real del PDF

        st.markdown(f"""
        <iframe src="{pdf_url}" width="800" height="600" frameborder="0">
        <p>Este navegador no es compatible con la visualización de PDF. Descarga el PDF para verlo.</p>
        </iframe>
        """, unsafe_allow_html=True)
        with st.form('Escribe lo mas extensamente que puedas lo siguientes'):
            respuesta=st.text_area('Responde lo mejor posible en tu análisis del artículo, incluye lo siguiente: objetivos del estudio, justificación, problema, hipótesis, tipo de enfoque (experimental, no experimental, que tipo), consideras que es un estudio exploratorio, descriptivo, correlacional, explicativo, que variables independientes y dependiente observas, utilizaron muestreo, que caracteristicas tiene la población, identificas criterios de inclusión y exclusión, alguna observacion respecto a la metodología',height=600)
            enviar=st.form_submit_button('Enviar respuesta')