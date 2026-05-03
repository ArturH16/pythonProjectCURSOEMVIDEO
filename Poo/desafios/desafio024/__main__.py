#Simule uma cafeteira

from cha import Cha
from cafe import Cafe
from leite import Leite

def main():
    cafe = Cafe()
    cafe.preparar()
    cha = Cha()
    cha.preparar()
    leite = Leite()
    leite.preparar()


if __name__ == "__main__":
    main()