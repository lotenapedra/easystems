import sqlite3
import streamlit as st
import subprocess
import webbrowser

# Função para verificar as credenciais de login
def verifica_login(usuario, senha):
    conn = sqlite3.connect('novo.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE user = ? AND senha = ?", (usuario, senha))
    resultado = cursor.fetchone()
    conn.close()
    return resultado

# Tela de login

import streamlit as st
import webbrowser

def tela_login():
    st.title("Acesso Solicitante Frete")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Login"):
        resultado = verifica_login(usuario, senha)
        if resultado:
            st.success("Login realizado com sucesso!")
            abrir_url("https://easystems-0ixw0ptprokl.streamlit.app/")
        else:
            st.error("Credenciais inválidas!")

def verifica_login(usuario, senha):
    # Implemente a lógica de verificação de login aqui
    # Retorne True se as credenciais forem válidas, caso contrário, retorne False
    return True  # Altere conforme sua lógica de verificação

def abrir_url(url):
    webbrowser.open_new_tab(url)

tela_login()
Neste código, ao clicar no botão "Login" e ter as credenciais corretas, a função abrir_url será chamada para abrir o URL especificado em um navegador externo. Tenha em mente que isso abrirá uma nova janela ou guia no navegador padrão do usuário.

