import streamlit as st

st.title("Calculadora IMC📱")
st.subheader("veja se seu peso esta bom teste!")
st.subheader("o app ainda esta em beta!")
altura = st.number_input("digite a sua altura",min_value = 0.0)
peso = st.number_input("digite o seu peso",min_value =0.0)

if st.button("calcular"):
    imc = peso / altura ** 2

    if imc < 18.5:
        st.warning("abaixo do peso")


    elif imc < 24.9:
        st.success("peso normal")

    elif imc < 29.9:
        st.warning("sobrepeso")

    elif imc < 34.9:
        st.warning("obesidade grau I")
    elif imc < 39.9:
        st.error("obesidade grau II")
    elif imc >= 40.:
        st.error("obesidade grau III ")
        
    
    else:(f"{st.error}erro digite numeros nao letras! ou tente novamente")
