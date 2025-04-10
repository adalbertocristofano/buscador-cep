import streamlit as st
import requests 

def busca_cep(cep):
    resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    return resposta

st.set_page_config(
    page_title='Busca CEP',
    page_icon='💌'
)

st.title('Sitema de busca de CEP')
st.divider()
menu = st.sidebar
cep = menu.text_input("Digite o CEP:")
botao = menu.button('Pesquisar')

if botao:
    resposta = busca_cep(cep)

    if resposta.status_code == 200:
        st.success('CEP encontrato com sucesso!', icon='✔')
        dados = resposta.json()

        col1, col2 = st.columns(2)

        col1.markdown(f"**CEP:** {dados['cep']}")
        col1.markdown(f"**Logradouro:** {dados['logradouro']}")
        col1.markdown(f"**Complemento:** {dados['complemento']}")
        col1.markdown(f"**Unidade:** {dados['unidade']}")
        col1.markdown(f"**Bairro:** {dados['bairro']}")
        col1.markdown(f"**Localidade:** {dados['localidade']}")
        col1.markdown(f"**UF:** {dados['uf']}")
        col2.markdown(f"**Estado:** {dados['estado']}")
        col2.markdown(f"**Regiao:** {dados['regiao']}")
        col2.markdown(f"**Ibge:** {dados['ibge']}")
        col2.markdown(f"**Gia:** {dados['gia']}")
        col2.markdown(f"**DDD:** {dados['ddd']}")
        col2.markdown(f"**Siafi:** {dados['siafi']}")
        st.balloons()
    else:
        st.error('O CEP informado é inválido', icon='❌')     