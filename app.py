from clientes import listar_clientes
from quartos import listar_quartos
from reservas import listar_reservas

def main():
    print("=== Sistema de Gestão de Reservas de Hotel ===")
    listar_clientes()
    listar_quartos()
    listar_reservas()

if __name__ == "__main__":
    main()
