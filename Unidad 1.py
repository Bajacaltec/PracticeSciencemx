import streamlit as st 
import pandas as pd 
import streamlit.components.v1 as components
import openpyxl
import psycopg2
from streamlit_lottie import st_lottie as stl

#Base de datos
conn = psycopg2.connect(
                        host="dpg-cokdc7gl5elc73c3klp0-a.oregon-postgres.render.com",
                        database="bajacaltec_ciencia",
                        user="bajacaltec_ciencia_user",
                        password="QnVGnpcQGxEr7q9W3YDiPS4ABxSTkAVn"
                    )


st.sidebar.caption('By Baja Caltec')

Desactivar=False
usuario=st.sidebar.text_input('Usuario')
#from streamlit_lottie import st_lottie
contra = st.sidebar.text_input('Contraseña', type='password')
falcho=False
ingresar=st.sidebar.toggle('Ingresar',disabled=Desactivar)

usuarios = ('2089', '234')
#key=st.sidebar.text_input('Poner API key gemini')

if ingresar ==True and contra in usuarios:
    st.subheader('Metodología de la investigación I')
    tab1,tab2,tab3,tab4,tab5=st.tabs(['Presentación','Encuesta','Historía de la ciencia','Pensamiento crítico','Idea de investigación'])
    with tab1:
        st.subheader('Docentes')
        col1,col2=st.columns(2)
        with col1:
            st.image('Imagenes/Foto alonso.PNG',width=100)
            st.markdown('')
            st.caption('Dr. Fernando A. Núñez Moreno')
            st.caption('Cirujano General, MSc y doctorando por la universidad de Oldenburg')
        
        with col2:
            st.image('data:image/jpeg;base64,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',width=200)
            st.caption('Dr. Edgar Santos Marcial')
            st.caption('Neurocirujano, Dr. Med, MSc, SNI III  ')
        st.markdown('_____')
        st.subheader('AG Santos, laboratorio de neurofisiología vascular')
        sol1,sol2=st.columns(2)
        with sol1:
            st.image('https://newzealandfresh.sg/cdn/shop/files/Pigs-Brains_1024x1024.jpg?v=1704417949')
            st.caption('Cerebro girencefálico porcino')
        with sol2:
            st.image('https://www.researchgate.net/publication/231861205/figure/fig1/AS:214208277946396@1428082641915/Image-of-a-representative-rat-brain-showing-a-focal-ischemic-lesion-within-the-right.png')
            st.caption('Cerebro lisencefálico murino')
        st.image('Imagenes/kartoonpig.jpg')
        st.caption('Grabación multiespectral a traves de craneotomía posterior a la oclusión de la arteria cerebral media vía transorbital')
        st.image('https://upload.wikimedia.org/wikipedia/commons/b/b3/Santos_E_et_al_Neuroimage_2014_.gif',width=705)
        st.caption('Visualización multiespectral de una CSD (Cortical spreading depresion) en un modelo porcino, Dr. Santos')
        with st.expander('Ejes del curso'):
            sol1,sol2,sol3=st.columns(3)
            with sol1:
                st.info('Teoría')
                st.write('Temario institucional')
                st.write('Teoría del desarollo de un anteproyecto')
            with sol2:
                st.info('Pensamiento crítico')
                st.write('Características del pensamiento crítico')
                st.write('Barreras del pensamiento crítico')
                st.write('Conceptos de lógica básica')
                st.write('Fallas lógicas')
                st.write('Razonamiento inductivo')
                st.write('Ciencia y pseudociencia')
            with sol3:
                st.info('Anteproyecto')
                st.write('Elaboración de un anteproyecto de investigación')
        with st.expander('Temario'):
            df_tem={'Tema':['Historía de la ciencia']}
            df_temario=pd.read_excel('xlsx/Temario.xlsx')
            st.dataframe(df_temario,hide_index=True)
        with st.expander('Calificación'):
            df_calif=pd.read_excel('xlsx/Calificación df.xlsx',sheet_name='Sheet1')
            st.dataframe(df_calif,hide_index=True,width=600)
            df_crit=pd.read_excel('xlsx/Calificación df.xlsx',sheet_name='Sheet2')
            st.dataframe(df_crit,hide_index=True)
        st.subheader('Curva de aprendizaje y olvido')
        yol1,yol2=st.columns(2)
        with yol1:
            st.image('data:image/jpeg;base64,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4zobF+YzADPVYyQ/P6bDibvMmYm4/wCm4xf4uvaXld+mmwJtcPxM3WHTCAcIFuzDa3Uo/IYs16lU1XzXfnu3gz6RLu7YcfD0cVhjtbhixJD9XgzVOHGbrZoqvQQEBAQEBAQEBAQEBB+oeRep9bh9274rw142e2jO55F6n1uH3bvimvGxozueRep9bh9275k142NGdzyL1PrcPu3fFNeNjRnc8i9T63D7t3zJrxsaM7nkXqfW4fdu+ZNeNjRnc8i9T63D7t3zJrxsaM7nkXqfW4fdu+Ka8bGjO55F6n1uH3bvmTXjY0Z3PIvU+tw+7d8U142NGdzyL1PrcPu3fFNeNjRnc8i9T63D7t3zJrxsaM7nkXqfW4fdu+ZNeNjRnc8i9T63D7t3zJrxsaM7nkXqfW4fdu+Ka8bGjO55F6n1uH3bvimvGxozunkXqPW4fdu+ZNeNjRnc8i1R63D7t3xTXjY0Z3XyL1PrcPu3fMmvGxozu2Y/0UbQazdt2iGx6YAJA23VbFkM9E142Z8NF78r+jV8i9T63D7t3zJrxs1oTueRep9bh9275k142NGdzyL1PrcPu3fMmvGxozueRep9bh9275k142NGdzyL1PrcPu3fMmvGxozueRep9bh9275k142NGdzyL1PrcPu3fMmvGxozueRep9bh9275k142NGdzyL1PrcPu3fMmvGxozueRep9bh9275k142NGdzyL1PrcPu3fMmvGxozueRep9bh9275k142NGdzyL1PrcPu3fMmvGxozueRep9bh9275k142NGd37QuZ0CAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIP//Z')
        with yol2:
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSJR9ovYgt7rPBfwWlDetGz9pkBsjgrGNxzg&s')
        
    with tab2:
        with st.form('Datos anónimos'):

            col1,col2=st.columns(2)

            with col1:
                    st.title('Encuesta')
                    edad=st.number_input('Edad',step=1)
                    género=st.radio('Género',['Femenino','Masculino'])
                    aborto=st.selectbox('¿Estás a favor o en contra del aborto?',['A favor','En contra'])
                    pena=st.selectbox('¿Estarías a favor de la pena de muerte en México en el caso de narcotraficantes?',['Si','No'])
                    qx1=st.selectbox('¿Qué consideras que es lo más importante para evitar infecciones en el quirófano',['Lavado de manos','Botas qurúrgicas','Mantener técnica esteril','Lavado de instrumental'])
                    qx2=st.selectbox('¿Estas de acuerdo con la siguiente oración?:El uso de cepillos quirúrgicos es necesario para un correcto lavado quirúrgico de manos',['Si','No'])
            with col2:
                    prob=st.selectbox('¿Crees que es más peligroso lanzarse de un paracaidas qué estar hospitalizado?',['Si','No'])
                    saber1=st.selectbox('¿Sabes por que el cielo es de color azul?',['Si','No','No sé'])
                    saber2=st.radio('Sabes por que suceden las mareas y su relación con la luna?',['Si','No'])
                    st.text_input('Si tu, respuesta es afirmativa, explica ¿por que?')
                    protocolo=st.selectbox('Si, tuvieras la oportunidad de hacer un proyecto de investigación, en cual de las siguientes áreas te gustaría realizarlo?',['Neurocirugía','Cirugía general','Urología','Manejo de la sala quirúrgica'])
                    bot_enviar=st.form_submit_button('Enviar')
                    # Conectarse a la base de datos Postgres
                    

                    # Crear un cursor para ejecutar sentencias SQL
                    cursor = conn.cursor()

                    # Insertar datos en la tabla
                    if bot_enviar:
                        creat='''CREATE TABLE IF NOT EXISTS encuestas (
                        id SERIAL PRIMARY KEY,
                        edad INTEGER NOT NULL,
                        genero VARCHAR(255) NOT NULL,
                        aborto VARCHAR(255) NOT NULL,
                        pena_muerte VARCHAR(255) NOT NULL,
                        qx1 VARCHAR(255) NOT NULL,
                        qx2 VARCHAR(255) NOT NULL,
                        paracaidas VARCHAR(255) NOT NULL,
                        saber1 VARCHAR(255) NOT NULL,
                        saber2 VARCHAR(255) NOT NULL,
                        saber2_explicacion TEXT,
                        protocolo VARCHAR(255) NOT NULL
                            )
                            '''
                        cursor.execute(creat)
                        cursor.execute("""
                            INSERT INTO encuestas (
                                edad, genero, aborto, pena_muerte, qx1, qx2, paracaidas, saber1, saber2, protocolo
                            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """, (
                            edad,
                            género,
                            aborto,
                            pena,
                            qx1,
                            qx2,
                            prob,
                            saber1,
                            saber2,
                            protocolo
                        ))

                        # Guardar los cambios en la base de datos
                        conn.commit()

                        # Mostrar un mensaje de confirmación
                        st.success("¡Datos enviados correctamente!")

                    # Cerrar la conexión a la base de datos
                    conn.close()
                        
    with tab3:
        st.video('https://www.youtube.com/watch?v=ZlgXh_sXm7M')
        st.title('Historía del pensamiento científico')        
        components.iframe('https://docs.google.com/presentation/d/e/2PACX-1vSe3Fg2NFEl6VES9qmoS4vnmgEp7GTjCYrSH22k9m1afpOcgF2hWv6LKe25I8vQYZq6aRQP3xkQMnSP/embed?start=false&loop=false&delayms=3000',height=500)
    with tab5:
        col1,col2,col3=st.columns([2,2,2])

        with col1:
            st.subheader('¿Como encontrar ideas para una investigación?')
            with col2:
                st.info("""Explorar tus intereses y áreas de conocimiento""")
                st.success('¿Qué temas te apasionan? ¿En qué áreas tienes experiencia o conocimiento previo?')
            with col3:
                st.info('')
                    
        with st.expander('Bases de datos'):
            st.text('Google Scholar')  
            st.markdown('https://scholar.google.com')
            st.text('Pubmed') 
            st.markdown('https://pubmed.ncbi.nlm.nih.gov')
            st.text('ELICIT')
            st.markdown('https://elicit.com/notebook/ddba5f35-e4c9-46f1-bb45-01f3da9d2762')
            with st.popover("Open popover"):
                st.markdown("Hello World 👋")
                name = st.text_input("What's your name?")


#Analizar problemas y necesidades: Observa tu entorno social, profesional o comunitario. ¿Qué problemas o necesidades puedes identificar que podrían ser objeto de investigación? ¿Cómo tu investigación podría contribuir a solucionarlos o mejorar la situación actual?

#Consultar con expertos: Dialoga con profesores, investigadores y profesionales en tu área de interés. Solicita su orientación, sugerencias y recomendaciones sobre posibles temas de investigación. Aprovecha su experiencia y conocimiento para afinar tus ideas.""")
        with st.expander('Viablidad'):
            st.subheader('Viabilidad del proyecto')
            viab_lottie='https://lottie.host/a0082b22-a44d-4f3d-a2a9-300bfc8c0a97/EU2v6Zvwgw.json'
            stl(viab_lottie,width=600)
            st.info('Evalúa si el tema elegido es viable en términos de tiempo, recursos y acceso a información. Asegúrate de que puedas recopilar datos suficientes y de calidad para realizar una investigación rigurosa y completa')
        with st.expander('Pregunta de investigación'):
            st.subheader('Definir preguntas de investigación')
            st.info('Una vez elegido el tema, formula preguntas de investigación claras, precisas y relevantes que guíen tu trabajo. Las preguntas deben ser factibles de responder y contribuir al conocimiento en el área.')
    with tab4:
        st.subheader('¿Qué es el pensamiento crítico?')       
        components.iframe('https://docs.google.com/presentation/d/e/2PACX-1vQs9c5f3qfakSGVgActoNc7Dfth3J6Fpk4z7LTQwcGgLCvpcvfpqHzZRh8C8F6X9Mv9lUlaX_y-qjXv/embed?start=false&loop=false&delayms=3000',height=500)

