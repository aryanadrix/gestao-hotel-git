#Colaboração: Tito Adriano


clientes = [
    {"nome": "Adriano", "telefone": "912345678"},
    {"nome": "Lucas", "telefone": "923456789"}
]

def listar_clientes():
    for c in clientes:
        print(f"{c['nome']} - {c['telefone']}")
