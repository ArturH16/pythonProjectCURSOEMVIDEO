from classes029 import Diario
from rich import print
def main():
    meu_diario = Diario()
    meu_diario.escrever("Essa é a primeira mensagem")
    meu_diario.escrever("Estou aprendendo Python")
    try:
        meu_diario.ler("CeV@")
    except Exception as e:
        print(f"[red]ERRO: {e}")

if __name__ == "__main__":
    main()