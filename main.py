import streamlit as st
import requests
import sqlite3
import pandas as pd

#
# Side bar menu
menu_option = st.sidebar.radio("Menu", ["Entrada", "Excluir Entrada","Visualizações","Requisição de Frete","Visualizar Requisicao"])

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
   exec(open("frete_request.py").read())
    
if menu_option == "Visualizar Requisicao":
    exec(open("visualizador_frete.py").read())
        

if menu_option == "Cadastros":
    st.write("")