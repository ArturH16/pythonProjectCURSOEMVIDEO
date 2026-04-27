#Algumas partes essenciais do desafio em si foram alteradas
#para respeitar a matemática
#Implementar a classe abstrata mãe com o atributo qtd_lados, e o metodo
#abstrato e area(); além disso, contruir as subclasses quadrado e triângulo
from quadrado import Quadrado
from hexagono import Hexagono
from rich import print


def main():
    q1 = Quadrado(4,12)
    print(f"Área = {q1.area()}")
    print(f"Perímetro = {q1.perimetro()}")
    print("\n")
    h1 = Hexagono(6,5)
    print(f"Área = {h1.area()}")
    print(f"Perímetro = {h1.perimetro()}")


if __name__ == "__main__":
    main()