import streamlit as st
from PIL import Image
import smtplib
import ssl

def principal():
    colunaUm = st.columns((1,1,10,1,1))
    with colunaUm[2]:
        st.title('Baú de Geolinks')
        st.subheader(
            '''Esse site foi desenvolvido para agregar os serviços geoespaciais que disponibilizem dados da cidade de Salvador.''')
        st.title(' ')
        st.markdown("<h5 style='text-align: right; color: #3399ff;'>TUTORIAL DE USO DA PLATAFORMA</h5>", unsafe_allow_html=True)
        # image = Image.open('D:/Caio/Drive/Mestrados/Desenvolvimento de Aplicações Geoespaciais - UFPR/trabalho_final/thumb.png')
        st.video('https://www.youtube.com/watch?v=c9pnTc32hhU')
        st.title(' ')

    colunaDois = st.columns((1,1,4,1,1))
    with colunaDois[2]:
        st.markdown("<h5 style='text-align: right; color: #3399ff;'>CADASTRO DE NOVOS SERVIÇOS</h5>",
                unsafe_allow_html=True)
        st.markdown("<h7 style='text-align: right; color: #808080;'>Envie novos serviços para a nossa equipe."
                    " Assim que validados, serão inseridos no site.</h7>",
                    unsafe_allow_html=True)
        nome = st.text_input('Insira seu Nome')
        contato = st.text_input('Email para contato', 'exemplo@exemplo.com')
        servico = st.text_input('Nome do Serviço')
        link = st.text_input('Insira o endereço do serviço')
        message = f"Subject:{servico}\n\nOlá, meu nome é{nome}, quero incluir o serviço do link a seguir: {link}".encode('utf-8')
        if st.button('Enviar'):
            from_adress = "coutoccaio@gmail.com"
            password = '**'
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server:
                server.login(from_adress, password)
                server.sendmail(
                    from_adress,
                    from_adress,
                    message
                )
                st.success("O serviço {} foi enviado".format(servico))
