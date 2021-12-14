import streamlit as st

def internal():
    with st.sidebar:
        menu = st.radio('Acesso',['Login','Cadastro'])
    if menu == 'Login':
        colunaUm = st.columns((1, 1, 4, 1, 1))
        with colunaUm[2]:
            username = st.text_input('Usuário')
            senha = st.text_input('Senha', type='password')
            if st.button('Entrar'):
                st.success(f"Olá {username}!  Login efetuado com sucesso")
    else:
        pass