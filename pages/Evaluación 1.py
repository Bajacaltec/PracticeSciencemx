import streamlit as st 
import pandas as pd 
import streamlit.components.v1 as components
import openpyxl
import psycopg2
from streamlit_lottie import st_lottie as stl

#Base de datos
conn = psycopg2.connect(
                        host="dpg-cokdc7gl5elc73c3klp0-a.oregon-postgres.render.com",
                        database="bajacaltec_ciencia",
                        user="bajacaltec_ciencia_user",
                        password="QnVGnpcQGxEr7q9W3YDiPS4ABxSTkAVn"
                    )


st.sidebar.caption('By Baja Caltec')

Desactivar=False
usuario=st.sidebar.text_input('Usuario')
usuarios=['AMMA']
#from streamlit_lottie import st_lottie
contra = st.sidebar.text_input('Contraseña', type='password')
falcho=False
ingresar=st.sidebar.toggle('Ingresar',disabled=Desactivar)

usuarios = ('2089', '234')
if ingresar ==True and contra in usuarios:
    st.subheader('Evaluación unidad 1: Historía del pensamiento científico')
    st.info('Haz iniciado el periodo de evaluación, cuentas con 10 minutos para terminar la evaluación')
    with st.form('Evaluación 1'):
        st.text_input('1.¿Pregunta hipotética no. 1?')
        st.radio('2.Pregunta hipotética no.2',['Cierto','Falso'])
        
        enviar_prueba=st.form_submit_button('Enviar')
        if enviar_prueba==True: #and usuario in usuarios:
            #Enviar prueba al termino de 10 minutos
            try:
                st.success('Se ha enviado tu evaluación')
                st.balloons()
            except:
                st.error('Hubo un error, contacta al docente')