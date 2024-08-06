import streamlit as st
import csv
import random
import psycopg2
import datetime
import pandas as pd
import datetime


st.set_page_config(layout='wide')
# Función para conectar a la base de datos
def conectar_base_de_datos():
    conn = psycopg2.connect(
        host="dpg-cokdc7gl5elc73c3klp0-a.oregon-postgres.render.com",
        database="bajacaltec_ciencia",
        user="bajacaltec_ciencia_user",
        password="QnVGnpcQGxEr7q9W3YDiPS4ABxSTkAVn"
    )
    return conn


# Diccionario de permisos de usuario
usuarios_accesos = {
    'fernando': 1111,
    "Alamillo Martínez María Aurelia (Baja)": 9275,
    "Alarcón Martínez Laura Patricia": 3568,
    "Cano García Yolanda (Baja)": 8731,
    "Cárdenas de la Cruz Perla Juana": 2019,
    "Cardoza Amador Evelyng Pamela": 7412,
    "Corral Montoya María Cristina": 9803,
    "Delgado Gurrola Jonathan Eduardo": 6357,
    "Gaytán Pérez Mayra Gorety": 5024,
    "González Vidales Jaquelìne": 9186,
    "Guzmán Pérez Dulce Carolina": 4269,
    "Hernández Ibarra Ana Mayela": 8532,
    "Maldonado Galarza Jimena Elizabeth": 1705,
    "Martínez Antuna Diana del Socorro": 6893,
    "Miramontes Romero Nancy Nallely": 3471,
    "Ortega Medrano Amanda": 1258,
    "Rodríguez Salas Maricela": 9624,
    "Romero González Javier Eduardo": 5937,
    "Rosales Hernández Eva Judith": 2810,
    "Sosa Pérez Anyela Amaranhta": 7149,
    "Valenzuela Herrera Rosa Isela": 9175
}

base = conectar_base_de_datos()

# Interfaz principal
st.sidebar.title('Practice sciencemx')
st.sidebar.caption('By Baja Caltec')

# Entrada de código de acceso
acceso = st.sidebar.text_input('Codigo de acceso', type='password')
ingresar = st.sidebar.toggle('Ingresar')

# Verificación del usuario
try:
    if acceso and ingresar:
        acceso = int(acceso)  # Intenta convertir a entero si no está vacío
        usuario = next((user for user, codigo in usuarios_accesos.items() if codigo == acceso), None)
        if usuario:
                st.sidebar.write(f'Bienvenid@ a tu examen {usuario}')
                st.image('Imagenes/unidur.png')
                st.markdown('_________________')
                st.header('Exámen teórico')

                st.markdown("Parte teórica del exámen final debes seleccionar la respuesta correcta y darle al boton enviar, cuentas con 50 minutos.")
                dfu = pd.read_csv('examen_II 2.csv')
                preguntas_csv = dfu.values.tolist()

                # Ordenar las preguntas aleatoriamente
                random.shuffle(preguntas_csv)

                respuestas_usuario = []
                calificacion_total = 0

                with st.form("examen_form",):
                    for i, pregunta in enumerate(preguntas_csv[:27], start=1):
                        opciones = pregunta[1].split('_')
                        respuesta_usuario = st.radio(f'{i}.- {pregunta[0]}', opciones, key=f'pregunta_{i-1}')

                        # Crear un mapeo de opciones a índices
                        indice_opciones = {opcion: indice for indice, opcion in enumerate(opciones)}

                        # Crear un diccionario con la pregunta, respuesta y calificación
                        calificacion_pregunta = 1 if indice_opciones[respuesta_usuario] == int(pregunta[2]) else 0
                        pregunta_con_respuesta = {
                            "Pregunta": pregunta[0],
                            "Respuesta": respuesta_usuario,
                            "Calificación": calificacion_pregunta
                        }

                        # Agregar el diccionario a la lista y actualizar la calificación total
                        respuestas_usuario.append(pregunta_con_respuesta)
                        calificacion_total += calificacion_pregunta

                    enviar = st.form_submit_button('Enviar')

                if enviar==True:
                    conn=conectar_base_de_datos()
                    cursor=conn.cursor()
                    cursor.execute('''CREATE TABLE IF NOT EXISTS resultados_3examen (
                        id_usuario INT PRIMARY KEY NOT NULL,
                        pregunta TEXT NOT NULL,
                        respuesta TEXT NOT NULL,
                        calificacion_pregunta INT NOT NULL,
                        calificacion_total INT NOT NULL,
                        fecha TEXT
                    )''')
                    conn.commit()
                    resp=str(respuestas_usuario)
                
                    consulta = """
                        INSERT INTO resultados_3examen (id_usuario, pregunta,respuesta,calificacion_pregunta, calificacion_total,fecha)
                        VALUES (%s, %s, %s,%s,%s,%s)
                    """
                    fecha=datetime.datetime.now()
                    valores = (acceso,resp,resp,1,calificacion_total,fecha)
                    cursor.execute(consulta,valores)
                
                    conn.commit()
                    conn.close()

                    st.success('Se han enviado tus respuestas')
                    st.balloons()

            
                    


except ValueError:
    st.error('Por favor ingresa un código de acceso válido')
except Exception as e:
    st.error(f'Ocurrió un error: {e}')
finally:
    if 'base' in locals() and base is not None:
        base.close()