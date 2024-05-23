import streamlit as st 
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#Base de datos
conn = psycopg2.connect(
                        host="dpg-cokdc7gl5elc73c3klp0-a.oregon-postgres.render.com",
                        database="bajacaltec_ciencia",
                        user="bajacaltec_ciencia_user",
                        password="QnVGnpcQGxEr7q9W3YDiPS4ABxSTkAVn"
                    )

st.sidebar.caption('By Baja Caltec')

Desactivar=False
#from streamlit_lottie import st_lottie
contra = st.sidebar.text_input('Contraseña', type='password')
falcho=False
ingresar=st.sidebar.toggle('Ingresar',disabled=Desactivar)

usuarios = ('2089', '234')

if ingresar ==True and contra in usuarios:
        st.title('Anteproyecto')

        tab1,tab2,tab3,tab4=st.tabs(['Idea de investigación','Introducción','Planteamiento del problema','Justificación'])
