#Crie uma classe que represente um retângulo pelas suas medidas e área.
from retangulo import Retangulo
from rich import print,inspect

def main():
    r = Retangulo(8,4)
    r.base = 12
    r.altura = 33
    r.medidas = (9,3)
    print(r.medidas)
    inspect(r,private=True,methods=True)

if __name__ == "__main__":
    main()