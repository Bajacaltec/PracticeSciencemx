import streamlit as st
import psycopg2
import datetime

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
    # Resto de los usuarios...
}

# Conectar a la base de datos
base = conectar_base_de_datos()

# Interfaz principal
st.sidebar.title('Practice sciencemx')
st.sidebar.caption('By Baja Caltec')

# Entrada de código de acceso
acceso = int(st.sidebar.text_input('Codigo de acceso', type='password'))
ingresar = st.sidebar.toggle('Ingresar')

# Verificación del usuario
usuario = next((user for user, codigo in usuarios_accesos.items() if codigo == acceso), None)

if ingresar and usuario:
    st.sidebar.write(f'''Bienvenid@ {usuario}''')
    clases = [f'Clase {i}' for i in range(1, 8)]
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.sidebar.tabs(clases)

    # Artículo 1
    pdf_url = 'https://www.scielo.org.mx/scielo.php?pid=S2007-78902021000200050&script=sci_arttext'
    with tab1:
        st.subheader('Artículo 1 Estudio descriptivo')
        st.markdown('El siguiente ejercicio tiene como propósito evaluar la capacidad del estudiante para analizar las diferentes partes de un artículo de investigación y aplicar los conocimientos teóricos.')
        tiempo = datetime.datetime.now().strftime('%y-%m.%d %H:%M:%S')
        artículo = st.checkbox('Ver artículo', key=123)

        if artículo:
            st.markdown(f"""
            <iframe src="{pdf_url}" width="800" height="600" frameborder="0">
            </iframe>
            """)

        col1, col2 = st.columns([3, 1])
        with col1:
            with st.form('Escribe lo mas extensamente que puedas lo siguientes'):
                respuesta = st.text_area('Haz un análisis del artículo que incluya lo que se muestra a la derecha', height=600)
                enviar = st.form_submit_button('Enviar respuesta')

                if enviar:
                    # Obtener la fecha actual
                    fecha = datetime.datetime.now()

                    # Preparar la consulta SQL
                    cursor = base.cursor()
                    query = "INSERT INTO ult_ev1_analisis (usuario, fecha_evaluacion, resultado_analisis) VALUES (%s, %s, %s)"

                    # Ejecutar la consulta SQL
                    cursor.execute(query, (usuario, fecha, respuesta))

                    # Hacer commit de la transacción
                    base.commit()

                    st.success('Se ha enviado tu respuesta')
                    st.balloons()

        with col2:
            st.expander('Instrucciones')
            st.markdown('En este ejercicio debes incluir lo siguiente como parte del análisis del artículo: ')