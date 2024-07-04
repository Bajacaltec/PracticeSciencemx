import streamlit as st
import psycopg2
import funciones
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
    'fernando':1111,
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
usuario = next((user for user, codigo in usuarios_accesos.items() if codigo == int(acceso)), None)
pdf_url='https://docs.google.com/document/d/e/2PACX-1vRPG6brmZTCJ4bbmUF_xa_od7XyTHBL6B6Cmqa8LVQBiQF6nF51z9NFOojbWauKUj0k-fr8IQrIwRyC/pub '
if ingresar and usuario:
    st.sidebar.write(f'''Bienvenid@ {usuario}''')
    clases = [f'Clase {i}' for i in range(1, 8)]
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(clases)
    with tab1:
        st.subheader('Clase 1 Obtención de datos')
        funciones.ejercicio_articulos(usuario,pdf_url)

