from conta_bancaria import ContaBancaria
from rich import print,inspect
#Aprimore o exercício da ContaBancaria, aplicando conceitos de encapsulamento
def main():
    print("Criando a conta...")
    cc = ContaBancaria(123,"Gustavo",1000,"Gafanhoto")

    print("Realizando depósito...")
    cc.depositar(500)

    print("Realizando saque...")
    cc.sacar(200,"Gafanhbnoto")
    cc.nome = "Manuel"
    inspect(cc,methods=True,private=True)

if __name__ == "__main__":
    main()