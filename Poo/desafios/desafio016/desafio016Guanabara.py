from rich import print
from rich import inspect

class Funcionario:
    #Atributos de classe -> acessados pelo nome da classe
    empresa = "Curso em Vídeo"

    def __init__(self,nome,setor,cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self) -> str:
        return f":handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}"

#Funcionario.empresa = "IFCE"

c1 = Funcionario("Mario","Administração","Diretor")
c1.empresa = "Estudonauta"
#Ele criou um atributo de instância, comportamento do Python.
print(c1.empresa)
print(c1.apresentar())
#inspect(c1,methods=True,dunder=True)
c2 = Funcionario("Pedro","TI","Programador")
print(c2.apresentar())

#inspect(Funcionario,all=True)