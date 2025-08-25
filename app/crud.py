from db import get_connection

# Criar tabela
def criar_tabela():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        email VARCHAR(100),
        telefone VARCHAR(20)
    )
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("Tabela criada com sucesso!")

# Inserir cliente
def inserir_cliente(nome, email, telefone):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO clientes (nome, email, telefone)
    VALUES (%s, %s, %s)
    """, (nome, email, telefone))
    conn.commit()
    cur.close()
    conn.close()
    print("Cliente inserido com sucesso!")

# Listar clientes
def listar_clientes():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM clientes")
    clientes = cur.fetchall()
    cur.close()
    conn.close()
    return clientes

# Atualizar cliente
def atualizar_cliente(id, nome=None, email=None, telefone=None):
    conn = get_connection()
    cur = conn.cursor()
    query = "UPDATE clientes SET "
    campos = []
    valores = []

    if nome:
        campos.append("nome=%s")
        valores.append(nome)
    if email:
        campos.append("email=%s")
        valores.append(email)
    if telefone:
        campos.append("telefone=%s")
        valores.append(telefone)

    if campos:
        query += ", ".join(campos) + " WHERE id=%s"
        valores.append(id)
        cur.execute(query, valores)
        conn.commit()

    cur.close()
    conn.close()
    print("Cliente atualizado com sucesso!")

# Deletar cliente
def deletar_cliente(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM clientes WHERE id=%s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    print("Cliente deletado com sucesso!")
