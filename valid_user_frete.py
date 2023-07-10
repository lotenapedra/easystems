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
            if st.button("Acessar o sistema"):
                abrir_sistema()
        else:
            st.error("Credenciais inválidas!")

def abrir_sistema():
    link = "https://easystems-0ixw0ptprokl.streamlit.app/"
    js = f"window.open('{link}')"  # Abrir o link em uma nova guia do navegador
    html = '<img src onerror="{}">'.format(js)  # Executar o JavaScript
    st.markdown(html, unsafe_allow_html=True)

# Função para verificar as credenciais de login
def verifica_login(usuario, senha):
    # Implemente a lógica de verificação de login aqui
    # Retorne True se as credenciais forem válidas, caso contrário, retorne False
    return True  # Altere conforme sua lógica de verificação

tela_login()
