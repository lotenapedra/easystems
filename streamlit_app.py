import streamlit as st
import requests
import sqlite3
import pandas as pd


st.set_page_config(page_title='easystems',page_icon='caixa-aberta.png')

#
# Side bar menu
menu_option = st.sidebar.radio("Menu", ["Entrada", "Excluir Entrada","Visualizações","Requisição de Frete","mapa"])

if menu_option == "Entrada":
    exec(open("entrada.py").read())

if menu_option == "Cadastros":
    st.write("")
# Resto do seu código...
if menu_option == "Excluir Entrada":
    exec(open("editar_excluir.py").read())
    
if menu_option == "Visualizações":
    exec(open("visualizacao.py").read())
    
if menu_option == "Requisição de Frete":
   exec(open("valid_user_frete.py").read())
    
if menu_option == "mapa":
    exec(open("maps.py").read())
        

if menu_option == "Cadastros":
    st.write("")
