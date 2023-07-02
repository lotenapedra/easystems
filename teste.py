import streamlit as st
import requests
import sqlite3

# Função para criar a tabela no banco de dados
def criar_tabela():
    conn = sqlite3.connect('novo.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS enderecos (
            cep TEXT,
            logradouro TEXT,
            complemento TEXT,
            bairro TEXT,
            cidade TEXT,
            estado TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Função para inserir os dados no banco de dados
def inserir_endereco(cep, logradouro, complemento, bairro, cidade, estado):
    conn = sqlite3.connect('novo.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO enderecos (cep, logradouro, complemento, bairro, cidade, estado)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (cep, logradouro, complemento, bairro, cidade, estado))
    conn.commit()
    conn.close()

# Função para consultar o CEP e inserir os dados no banco de dados
def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    data = response.json()

    if "erro" not in data:
        inserir_endereco(
            data["cep"],
            data["logradouro"],
            data["complemento"],
            data["bairro"],
            data["localidade"],
            data["uf"]
        )
        st.success("Consulta realizada com sucesso e dados inseridos no banco de dados!")
        st.write("CEP:", data["cep"])
        st.write("Logradouro:", data["logradouro"])
        st.write("Complemento:", data["complemento"])
        st.write("Bairro:", data["bairro"])
        st.write("Cidade:", data["localidade"])
        st.write("Estado:", data["uf"])
    else:
        st.error("CEP não encontrado!")

# Configurações do Streamlit
st.title("Consulta de CEP")
cep_input = st.text_input("Digite o CEP para consulta")

if st.button("Consultar"):
    criar_tabela()
    consultar_cep(cep_input)
