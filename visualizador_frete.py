import streamlit as st
import sqlite3

st.title('Entradas')

# Conectar ao banco de dados
conn = sqlite3.connect('novo.db')
cursor = conn.cursor()

# Executar a consulta SQL para obter os dados da tabela 'entrada'
cursor.execute("SELECT * FROM entrada")
data = cursor.fetchall()

# Obter os nomes das colunas
column_names = [description[0] for description in cursor.description]

# Fechar a conexão com o banco de dados
conn.close()

# Obter os valores únicos das colunas para os filtros
unique_local = list(set([row[column_names.index("local")] for row in data]))
unique_cidade_origem = list(set([row[column_names.index("cidade_origem")] for row in data]))
unique_tipo_veiculo = list(set([row[column_names.index("tipo_veiculo")] for row in data]))

# Filtros
selected_local = st.selectbox("Filtrar por Local:", ["Todos"] + unique_local)
selected_cidade_origem = st.selectbox("Filtrar por Cidade de Origem:", ["Todas"] + unique_cidade_origem)
selected_tipo_veiculo = st.selectbox("Filtrar por Tipo de Veiculo:", ["Todos"] + unique_tipo_veiculo)

# Filtrar os dados com base nos filtros selecionados
filtered_data = data
if selected_local != "Todos":
    filtered_data = [row for row in filtered_data if row[column_names.index("local")] == selected_local]
if selected_cidade_origem != "Todas":
    filtered_data = [row for row in filtered_data if row[column_names.index("cidade_origem")] == selected_cidade_origem]
if selected_tipo_veiculo != "Todos":
    filtered_data = [row for row in filtered_data if row[column_names.index("tipo_veiculo")] == selected_tipo_veiculo]

# Criar uma tabela no Streamlit com os dados filtrados
table = "<style>tbody tr:nth-of-type(odd) {background-color: #f5f5f5;}</style>"
table += "<table><thead><tr>"
for col_name in column_names:
    table += f"<th>{col_name}</th>"
table += "</tr></thead><tbody>"
for row in filtered_data:
    table += "<tr>"
    for value in row:
        table += f"<td>{value}</td>"
    table += "</tr>"
table += "</tbody></table>"

# Exibir a tabela no Streamlit
st.write(table, unsafe_allow_html=True)







st.title('Requisicoes de Fretes')
#tabela de fretes requisição
import streamlit as st
import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('novo.db')
cursor = conn.cursor()

# Executar a consulta SQL para obter os dados da tabela 'frete'
cursor.execute("SELECT * FROM frete")
data = cursor.fetchall()

# Obter os nomes das colunas
column_names = [description[0] for description in cursor.description]

# Fechar a conexão com o banco de dados
conn.close()

# Criar uma tabela no Streamlit
table = "<style>tbody tr:nth-of-type(odd) {background-color: #f5f5f5;}</style>"
table += "<table><thead><tr>"
for col_name in column_names:
    table += f"<th>{col_name}</th>"
table += "</tr></thead><tbody>"

# Função para atualizar o status no banco de dados
def atualizar_status(id, novo_status):
    conn = sqlite3.connect('novo.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE frete SET Status=? WHERE ID=?", (novo_status, id))
    conn.commit()
    conn.close()

# Obter os status únicos da coluna 'Status'
unique_statuses = list(set([row[column_names.index("Status")] for row in data]))

# Criar uma lista suspensa para selecionar o status
selected_status = st.selectbox("Filtrar por status:", ["Todos"] + unique_statuses)

# Filtrar os dados com base no status selecionado
if selected_status != "Todos":
    filtered_data = [row for row in data if row[column_names.index("Status")] == selected_status]
else:
    filtered_data = data

# Exibir os dados filtrados na tabela
for row in filtered_data:
    table += "<tr>"
    for value in row:
        table += f"<td>{value}</td>"
    table += "</tr>"
table += "</tbody></table>"

# Exibir a tabela no Streamlit
st.write(table, unsafe_allow_html=True)

# Atualizar o status selecionado
selected_id = st.selectbox("Selecione o ID do frete para atualizar o status:", [str(row[0]) for row in filtered_data])
novo_status = st.selectbox("Selecione o novo status:", ['Em Andamento', 'Realizado', 'Encerrado'])
if st.button('Atualizar'):
    atualizar_status(selected_id, novo_status)
