import streamlit as st 
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from streamlit_gsheets import GSheetsConnection

conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
#Base de datos
