import streamlit as st
from main import *

lista_racas = ['beast', 'dragon', 'humanoid', 'monstrosity', 'fiend', 'undead',
       'elemental', 'giant', 'swarm of tiny beasts', 'construct', 'plant',
       'celestial', 'fey', 'aberration', 'ooze', 'Fiend']

lista_tamanho = ['Medium', 'Large', 'Huge', 'Tiny', 'Small', 'Gargantuan']

lista_alinhamento = ['Unaligned', 'Chaotic Evil', 'Lawful Evil', 'Neutral Evil',
       'Lawful Good', 'Chaotic Good', 'Neutral Good', 'True Neutral']
lista_genero = ['male','female','Undefined']


st.title('Gerador de monstros de RPG')

nome_select = st.text_input('Nome')
raca_select = st.selectbox('Raças', lista_racas)
tamanho_select = st.selectbox('Tamanhos', lista_tamanho)
alinhamento_select = st.selectbox('Alinhamento', lista_alinhamento)
genero_select = st.selectbox('Genero', lista_genero)
api_key = st.text_input('API Key')


if st.button('Gerar monstro'):
    gerador = GeradorMonstro(api_key = api_key)
    gerador.montar_prompt(nome_input = nome_select,
                        raca_input = raca_select,
                        tamanho_input = tamanho_select,
                        alinhamento_input = alinhamento_select,
                        genero_input = genero_select)

    st.markdown(gerador.gerar_descricao())
    st.markdown(gerador.gerar_imagem())
    #st.markdown(gerador.gerar_resposta())
