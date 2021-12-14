import streamlit as st
from PIL import Image

def team():
    colunaUm = st.columns((1,2,1,2,1,2,1))
    with colunaUm[1]:
        imagemUm= Image.open('1.png')
        st.image(imagemUm)
        st.markdown("<h4 style='text-align: center; color: white;'>Cainho</h4>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center; color: gray;'>Mascote</h5>", unsafe_allow_html=True)

    with colunaUm[3]:
        imagemDois = Image.open('2.png')
        st.image(imagemDois)
        st.markdown("<h4 style='text-align: center; color: white;'>Caio Couto</h4>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center; color: gray;'>CEO</h5>", unsafe_allow_html=True)

    with colunaUm[5]:
        imagemTres = Image.open('3.png')
        st.image(imagemTres)
        st.markdown("<h4 style='text-align: center; color: white;'>Caião</h4>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center; color: gray;'>Desenvolvedor</h5>", unsafe_allow_html=True)


def contact():
    st.markdown("<h5 style='text-align: left; color: #3399ff;'>Entre em contato conosco</h5>",
                unsafe_allow_html=True)
    nome = st.text_input('Insira seu Nome')
    contato = st.text_input('Email para contato', 'exemplo@exemplo.com')
    servico = st.text_area('Digite aqui sua dúvida ou sugestão')
