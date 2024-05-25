import streamlit as st 
import pandas as pd 
import numpy as np
import funciones

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
