reservas = []

def criar_reserva(nome_cliente, numero_quarto):
    reserva = {"cliente": nome_cliente, "quarto": numero_quarto}
    reservas.append(reserva)
    print(f"Reserva criada para {nome_cliente} no quarto {numero_quarto}.")

def cancelar_reserva(nome_cliente):
    global reservas
    reservas = [r for r in reservas if r["cliente"] != nome_cliente]
    print(f"Reserva de {nome_cliente} cancelada.")

def listar_reservas():
    print("\n=== Lista de Reservas ===")
    if not reservas:
        print("Nenhuma reserva registada.")
    else:
        for r in reservas:
            print(f"Cliente: {r['cliente']} | Quarto: {r['quarto']}")
