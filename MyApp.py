import streamlit as st
st.title("Mi primer app")
#st.button("Dale click")
#st.button("otro boton")
import pandas as pd

#Las siguintes lineas de cogido eran para visualizar
#df = pd.read_csv('https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv')

#st.write(df)

#Agregue una ecuacion y una vinieta
#st.map(df)
#st.text("Hola mundo")
#st.text("La siguiente es una integral")
#st.latex("\int_1^6sin(x)dx")
#st.markdown("Esta es una vinieta")

Click=st.button("Dale Click")
st.write("El valor de cilck es",Click)

if Click==True:
    st.image("Luffy.jpg")