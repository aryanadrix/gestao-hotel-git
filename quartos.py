rooms = [
    {"number": 101, "tipo": "Solteiro", "disponivel": True},
    {"number": 102, "tipo": "Casal", "disponivel": False}
]

def listar_quartos():
    print("\n=== Lista de Quartos ===")
    for q in rooms:
        estado = "Disponível" if q["disponivel"] else "Ocupado"
        print(f"Quarto {q['number']} - {q['tipo']} ({estado})")

