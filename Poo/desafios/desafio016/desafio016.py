#Crie a classe Funcionário, onde podemos cadastrar nome,setor e cargo.
#Crie também um método que permita ao funcionário se apresentar.
from rich import print

class Funcionario:
    def __init__(self,nome,setor,cargo,empresa = "Curso em Vídeo"):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.empresa = empresa


    def apresentar(self):
        return f":handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {self.empresa}"



c1 = Funcionario("Dandara","Biomedicina","Médica")
print(c1.apresentar())

c2 = Funcionario("Artur","TI","Programador Full-Stack")
print(c2.apresentar())