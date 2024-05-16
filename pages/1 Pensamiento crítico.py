import streamlit as st 
import pandas as pd 


st.sidebar.caption('By Baja Caltec')

Desactivar=False
#from streamlit_lottie import st_lottie
contra = st.sidebar.text_input('Contraseña', type='password')
falcho=False
ingresar=st.sidebar.toggle('Ingresar',disabled=Desactivar)

st.sidebar.caption('El conteo de 10 minutos inicia al hacer click en ingresar')
usuarios = ('2089', '234')

if ingresar ==True and contra in usuarios:
    st.title('Pensamiento crítico') 
    tab1,tab2,tab3=st.tabs(['Pensamiento crítico','Historía','Tipos de ciencia'])
    with tab1:
        st.title('¿Qué es el pensamiento crítico?')
