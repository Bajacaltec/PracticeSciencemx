import streamlit as st
import psycopg2
import funciones
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
acceso = int(st.sidebar.text_input('Codigo de acceso', type='password'))
ingresar = st.sidebar.toggle('Ingresar')

# Verificación del usuario


# Verificación del usuario
usuario = next((user for user, codigo in usuarios_accesos.items() if codigo == acceso), None)
if ingresar and usuario:
    st.sidebar.write(f'''Bienvenid@ {usuario}''')
    clases = [f'Artículo {i}' for i in range(1, 4)]
    tab1, tab2, tab3 = st.tabs(clases)


    #Artículo 1
    pdf_url='https://www.scielo.org.mx/scielo.php?pid=S2007-78902021000200050&script=sci_arttext '
    with tab1:
        st.subheader('Artículo 1 Estudio descriptivo')
        st.markdown('El siguiente ejercicio tiene como propósito evaluar la capacidad del estudiante para analizar las diferentes partes de un artículo de investigación y aplicar los conocimientos teóricos')
        tiempo=datetime.datetime.now().strftime('%y-%m.%d %H:%M:%S')
        artículo=st.toggle('Ver artículo',key=123)
        if artículo==True:
            st.markdown(f"""
            <iframe src="{pdf_url}" width="800" height="600" frameborder="0">
            <p>Este navegador no es compatible con la visualización de PDF. Descarga el PDF para verlo.</p>
            </iframe>
            """, unsafe_allow_html=True)
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
                    nombre_correspondiente = next((nombre for nombre, codigo in usuarios_accesos.items() if codigo == acceso), None)
                    cursor.execute(query, (nombre_correspondiente,fecha, respuesta))

                    # Hacer commit de la transacción
                    conn.commit()

                    st.success('Se ha enviado tu respuesta')
                    st.balloons()
        with col2:
            st.expander('Instrucciones')
            st.caption('En este ejercicio debes incluir lo siguiente como parte del análisis del artículo: ')
            st.write('Problema de investigación')
            st.write('Pregunta de investigación')
            st.write('Objetivos')
            st.write('Hipótesis de investigación e hipótesis nula')
            st.write('Justificación')
            st.write('Tipo de diseño')
            st.write('Análisis estadístico')
            st.write('Población, tipo de muestreo, criterios de inclusión y exclusión')



