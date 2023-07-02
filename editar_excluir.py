import streamlit as st
import sqlite3

st.title('Excluir cadastro')

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
    cursor.execute("UPDATE entrada SET Status=? WHERE ID=?", (novo_status, id))
    conn.commit()
    conn.close()

# Função para excluir uma linha do banco de dados
def excluir_cadastro(id):
    conn = sqlite3.connect('novo.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM entrada WHERE ID=?", (id,))
    conn.commit()
    conn.close()

# Obter os valores únicos da coluna 'data' para o filtro
unique_dates = list(set([row[column_names.index("data")] for row in data]))

# Criar um seletor de data para filtrar
selected_date = st.date_input("Filtrar por data:", value=None, min_value=None, max_value=None, key=None, help=None)
if selected_date:
    filtered_data = [row for row in data if row[column_names.index("data")] == selected_date.strftime("%Y-%m-%d")]
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

# Excluir a linha selecionada
selected_id = st.selectbox("Para excluir, selecione o ID:", [str(row[0]) for row in filtered_data])
if st.button('Excluir'):
    excluir_cadastro(selected_id)
