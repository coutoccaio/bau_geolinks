import streamlit as st
import leafmap.foliumap as leafmap
from owslib.wfs import WebFeatureService
from PIL import Image


def principal():
    st.title('Serviços Externos')
    st.subheader( """Nessa página você tem acesso aos geoserviços que podem ser utilizados por qualquer usuário interessado.""")
    colunaUm = st.columns((1, 1, 4, 1, 1))
    with colunaUm[2]:
        st.title(' ')
        st.title(' ')
        st.title(' ')
        st.markdown("<h1 style='text-align: center; color: #FF7D33;'>Selecione na lista ao lado a categoria que deseja acessar</h1>",
                    unsafe_allow_html=True)
        st.title(' ')

def ortofotos():
    st.title('Ortofotos')
    st.subheader("""Selecione ao lado o ano das fotos""")
    with st.sidebar:
        orto = st.selectbox('Ano:', ['2006','2010','2017', '2017 WMTS'])
    if orto == '2006':
        st.subheader("""Ortofotos do ano de 2006""")
        m = leafmap.Map(
            center = [-12.85,-38.43],
            zoom = 11,
            tiles="stamentoner")
        url = 'https://geo.salvador.ba.gov.br/imageserver/services/Ortofotos/Ortofotos_2006_Ref_/ImageServer/WMSServer'
        m.add_wms_layer(url=url, layers='0', name='Ortofotos 2006', format='image/png', shown=True)
        with st.expander("Link acesso ao serviço WMS:"):
            st.markdown(f"<h5 style='text-align: left; color: red;'>{url}</h5>",
                            unsafe_allow_html=True)
        m.to_streamlit(600,600)
    elif orto == '2010':
        st.subheader("""Ortofotos do ano de 2010""")
        m = leafmap.Map(
            center=[-12.85, -38.43],
            zoom=11,
            tiles="stamentoner")
        url = 'https://geo.salvador.ba.gov.br/imageserver/services/Ortofotos/Ortofotos_2010_Ref_/ImageServer/WMSServer'
        m.add_wms_layer(url=url, layers='0', name='Ortofotos 2010', format='image/png', shown=True)
        with st.expander("Link acesso ao serviço WMS:"):
            st.markdown(f"<h5 style='text-align: left; color: red;'>{url}</h5>",
                            unsafe_allow_html=True)
        m.to_streamlit(600, 600)

    elif orto == '2017':
        st.subheader("""Ortofotos do ano de 2017""")
        m = leafmap.Map(
            center=[-12.85, -38.43],
            zoom=11,
            tiles="stamentoner")
        url = 'https://geo.salvador.ba.gov.br/imageserver/services/Ortofotos/Ortofotos_2017/ImageServer/WMSServer'
        m.add_wms_layer(url=url, layers='0', name='Ortofotos 2017', format='image/png', shown=True)
        with st.expander("Link acesso ao serviço WMS:"):
            st.markdown(f"<h5 style='text-align: left; color: red;'>{url}</h5>",
                            unsafe_allow_html=True)
        m.to_streamlit(600, 600)

def limites():
    st.title('Limites Adminitrativos')
    st.subheader("""Selecione ao lado o serviço que você deseja acessar""")
    servicos = ['http://geoserver.sedur.salvador.ba.gov.br:8080/geoserver/bairro_oficial/ows?SERVICE=WFS&REQUEST=GetCapabilities','http://geoserver.sedur.salvador.ba.gov.br:8080/geoserver/pddu_prefeitura_bairro/ows?','http://geoserver.sedur.salvador.ba.gov.br:8080/geoserver/apcp_centro_antigo/ows?SERVICE=WFS&REQUEST=GetCapabilities']
    categorias = ['Bairros','Prefeitura Bairro','Projeto Revitalizar']
    with st.sidebar:
        adm = st.selectbox('Serviço:', categorias)
    for index, categoria in enumerate(categorias):
        if adm == categoria:
            wfs11 = WebFeatureService(url=servicos[index], version='1.1.0')
            featureTypes = list(wfs11.contents)
            camadas = []
            for i in featureTypes:
                response = wfs11[i].title
                camadas.append(response)
            st.title(adm)
            st.markdown("<h4 style='text-align: left; color: white;'>Serviço</h4>",
                        unsafe_allow_html=True)
            with st.expander("Link acesso ao serviço WFS:"):
                st.markdown(f"<h5 style='text-align: left; color: red;'>{servicos[index]}</h5>",
                            unsafe_allow_html=True)
            st.markdown(f"<h5 style='text-align: left; color: #B6B6B6;'>Escolha abaixo a camada que deseja visualizar.</h5>",
                        unsafe_allow_html=True)
            cam = st.selectbox('Camadas nessa categoria:', camadas)
            for camada in camadas:
                if cam == camada:
                    imagemUm = Image.open(
                        f'G:/Meu Drive/Mestrados/Desenvolvimento de Aplicações Geoespaciais - UFPR/trabalho_final/Site/SEDUR/{camada}1.png')
                    st.image(imagemUm)
            st.text("""A biblioteca leafmap utilizada nesse site não suporta a inserção de Serviços WFS.
    A imagem acima foi utilizada para representar o serviço escolhido enquanto essa funcionalidade está sendo desenvolvida.
    Sinta-se a vontade para copiar o link do serviço e inserir no programa de geoprocessamento de sua preferência""")

def cartografia():
    servicos = ['http://mapeamento.salvador.ba.gov.br/enc', 'http://mapeamento.salvador.ba.gov.br/rel',
                'http://mapeamento.salvador.ba.gov.br/hid', 'http://mapeamento.salvador.ba.gov.br/tra',
                'http://mapeamento.salvador.ba.gov.br/aer', 'http://mapeamento.salvador.ba.gov.br/dut',
                'http://mapeamento.salvador.ba.gov.br/fer', 'http://mapeamento.salvador.ba.gov.br/ver',
                'http://mapeamento.salvador.ba.gov.br/hdv',
                'http://mapeamento.salvador.ba.gov.br/cbge', 'http://mapeamento.salvador.ba.gov.br/edf',
                'http://mapeamento.salvador.ba.gov.br/emu', 'http://mapeamento.salvador.ba.gov.br/laz']
    categorias = ['Energia e Comunicações',
 'Relevo',
 'Hidrografia',
 'Sistema de Transporte',
 'Sistema de Transporte Aeroportuario',
 'Sistema de Transporte Dutos',
 'Sistema de Transporte Ferroviário',
 'Área Verde',
 'Sistema de Transporte Hidroviário',
 'CBGE',
 'Edificação',
 'Estrutura de Mobilidade Urbana',
 'Cultura e Lazer']

    with st.sidebar:
        adm = st.selectbox('Categorias:', categorias)

    for index, categoria in enumerate(categorias):
        if adm == categoria:
            wfs11 = WebFeatureService(url=servicos[index], version='1.1.0')
            featureTypes = list(wfs11.contents)
            camadas = []
            for i in featureTypes:
                response = wfs11[i].title
                camadas.append(response)
            st.title(adm)
            st.markdown("<h4 style='text-align: left; color: white;'>Serviço</h4>",
                        unsafe_allow_html=True)
            with st.expander("Link acesso ao serviço WFS:"):
                st.markdown(f"<h5 style='text-align: left; color: red;'>{servicos[index]}</h5>",
                            unsafe_allow_html=True)
            st.subheader('''Escolha abaixo a camada que deseja visualizar.''')
            cam = st.selectbox('Camadas nessa categoria:', camadas)
            for camada in camadas:
                 if cam == camada:
                     colunaUm = st.columns((1, 2, 1, 2, 1))
                     imagemUm = Image.open(f'G:/Meu Drive/Mestrados/Desenvolvimento de Aplicações Geoespaciais - UFPR/trabalho_final/Site/Escala 1/{camada}1.png')
                     st.image(imagemUm)
                     imagemDois = Image.open(
                             f'G:/Meu Drive/Mestrados/Desenvolvimento de Aplicações Geoespaciais - UFPR/trabalho_final/Site/Escala 2/{camada}2.png')
                     st.image(imagemDois)
            st.text("""A biblioteca leafmap utilizada nesse site não suporta a inserção de Serviços WFS.
 A imagem acima foi utilizada para representar o serviço escolhido enquanto essa funcionalidade está sendo desenvolvida.
 Sinta-se a vontade para copiar o link do serviço e inserir no programa de geoprocessamento de sua preferência""")

def defesaCivil():
    servicos = ['http://mapa.salvador.ba.gov.br:8080/geoserver/MAPA/ows']
    categorias = ['Serviço da CODESAL']

    with st.sidebar:
        adm = st.selectbox('Categorias:', categorias)

    for index, categoria in enumerate(categorias):
        if adm == categoria:
            wfs11 = WebFeatureService(url=servicos[index], version='1.1.0')
            featureTypes = list(wfs11.contents)
            camadas = []
            for i in featureTypes:
                response = wfs11[i].title
                camadas.append(response)
            st.title(adm)
            st.markdown("<h4 style='text-align: left; color: white;'>Serviço</h4>",
                        unsafe_allow_html=True)
            st.markdown(f"<h5 style='text-align: left; color: red;'>{servicos[index]}</h5>",
                        unsafe_allow_html=True)
            st.subheader('''Escolha abaixo a camada que deseja visualizar.''')
            cam = st.selectbox('Camadas nessa categoria:', camadas)
            for camada in camadas:
                if cam == camada:
                    imagemUm = Image.open(
                        f'G:/Meu Drive/Mestrados/Desenvolvimento de Aplicações Geoespaciais - UFPR/trabalho_final/Site/CODESAL/{camada}1.png')
                    st.image(imagemUm)
            st.text("""A biblioteca leafmap utilizada nesse site não suporta a inserção de Serviços WFS.
     A imagem acima foi utilizada para representar o serviço escolhido enquanto essa funcionalidade está sendo desenvolvida.
     Sinta-se a vontade para copiar o link do serviço e inserir no programa de geoprocessamento de sua preferência""")

def categorias():
    with st.sidebar:
        categ = st.radio('Categorias', ['Principal', 'Ortofotos', 'Limites', 'Cartografia Restituida', 'Defesa Civil'])

    if categ == 'Principal':
        principal()

    elif categ == 'Ortofotos':
        ortofotos()

    elif categ == 'Limites':
        limites()

    elif categ == 'Cartografia Restituida':
        cartografia()

    elif categ == 'Defesa Civil':
        defesaCivil()
