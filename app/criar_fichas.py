from db import get_connection

def criar_tabela_fichas():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS fichas (
        id SERIAL PRIMARY KEY,
        descricao VARCHAR(255) NOT NULL,
        data DATE NOT NULL,
        valor NUMERIC(10,2),
        responsavel VARCHAR(100)
    )
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("Tabela 'fichas' criada com sucesso!")

if __name__ == "__main__":
    criar_tabela_fichas()
