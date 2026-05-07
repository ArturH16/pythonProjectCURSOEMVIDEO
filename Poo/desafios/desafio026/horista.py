from funcionario import Funcionario

class Horista(Funcionario):
    def __init__(self,nome,valor_hora,horas_trab):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calc_sal(self):
        self.salario = self.valor_hora * self.horas_trab
        self.salario -= self.salario * Horista.inss

