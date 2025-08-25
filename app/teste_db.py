from crud import criar_tabela, inserir_cliente, listar_clientes, atualizar_cliente, deletar_cliente

# Criar tabela
criar_tabela()

# Inserir cliente
inserir_cliente("João Silva", "joao@email.com", "11999999999")
inserir_cliente("Maria Souza", "maria@email.com", "11988888888")

# Listar clientes
clientes = listar_clientes()
for cliente in clientes:
    print(cliente)

# Atualizar cliente
atualizar_cliente(1, telefone="11977777777")

# Deletar cliente
# deletar_cliente(2)
