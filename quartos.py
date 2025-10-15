quartos = [
    {"numero": 101, "tipo": "Solteiro", "disponivel": True},
    {"numero": 102, "tipo": "Casal", "disponivel": False}
]

def listar_quartos():
    for q in quartos:
        estado = "Disponível" if q["disponivel"] else "Ocupado"
        print(f"Quarto {q['numero']} - {q['tipo']} ({estado})")
