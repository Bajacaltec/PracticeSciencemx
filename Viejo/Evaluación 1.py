import streamlit as st 
import pandas as pd 
import streamlit.components.v1 as components
import openpyxl
import psycopg2
from streamlit_lottie import st_lottie as stl
import datetime

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
contra = st.sidebar.text_input('Contraseña', type='password')
nombre=st.sidebar.number_input('clave de alumno',step=1,)
claves=[1258, 1705, 2019, 2810, 3471, 3568, 4269, 5024, 5937, 6357, 6893, 7149, 7412, 8532, 8731, 9175, 9186, 9275, 9624, 9803]

falcho=False
ingresar=st.sidebar.toggle('Ingresar',disabled=Desactivar)

usuarios = ('234')
if ingresar ==True and contra in usuarios and nombre in claves:
    st.subheader('Evaluación unidad 1: Pensamiento crítico')
    st.info('Haz iniciado el periodo de evaluación, cuentas con 10 minutos para terminar la evaluación')
    with st.form('Evaluación 1'):
        claridad=st.radio('1.-¿La claridad en el pensamiento crítico se relaciona con el hecho de entender el argumento o problema de manera clara y precisa?',['Cierto','Falso'],horizontal=True)
        if claridad=='Cierto':
            claridad=1
        else:
            claridad=0
        precision=st.text_input('2.-¿Cúal es la definición de precisión en el pensamiento crítico?')
    
        certeza=st.radio('3.-¿Como se relaciona el concepto de certeza con el pensamiento crítico?',['La calidad de la información determinará la calidad de la conclusión','Saber a ciencia cierta el conocimiento base para la conclusión','Tener premisas lógicas'],horizontal=False)
        if certeza=='La calidad de la información determinará la calidad de la conclusión':
            certeza=1
        else:
            certeza=0
        certeza2=st.radio('4.-¿Si dentro de nuestro análisis de datos se ingresa información incorrecta, la conclusión será incorrecta, a que característica del pensamiento crítico pertenece esta definición?',['Precisión','Certeza','Claridad'])
        consistencia=st.radio('5.-¿Los dos tipos de consistencía son lógica y práctica ?',['Falso','Cierto'])
        consistencia2=st.radio('6.-El siguiente argumento tiene certeza lógica, -todos los hombres son poco romanticos, Alberto es un hombre, por lo tanto Alberto es poco romántico- ',['Correcto','Incorrecto'])
        enviar=st.form_submit_button('Enviar')
        if enviar==True:
            try:
                fecha_actual = datetime.datetime.now()

                insert_query = """
                            INSERT INTO evaluacion1 (caractpc, precision, certeza, certeza2, consistencia, consistencia2,certezalogica,certezalog3)
                            VALUES (%s, %s, %s, %s, %s, %s,%s,%s)
                            """
                cursor.execute(insert_query, (claridad, precision, certeza, certeza2, consistencia, consistencia2,nombre,fecha_actual))

    # Commit the changes and close the connection
                conn.commit()
                st.success('Enviado')
            except:
                st.error('Error de captura')

