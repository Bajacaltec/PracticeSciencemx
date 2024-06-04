import streamlit as st 
import pandas as pd 
import streamlit.components.v1 as components
import openpyxl
import psycopg2
from streamlit_lottie import st_lottie as stl
import datetime
import time
import schedule


#Base de datos
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
nombre=st.sidebar.number_input('clave de alumno',step=1,)

contra = st.sidebar.text_input('Contraseña', type='password')
claves=[1258, 1705, 2019, 2810, 3471, 3568, 4269, 5024, 5937, 6357, 6893, 7149, 7412, 8532, 8731, 9175, 9186, 9275, 9624, 9803]

falcho=False
ingresar=st.sidebar.toggle('Ingresar',disabled=Desactivar)
counting = False

usuarios = ('189')
if ingresar ==True and contra in usuarios and nombre in claves:
    st.subheader('2da evaluación')
    st.caption('Cuentas con 10 minutos para enviar tus respuestas')
    with st.form ('Evaluación 2'):
        primera=st.radio('1.-Lo siguiente se define como premisa......... Una proposición o declaración que forma la base de un argumento o conclusión. Es uno de los puntos de partida a partir de los cuales se extrae una inferencia lógica. Las premisas se presentan típicamente en pares o más, formando la base para un silogismo u otras formas de razonamiento- ',['Cierto','Falso'])
        segunda=st.radio('2.-Los argumentos que se basan en la generalización de información a partir de observaciones particulares. Por ejemplo el avistamiento de cisnes en Austria y Suiza sugieren que todos los gansos son blancos, se basan en el...',['Deductivismo','Induccionismo','Silogismo','Empirismo'])
        tercera=st.radio('3.-Durante esta fase del anteproyecto, intentamos exponer por que es relevante el tema que proponemos como objeto de estudio.',['Objetivos','Marco teórico','Justificación','Hipótesis'],)
        cuarta=st.radio('4.-La siguiente es la definición de ______________________: -Tendencia sistemática que distorsiona los resultados de un estudio o la interpretación de los datos',['Sesgo','Error sistemático','Fallos lógicos','Error de interpretación'])
        quinta=st.radio('5.-¿Quien fue quién ideó el método dialéctico',['Platón','Parmenides','Aristoteles','Sócrates'])
        sexta=st.radio('6.-El padre del método experimental fue...',['Descartes','Comte','Galileo','Einstein'])
        septima=st.radio('7.-La tendencia a buscar información que confirme nuestras percepciones es el sesgo de ________',['Contrataque','Encuadre','Congruencia','Confirmación'])
        octava=st.radio('8.-A qué parte del protocolo de investigación pertenece este fragmento de este artículo publicado en el hospital 450 de Durango',['Justificación', 'Objetivos','Hipótesis','Pregunta de investigación'])
        st.image('Imagenes/obj.png',300)
        novena=st.radio('9.-¿Qué parte del protocolo de investigación busca dar una respuesta temporal a la pregunta de investigación ? (Tip: Se formula en forma de proposición afirmativa)',['Hipótesis','Justificación','Objetivos','Pregunta de investigación'])
        decima=st.radio('10.-Dentro de las propuestas de Francis Bacon, uno de los postulados incluía las barreras psicológicas para el descubrimiento científico, a ¿cuál ídolo, corresponde lo siguiente?,-Tendencia a imponer preconcepciones en aspectos naturales-',['Ídolo de la tribu','Ídolo de la cueva','Ídolo del mercado','Ídolo del teatro'])
        enviar=st.form_submit_button('Enviar')

        if enviar==True:
            
            try:
                fecha_actual = datetime.datetime.now()

                insert_query = """
                            INSERT INTO evaluacionsegunda (primera, segunda, tercera, cuarta, quinta,sexta,septima, octava,novena,decima,tiempo,clave)
                            VALUES (%s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s)
                            """
                cursor.execute(insert_query, (primera, segunda, tercera, cuarta, quinta, sexta,septima,octava,novena,decima,fecha_actual,nombre))
                cursor.execute('DELETE FROM evaluacionsegunda')

    # Commit the changes and close the connection
                conn.commit()
                st.success('Enviado')
                st.balloons()
                conn.close()


            except:
                st.error('Error de captura')
