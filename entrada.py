import streamlit as st
import sqlite3
from datetime import date
import requests

# Função de consulta de CEP
def consulta_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    data = response.json()

    if "erro" not in data:
        cidade = data["localidade"]
        uf = data["uf"]
        return cidade, uf
    else:
        st.write("CEP não encontrado.")
        return None, None

st.title('Entrada')
local = st.selectbox('Local', ['Clean Plastic', 'Clean Poa', 'Clean Jundiai', 'Clean Bottle', 'Clean Fortal', 'Raposo Plasticos', 'Raposo Minas', 'Fornecedor PF', 'Outro'])

col1, col2 = st.columns(2)
today = date.today()

# Verifica se o estado do campo de CEP de origem já foi definido
if "cep_origem" not in st.session_state:
    st.session_state.cep_origem = ""
if "cidade_origem" not in st.session_state:
    st.session_state.cidade_origem = ""
if "uf_origem" not in st.session_state:
    st.session_state.uf_origem = ""

with col1:
    cep_origem = st.text_input('CEP Origem', value=st.session_state.cep_origem)
    cidade_origem = st.session_state.cidade_origem
    uf_origem = st.session_state.uf_origem
    
    if st.button("Consultar Origem"):
        cidade_origem, uf_origem = consulta_cep(cep_origem)
        if cidade_origem is not None:
            st.write('Cidade Origem:', cidade_origem)
            st.session_state.cep_origem = cep_origem  # Armazena o valor do CEP de origem
            st.session_state.cidade_origem = cidade_origem  # Armazena a cidade de origem
            st.session_state.uf_origem = uf_origem  # Armazena a UF de origem

    nome_completo = st.text_input("Nome Completo:")
    tipo_veiculo = st.selectbox('Tipo de Veiculo:', ["Truck-Side", "Carreta-Side", "Truck-Grade Baixa", "Carreta-Grade Baixa", "Carreta Graneleira", "Container"])
    motivo = st.selectbox('Motivo:', ['Carregar', 'Descarregar'])
    data = st.date_input("Data Entrada", value=today, key="data_input")

with col2:
    empresa_origem = st.selectbox('Empresa Origem', ['Clean Plastic', 'Clean Poa', 'Clean Jundiai', 'Clean Bottle', 'Clean Fortal', 'Raposo Plasticos', 'Raposo Minas', 'Fornecedor PF', 'Outro'])

    telefone = st.text_input('Telefone')
    placa = st.text_input('Placa do Veiculo:')
    frete_retono = st.selectbox('Possuem Frete Retorno?', ['Sim', 'Nao'])

info = st.text_area('Info. Complementar')



if st.button("Salvar"):
    # Connect to the database or create a new one if it doesn't exist
    conn = sqlite3.connect('novo.db')

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Create the 'entrada' table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS entrada (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        local TEXT,
                        cep_origem TEXT,
                        cidade_origem TEXT,
                        uf_origem TEXT,
                        nome_completo TEXT,
                        tipo_veiculo TEXT,
                        motivo TEXT,
                        data TEXT,
                        empresa_origem TEXT,
                        telefone TEXT,
                        placa TEXT,
                        frete_retorno TEXT,
                        info_complementar TEXT
                    )''')

    # Get the values from the fields
    local_value = local
    cep_origem_value = cep_origem
    cidade_origem_value = st.session_state.cidade_origem  # Utiliza a cidade de origem armazenada em st.session_state
    uf_origem_value = st.session_state.uf_origem  # Utiliza a UF de origem armazenada em st.session_state
    nome_completo_value = nome_completo
    tipo_veiculo_value = tipo_veiculo
    motivo_value = motivo
    data_value = data.strftime("%Y-%m-%d")
    empresa_origem_value = empresa_origem
    telefone_value = telefone
    placa_value = placa
    frete_retorno_value = frete_retono
    info_complementar_value = info

    # Insert the values into the 'entrada' table
    cursor.execute('''INSERT INTO entrada (
                        local,
                        cep_origem,
                        cidade_origem,
                        uf_origem,
                        nome_completo,
                        tipo_veiculo,
                        motivo,
                        data,
                        empresa_origem,
                        telefone,
                        placa,
                        frete_retorno,
                        info_complementar
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (
                        local_value,
                        cep_origem_value,
                        cidade_origem_value,
                        uf_origem_value,
                        nome_completo_value,
                        tipo_veiculo_value,
                        motivo_value,
                        data_value,
                        empresa_origem_value,
                        telefone_value,
                        placa_value,
                        frete_retorno_value,
                        info_complementar_value
                    ))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    st.success("Dados salvos com sucesso!")
