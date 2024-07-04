import streamlit as st 
import pandas as pd 
import numpy as np
import funciones
import psycopg2
st.sidebar.subheader('Practice science')
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
falcho=False
ingresar=st.sidebar.toggle('Ingresar',disabled=Desactivar)

usuarios = ('2089', '234')
#key=st.sidebar.text_input('Poner API key gemini')

if ingresar ==True and contra in usuarios:
    st.header('Centro de control')

    with st.expander('Crear una nueva tabla'):
        col1,col2,col3=st.columns(3)   

        with col1:
            num_variables = st.number_input("Número de variables:", min_value=1)
            global variables
            variables = {}
            for i in range(num_variables):
                numero_pregunta = i + 1  # Suma 1 para que el número empiece en 1
    # ... (resto del código
                variable_name = st.text_input(f"Nombre de la variable {i + 1}:")
                if variable_name != "":
                    variable_type = st.selectbox(f"Tipo de dato de {variable_name}:", options=["VARCHAR", "INTEGER", "FLOAT", ...])
                    variables[variable_name] = variable_type
            global nombre_tabla
            nombre_tabla = st.text_input('Nombre de la tabla',key=12,help='Palabra continua, no separaciones, ejemplo: Nueva_tabla')
            boton_crear = st.button('Crear',key=1233)

            if boton_crear:
                try:
                    funciones.crear_db(variables, nombre_tabla)
                    st.success('Base de datos creada')
                    
                except Exception as e:
                    with col2:
                        st.error(f'Error: {e}')
        with col2:
            st.write(variables)
    with st.expander('Ver tablas'):
        st.subheader('Ver tablas')
        ver=st.toggle('Ver tablas')
        if ver==True:
            nombre_de_tabla=st.text_input('')
            tablas=f'''SELECT * FROM {nombre_de_tabla} '''
            dbdf=pd.read_sql(tablas,conn)
            st.dataframe(dbdf,width=900)
            for index, row in dbdf.iterrows():
                st.write(row)

            

            

