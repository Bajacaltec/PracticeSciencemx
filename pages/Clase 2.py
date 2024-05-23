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
    st.title('Pensamiento crítico') 
    tab1,tab2,tab3=st.tabs(['Pensamiento crítico','PC1','Tipos de ciencia'])
    with tab1:
        st.title('¿Qué es el pensamiento crítico?')
    with tab2:
        st.title('Pensamiento crítico 1')
  

# Conectarse a la base de datos Postgres
        

        # Crear un cursor para ejecutar sentencias SQL
        cursor = conn.cursor()

        # Ejecutar una consulta para obtener los datos de la tabla
        cursor.execute("SELECT * FROM encuestas")

        # Obtener los resultados de la consulta
        resultados = cursor.fetchall()

        # Convertir los resultados en un DataFrame de Pandas
        df = pd.DataFrame(resultados, columns=[col.name for col in cursor.description])

        st.dataframe(df)
       

        # Cerrar la conexión a la base de datos
        conn.close()
        #Graficos
        genero_col=df['genero']
        genero_frec=genero_col.value_counts()
        st.write(genero_frec)
        st.bar_chart(genero_frec)
        









elif ingresar==True and contra not in usuarios:
    st.sidebar.error('Contraseña incorrecta')
