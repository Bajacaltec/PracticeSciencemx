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
        with tab1:
                st.subheader('¿Como encontrar ideas para una investigación?')
                st.write("""Explorar tus intereses y áreas de conocimiento: Reflexiona sobre tus intereses académicos, profesionales y personales. ¿Qué temas te apasionan? ¿En qué áreas tienes experiencia o conocimiento previo? Elegir un tema que te motive y en el que tengas cierto bagaje te permitirá abordar la investigación con mayor entusiasmo y dedicación.

Revisar literatura académica: Investiga en revistas científicas, libros especializados y bases de datos académicas como SciELO, JSTOR o Google Scholar. Busca artículos recientes y relevantes relacionados con tu área de interés. Identifica las brechas de conocimiento, los debates actuales y las nuevas tendencias en el campo.

Analizar problemas y necesidades: Observa tu entorno social, profesional o comunitario. ¿Qué problemas o necesidades puedes identificar que podrían ser objeto de investigación? ¿Cómo tu investigación podría contribuir a solucionarlos o mejorar la situación actual?

Consultar con expertos: Dialoga con profesores, investigadores y profesionales en tu área de interés. Solicita su orientación, sugerencias y recomendaciones sobre posibles temas de investigación. Aprovecha su experiencia y conocimiento para afinar tus ideas.""")
                st.subheader('Viabilidad del proyecto')
                st.info('Evalúa si el tema elegido es viable en términos de tiempo, recursos y acceso a información. Asegúrate de que puedas recopilar datos suficientes y de calidad para realizar una investigación rigurosa y completa')
                st.subheader('Definir preguntas de investigación')
                st.info('Una vez elegido el tema, formula preguntas de investigación claras, precisas y relevantes que guíen tu trabajo. Las preguntas deben ser factibles de responder y contribuir al conocimiento en el área.')
