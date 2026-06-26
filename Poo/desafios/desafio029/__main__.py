#Simule um diário secreto orientado a objetos
from diario import Diario
from rich import print,inspect

def main():
    d = Diario("Gafanhoto")
    d.escrever("Primeira mensagem")
    d.escrever("Você é uma pessoa simpática")
    d.escrever("Você gosta de Python")
    inspect(d,private=True,methods=True)
    d.ler("Gafanhoto")


if __name__ == "__main__":
    main()