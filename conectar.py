import psycopg2

# Criar conexão
conexao = psycopg2.connect(
    database="postgresDB",
    user="meu_usuario",
    password="minha_senha",
    host="127.0.0.1",
    port="5432"
)
print("Conexão com o Banco de Dados aberta com sucesso!")

# Criação do cursor
meu_cursor = conexao.cursor()