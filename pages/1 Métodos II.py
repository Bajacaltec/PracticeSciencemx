import streamlit as st 
import pandas as pd 
import streamlit.components.v1 as components
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
practica=[]
for i in range(1,9):
    practica.append('Práctica '+str(i))
usuarios = ('234')
if ingresar ==True and contra in usuarios and nombre in claves:
    st1,st2,st3,st4,st5,st6,st7,st8=st.tabs(practica)
    with st1:
        st.sidebar.subheader('Metodología II')
        st.write('Práctica I')