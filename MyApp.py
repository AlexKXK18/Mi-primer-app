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

num1 = st.slider('Elige el numero 1', 0.0, 100.0, 25.0)
num2 = st.slider('Elige el numero 2', 0.0, 100.0, 25.0)
suma = num1+num2
st.write("La suma de", num1,"y",num2,"es:",suma)


st.write("Ahora multipliqumeos")
nn1 = st.number_input("dame n1")
nn2 = st.number_input("dame n2")

mult=nn1(nn2)
st.write("la multiplicacion de",nn1 "y", nn2, "es:",mult)