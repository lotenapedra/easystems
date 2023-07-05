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
def tela_login():
    st.title("Acesso Solicitante Frete")
    usuario = st.text_input("Usuario")
    senha = st.text_input("Senha", type="password")
    if st.button("Login"):
        resultado = verifica_login(usuario, senha)
        if resultado:
            st.success("Login realizado com sucesso!")
            # Abra o arquivo main.py em um novo navegador
            webbrowser.open_new("https://easystems-0ixw0ptprokl.streamlit.app")
            # Encerre o aplicativo atual para evitar conflitos entre os servidores do Streamlit
            raise SystemExit
        else:
            st.error("Credenciais inválidas!")

# Executa a tela de login
tela_login()
