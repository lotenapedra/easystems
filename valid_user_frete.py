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
usuario = st.text_input("Usuário")
senha = st.text_input("Senha", type="password")
if st.button("Login"):
resultado = verifica_login(usuario, senha)
if resultado:
st.success("Login realizado com sucesso!")
st.markdown("[Clique aqui para acessar o sistema](https://easystems-0ixw0ptprokl.streamlit.app/)")
else:
st.error("Credenciais inválidas!")

tela_login()
