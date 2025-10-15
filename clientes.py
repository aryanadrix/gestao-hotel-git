clientes = []

def registar_cliente(nome, telefone):
    cliente = {"nome": nome, "telefone": telefone}
    clientes.append(cliente)
    print(f"Cliente {nome} registado com sucesso!")

def listar_clientes():
    print("\n=== Lista de Clientes ===")
    for c in clientes:
        print(f"Nome: {c['nome']}, Telefone: {c['telefone']}")
