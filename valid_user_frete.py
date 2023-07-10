import sqlite3
import streamlit as st

# Função para verificar as credenciais de login
def verifica_login(usuario, senha):
    conn = sqlite3.connect('novo.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE user = ? AND senha = ?", (usuario, senha))
    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None



# Tela de login
import sqlite3
import streamlit as st

# Função para verificar as credenciais de login
def verifica_login(usuario, senha):
    conn = sqlite3.connect('novo.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE user = ? AND senha = ?", (usuario, senha))
    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None

# Tela de login
def tela_login():
    st.title("Acesso Solicitante Frete")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Login"):
        if verifica_login(usuario, senha):
            st.success("Login realizado com sucesso!")
            st.markdown("[Acesso Ambiente Fretes](https://easystems-0ixw0ptprokl.streamlit.app/)")
        else:
            st.error("Credenciais inválidas!")

tela_login()
