import pandas as pd
import sqlite3

# Carregar o arquivo CSV em um DataFrame
file_path = 'sales.csv'
df = pd.read_csv(file_path)

# Conectar ao banco de dados SQLite em memória
conn = sqlite3.connect(':memory:')

# Escrever o DataFrame para uma tabela no banco de dados
df.to_sql('sales', conn, index=False, if_exists='replace')

# Consultar os dados para garantir que foram inseridos corretamente
query_result = pd.read_sql_query('SELECT * FROM sales', conn)

# Exibir os dados inseridos
print(query_result)

# Fechar a conexão com o banco de dados
conn.close()