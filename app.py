import streamlit as st
from langchain import LLM, OpenAI
from requests import get
from requests.exceptions import RequestException

# Initialisation de LangChain avec votre clé API
llm = LLM(adapter=OpenAI(api_key="ls__4990ccb7acf54b28bb753b3e81eec81d"))

def fetch_page_content(url):
    try:
        response = get(url)
        response.raise_for_status()
        return response.text
    except RequestException:
        return "Erreur lors de la récupération du contenu de la page."

def semantic_similarity(text1, text2):
    return llm.semantic_similarity(text1, text2)

# Interface utilisateur
st.title('Analyseur de proximité sémantique')
url1 = st.text_input('Entrez l\'URL de la première page:')
url2 = st.text_input('Entrez l\'URL de la deuxième page:')

if st.button('Analyser'):
    if url1 and url2:
        content1 = fetch_page_content(url1)
        content2 = fetch_page_content(url2)
        similarity = semantic_similarity(content1, content2)
        st.write(f'La proximité sémantique entre les deux pages est de: {similarity}')
    else:
        st.error('Veuillez entrer des URL valides pour les deux pages.')

