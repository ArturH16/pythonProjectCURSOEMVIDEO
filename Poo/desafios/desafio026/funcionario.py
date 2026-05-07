from abc import ABC,abstractmethod
from rich.panel import Panel
from rich import print
class Funcionario(ABC):
    sal_min = 1621
    inss = 0.075
    def __init__(self,nome,sal_bruto=0,salario=0):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = salario

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        conteudo = f"O salário de [blue]{self.nome}[/]([purple]{type(self).__name__}[/]) é de [green]R${self.salario:.2f}[/] e corresponde a [yellow]{self.salario/Funcionario.sal_min:.2f} salaŕios mínimos[/]."
        panel = Panel(conteudo,title="Análise de Salaŕios")
        print(panel)