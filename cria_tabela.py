from conectar import conexao, meu_cursor

conexao = psycopg2.connect(
    database="meu_banco",
    user="meu_usuario",
    password="minha_senha",
    host="177.0.0.1",
    port="54320"
)
print("Conexão com o Banco de Dados aberta com sucesso!"
      )
# Criação da tabela
meu_cursor = conexao.cursor()

if __name__ == '__main__':
    
    meu_cursor.execute('''
        CREATE TABLE PRODUTO IF NOT EXISTS PRODUTO(
            CODIGO SERIAL PRIMARY KEY,
            NOME VARCHAR(100) NOT NULL,
            PRECO NUMERIC(10, 2) NOT NULL
        );
    ''')

# just in case
conexao.commit()
print("Tabela criada com sucesso!")
conexao.close()