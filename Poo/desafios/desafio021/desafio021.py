#Crie a classe Caneta, que simula o funcionamento de uma caneta colorida,
#podendo escrever frases na cor relativa.
from rich import print

class Caneta:
    def __init__(self,cor):
        self.cor = cor
        self.is_tampada = True

    def destampar(self):
        if self.is_tampada:
            self.is_tampada = not self.is_tampada

    def escrever(self,msg):
        if self.is_tampada:
            print(":no_entry_sign: A [blue]caneta [/] está tampada!")
            return
        if self.cor.upper() == "VERMELHA":
            print(f"[red]{msg} [/]",end="")
            return
        elif self.cor.upper() == "AZUL":
            print(f"[blue]{msg} [/]",end="")
            return
        elif self.cor.upper() == "VERDE":
            print(f"[green]{msg} [/]",end="")
            return
        else:
            print(f"{msg}")

    def quebrar_linha(self,n):
        for c in range(0,n):
            print()


c1 = Caneta("azul")
c2 = Caneta("vermelha")
c3 = Caneta("verde")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá,tudo bem?")
c1.quebrar_linha(2)
c2.escrever("Olá Gafanhoto!")
c3.escrever("Vamos Exercitar!")
