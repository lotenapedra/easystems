import requests
import streamlit as st
import sqlite3
from datetime import date
st.title('Solicitar um Frete')
def consulta_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    data = response.json()

    if "erro" not in data:
        cidade = data["localidade"]
        return cidade
    else:
        st.write("CEP não encontrado.")
        return None



today = date.today()
empresa_origem = st.selectbox('Empresa Origem/local de Coleta', ['Clean Plastic', 'Clean Poa', 'Clean Jundiai', 'Clean Bottle', 'Clean Fortal', 'Raposo Plasticos', 'Raposo Minas', 'Fornecedor PF', 'Outro'])

col1, col2 = st.columns(2)
today = date.today()

# Verifica se o estado do campo de CEP de origem já foi definido
if "cep_origem" not in st.session_state:
    st.session_state.cep_origem = ""
if "cep_destino" not in st.session_state:
    st.session_state.cep_destino = ""
if "cidade_origem" not in st.session_state:
    st.session_state.cidade_origem = ""
if "cidade_destino" not in st.session_state:
    st.session_state.cidade_destino = ""

with col1:
    cep_origem = st.text_input('CEP Origem', value=st.session_state.cep_origem)
    cidade_origem = st.session_state.cidade_origem
    
    if st.button("Consultar Origem"):
        cidade_origem = consulta_cep(cep_origem)
        if cidade_origem is not None:
            st.write('Cidade Origem:', cidade_origem)
            st.session_state.cep_origem = cep_origem  # Armazena o valor do CEP de origem
            st.session_state.cidade_origem = cidade_origem  # Armazena a cidade de origem
    cep_destino = st.text_input('CEP Destino', value=st.session_state.cep_destino)
    cidade_destino = st.session_state.cidade_destino
    if st.button("Consultar Destino"):
        cidade_destino = consulta_cep(cep_destino)
        if cidade_destino is not None:
            st.write('Cidade Destino:', cidade_destino)
            st.session_state.cep_destino = cep_destino  # Armazena o valor do CEP de destino
            st.session_state.cidade_destino = cidade_destino  # Armazena a cidade de destino
        elif cidade_origem is not None:
            st.write('Cidade Origem:', cidade_origem)  # Mantém a cidade de origem quando a consulta do destino falha

with col2:
    data_coleta = st.date_input("Data da coleta", value=today, key="data_input")
    data_entrega = st.date_input("Data da Entrega", value=today, key="")
    tipo_veiculo = st.selectbox("Tipo de Veiculo", ["Truck-Side", "Carreta-Side", "Truck-Grade Baixa", "Carreta-Grade Baixa", "Carreta Graneleira", "Container"])             
Observacao = st.text_area("Observacoes")

# Save button
if st.button("Salvar"):
    # Connect to the database or create a new one if it doesn't exist
    conn = sqlite3.connect('novo.db')

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Create the 'frete' table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS frete (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        empresa_origem TEXT,
                        cep_origem TEXT,
                        cidade_origem TEXT,
                        cep_destino TEXT,
                        cidade_destino TEXT,
                        data_coleta TEXT,
                        data_entrega TEXT,
                        tipo_veiculo TEXT,
                        observacao TEXT
                    )''')

    # Get the values from the fields
    empresa_origem_value = empresa_origem
    cep_origem_value = cep_origem
    cidade_origem_value = st.session_state.cidade_origem  # Utiliza a cidade de origem armazenada em st.session_state
    cep_destino_value = cep_destino
    cidade_destino_value = st.session_state.cidade_destino  # Utiliza a cidade de destino armazenada em st.session_state
    data_coleta_value = data_coleta.strftime("%Y-%m-%d")
    data_entrega_value = data_entrega.strftime("%Y-%m-%d")
    tipo_veiculo_value = tipo_veiculo
    observacao_value = Observacao

    # Insert the values into the 'frete' table
    cursor.execute('''INSERT INTO frete (
                        empresa_origem,
                        cep_origem,
                        cidade_origem,
                        cep_destino,
                        cidade_destino,
                        data_coleta,
                        data_entrega,
                        tipo_veiculo,
                        observacao
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (empresa_origem_value, cep_origem_value, cidade_origem_value, cep_destino_value, cidade_destino_value, data_coleta_value, data_entrega_value, tipo_veiculo_value, observacao_value))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    st.success("Dados salvos com sucesso!")
