#Crie a classe Churrasco, onde seja possível informar quantas pessoas
#vão participar e mostre qunato de carne deve ser comprado, o custo total
#do churrasco e o preço por pessoa.

from rich import print
from rich.panel import Panel

#DADOS A SEREM CONSIDERADOS:
#Consumo Padrão: 400g / pessoa
#Preço: R$82,4/Kg

class Churrasco:
    def __init__(self,titulo,quant):
        self.titulo = titulo
        self.quant = quant

    def analisar(self):
        quant_carne = 0.4 * self.quant
        custo_total = 82.4 * quant_carne
        custo_pessoa = custo_total / self.quant
        dados_analisados = f"Analisando [green]{self.titulo}[/] com [blue]{self.quant}[/]\nCada participante comerá 0.4 Kg e cada Kg custa R$82.40\nRecomendo [blue]comprar {quant_carne:.2f}Kg[/] de carne\nO custo total será de [green]R${custo_total:.2f}[/]\nCada pessoa deverá pagar [red]R${custo_pessoa:.2f}[/] para participar."
        analise = Panel(dados_analisados,title=self.titulo)
        print(analise)


c1 = Churrasco("Churras dos Bacanas",100)
c1.analisar()

