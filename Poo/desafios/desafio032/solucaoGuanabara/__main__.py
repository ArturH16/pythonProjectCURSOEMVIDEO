from classe032 import ContaBancaria

def main():
    cc = ContaBancaria(111,"Josenildo","Guanabara")

    print("Vou tentar sacar...")
    cc.sacar(500)

    print("Tentando mudar o nome...")
    cc.nome = "Maricota"

    print(cc)

if __name__ == "__main__":
    main()