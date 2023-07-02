import streamlit as st
import requests
import sqlite3
import pandas as pd

#
# Side bar menu


menu_option = st.sidebar.radio("Menu", ["Requisição de Frete", "Requisição x Entradas"])


if menu_option == "Requisição de Frete":
    
    exec(open("frete_request.py").read())

# Resto do seu código...
if menu_option == "Requisição x Entradas":
    exec(open("visualizador_frete.py").read())
 
        