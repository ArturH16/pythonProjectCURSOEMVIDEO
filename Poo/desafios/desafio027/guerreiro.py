from personagem import Personagem
from random import randint
from rich import print
class Guerreiro(Personagem):
    def __init__(self,nome,vida,golpes=["Soco","Pulo Giratório"]):
        super().__init__(nome,vida,golpes)

    def curar(self):
        cura = randint(0,100)
        self.vida += cura
        print(f"[blue]{self.nome}[/] fez uma atadura e [green]recuperou {cura} pontos [/] de vida. ")