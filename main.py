import streamlit as st
from home import principal
from team import team, contact
from external import categorias
from internal import internal
from teste import teste

PAGE_CONFIG = {"page_title":"Baú de Geolinks","page_icon":"chart_with_upwards_trend","layout":"wide"}
st.set_page_config(**PAGE_CONFIG)

menu = ["Pagina Principal", "Serviços Externos", "Serviços Internos", "Equipe e Contato", "Teste"]
choice = st.sidebar.selectbox("Menu Principal", menu)

if choice == "Pagina Principal":
    principal()
elif choice == "Serviços Internos":
    internal()
elif choice == "Serviços Externos":
    categorias()
elif choice == "Teste":
    st.text('Em desenvolvimento')
else:
    team()
    contact()

