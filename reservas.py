reservas = [
    {"cliente": "Adriano", "quarto": 101}
]

def listar_reservas():
    for r in reservas:
        print(f"{r['cliente']} → Quarto {r['quarto']}")
