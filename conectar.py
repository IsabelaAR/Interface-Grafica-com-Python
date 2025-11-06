import psycopg2

# Criar conexão
conexao = psycopg2.connect(
    database="postgresDB",
    user="admin",
    password="admin123",
    host="127.8.8.1",
    port="5433"
)
print("Conexão com o Banco de Dados aberta com sucesso!")

# Criação do cursor
meu_cursor = conexao.cursor()