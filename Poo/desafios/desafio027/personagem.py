from abc import ABC,abstractmethod
from random import randint,choice
from rich import print

class Personagem(ABC):
    def __init__(self,nome,vida,golpes):
        self.nome = nome
        self.vida = vida
        self.golpes = golpes

    def atacar(self,alvo,forca):
        golpe = choice(self.golpes)
        print(f"[green]{self.nome}[/] atacou [red]{alvo.nome}[/][blue]({alvo.vida}[/]) com um [blue]{golpe}[/] de força [blue]{forca}[/]")
        ataque = randint(0,forca)
        alvo.receber_dano(ataque)
        print(f"[blue]{alvo.nome}[/] recebeu [red]dano de {ataque}[/]!")

    def receber_dano(self,dano):
        self.vida -= dano


    @abstractmethod
    def curar(self):
        pass