import streamlit as st
import pandas as pd 
import numpy as np
import psycopg2
import datetime


def conectar_base_de_datos():
    conn = psycopg2.connect(
        host="dpg-cokdc7gl5elc73c3klp0-a.oregon-postgres.render.com",
        database="bajacaltec_ciencia",
        user="bajacaltec_ciencia_user",
        password="QnVGnpcQGxEr7q9W3YDiPS4ABxSTkAVn"
    )
    return conn
def crear_db(variables,tabla):
    conn = psycopg2.connect(
                        host="dpg-cokdc7gl5elc73c3klp0-a.oregon-postgres.render.com",
                        database="bajacaltec_ciencia",
                        user="bajacaltec_ciencia_user",
                        password="QnVGnpcQGxEr7q9W3YDiPS4ABxSTkAVn"
                    )
    cursor=conn.cursor()
    create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {tabla} (
            {", ".join([f"{name} {type}" for name, type in variables.items()])}
        )
    """

    cursor.execute(create_table_query)
    cursor.execute(f"SELECT* FROM {tabla}")
    x=cursor.fetchall()

    conn.commit()
    conn.close()
    st.write(x)

def insertar_db(tabla,datos):
    conn = psycopg2.connect(
                        host="dpg-cokdc7gl5elc73c3klp0-a.oregon-postgres.render.com",
                        database="bajacaltec_ciencia",
                        user="bajacaltec_ciencia_user",
                        password="QnVGnpcQGxEr7q9W3YDiPS4ABxSTkAVn"
                    )
    cursor=conn.cursor()
    column_names = list(datos.keys())

    # Create a placeholder string for values (e.g., %s, %s, ...)
    placeholder_str = ", ".join(["%s" for _ in column_names])

    # Create the INSERT query with column names and placeholders
    insert_query = f"""
        INSERT INTO {tabla} ({", ".join(column_names)})
        VALUES ({placeholder_str})
    """

    # Extract values from the dictionary
    values = list(datos.values())

    # Execute the INSERT query, passing the values as a tuple
    cursor.execute(insert_query, values)

    conn.commit()
    conn.close()


    # Ejemplo de valores de datos
def generate_variable_inputs(num_variables):
    variables = {}
    for i in range(num_variables):
        variable_name = st.text_input(f"Nombre de la variable {i + 1}:")
        if variable_name != "":
            variable_type = st.selectbox(f"Tipo de dato de {variable_name}:", options=["VARCHAR", "INTEGER", "FLOAT", ...])
            variables[variable_name] = variable_type
    return variables

def ejercicio_articulos(nombre,pdf):
    key3=np.random.rand
    st.markdown('El siguiente ejercicio tiene como propósito evaluar la capacidad del estudiante para analizar las diferentes partes de un artículo de investigación y aplicar los conocimientos teóricos')
    tiempo=datetime.datetime.now().strftime('%y-%m.%d %H:%M:%S')
    artículo=st.toggle('Ver artículo',key=key3)
    if artículo==True:
        st.markdown(f"""
        <iframe src="{pdf}" width="800" height="600" frameborder="0">
        <p>Este navegador no es compatible con la visualización de PDF. Descarga el PDF para verlo.</p>
        </iframe>
        """, unsafe_allow_html=True)
    key1=np.random.rand
    key2=np.random.rand
    col1,col2=st.columns([3,1])
    with col1:
        with st.form('Escribe lo mas extensamente que puedas lo siguientes'):
            respuesta=st.text_area('Haz un análisis del artículo que incluya lo que se muestra a la derecha',height=600)
            enviar=st.form_submit_button('Enviar respuesta')
            conn=conectar_base_de_datos()


            if enviar==True:
                # Obtener la fecha actual
                fecha = datetime.datetime.now()
                cursor=conn.cursor()
                # Preparar la consulta SQL
                query = "INSERT INTO ult_ev1_analisis (usuario,fecha_evaluacion, resultado_analisis) VALUES (%s,%s, %s)"

                # Ejecutar la consulta SQL
                cursor.execute(query, (nombre,fecha, respuesta))

                # Hacer commit de la transacción
                conn.commit()

                st.success('Se ha enviado tu respuesta')
                st.balloons()
    with col2:
        st.info('Objetivo de investigación')
        st.info('Problema de investigación')
        st.info('Justificación')
        st.info('Hipótesis')
        st.info('Muestra y población')
        st.info('Tipo de diseño (Experimental, exploratorio, descriptivo, causal)')
        st.info('Errores metodológicos')