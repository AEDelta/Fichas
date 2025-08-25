from db import get_connection

# Criar ficha
def inserir_ficha(descricao, data, valor, responsavel):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO fichas (descricao, data, valor, responsavel)
    VALUES (%s, %s, %s, %s)
    """, (descricao, data, valor, responsavel))
    conn.commit()
    cur.close()
    conn.close()
    print("Ficha inserida com sucesso!")

# Listar fichas
def listar_fichas():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM fichas")
    fichas = cur.fetchall()
    cur.close()
    conn.close()
    return fichas

# Atualizar ficha
def atualizar_ficha(id, descricao=None, data=None, valor=None, responsavel=None):
    conn = get_connection()
    cur = conn.cursor()
    query = "UPDATE fichas SET "
    campos = []
    valores = []

    if descricao:
        campos.append("descricao=%s")
        valores.append(descricao)
    if data:
        campos.append("data=%s")
        valores.append(data)
    if valor is not None:
        campos.append("valor=%s")
        valores.append(valor)
    if responsavel:
        campos.append("responsavel=%s")
        valores.append(responsavel)

    if campos:
        query += ", ".join(campos) + " WHERE id=%s"
        valores.append(id)
        cur.execute(query, valores)
        conn.commit()

    cur.close()
    conn.close()
    print("Ficha atualizada com sucesso!")

# Deletar ficha
def deletar_ficha(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM fichas WHERE id=%s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    print("Ficha deletada com sucesso!")
