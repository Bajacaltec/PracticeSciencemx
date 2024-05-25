import streamlit as st
import pandas as pd 
import numpy as np
import psycopg2

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


    # Ejemplo de valores de datos
def generate_variable_inputs(num_variables):
    variables = {}
    for i in range(num_variables):
        variable_name = st.text_input(f"Nombre de la variable {i + 1}:")
        if variable_name != "":
            variable_type = st.selectbox(f"Tipo de dato de {variable_name}:", options=["VARCHAR", "INTEGER", "FLOAT", ...])
            variables[variable_name] = variable_type
    return variables