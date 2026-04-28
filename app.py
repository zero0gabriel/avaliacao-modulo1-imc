import streamlit as st

st.title("Calculadora IMC📱")
st.subheader("veja se seu peso esta bom teste!")
st.subheader("o app ainda esta em beta!")
altura = st.number_input("digite a sua altura",min_value = 0.0)
peso = st.number_input("digite o seu peso",min_value =0.0)

if st.button("calcular"):
    imc = peso / altura ** 2

    if imc < 18.5:
        st.image("https://i.ytimg.com/vi/tZt1Q4biMZA/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgXihGMA8=&rs=AOn4CLBSd19AcHKMo0dxchT-sCStwOkDBg")
        st.warning("abaixo do peso")
        st.audio("https://www.myinstants.com/media/sounds/chaves-musica-triste.mp3", autoplay=True)


    elif imc < 24.9:
        st.image("https://i.pinimg.com/originals/d5/12/a4/d512a43ce2abd626abf9d0142b10d9c9.jpg")
        st.success("peso normal")
        st.audio("https://www.myinstants.com/media/sounds/xuxa-parabens-da-xuxa.mp3", autoplay = True)

    elif imc < 29.9:
        st.image("https://th.bing.com/th/id/OIP.6OQZkAs2_9A6IcHlmxmolAHaLH?w=129&h=192&c=7&r=0&o=5&pid=1.7")
        st.warning("sobrepeso")
        st.audio("https://www.myinstants.com/media/sounds/auraa.mp3", autoplay= True)

    elif imc < 34.9:
        st.image("https://th.bing.com/th/id/OIP.bkA4uOD-rkPn-ow75qDHYAHaE8?w=276&h=184&c=7&r=0&o=5&pid=1.7")
        st.warning("obesidade grau I")
        st.audio("https://www.myinstants.com/media/sounds/alarme-incendie.mp3", autoplay = True)
    elif imc < 39.9:
        st.image("https://th.bing.com/th/id/OIP.AHvmycxrXMZu7zH8eFpXtAHaDQ?w=339&h=154&c=7&r=0&o=5&pid=1.7")
        st.error("obesidade grau II")
        st.audio("https://www.myinstants.com/media/sounds/alarme-incendie.mp3",autoplay = True)
    elif imc >= 40.:
        st.image("https://th.bing.com/th/id/OIP.qaWSVjmZCY3mYD4HQvEyiQHaDZ?w=350&h=160&c=7&r=0&o=5&pid=1.7")
        st.error("obesidade grau III (procure ajuda imediatamente)")
        st.audio("https://www.myinstants.com/media/sounds/alarme-incendie.mp3",autoplay = True)
        
    
    else:(f"{st.error}erro digite numeros nao letras! ou tente novamente")