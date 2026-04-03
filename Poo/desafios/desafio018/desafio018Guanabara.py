from rich import print
from rich.panel import Panel
class Churrasco:
    #Atributos de classe
    #Em Python, eu posso definir explicitamente o tipo da variável
    consumo_padrao:float = 0.400 #Consumo de carne por pessoa em kg
    preco_kg:float = 82.40 #Cada kg de carne custa R$82.40

    def __init__(self,titulo,qtd_p):
        self.titulo = titulo
        self.participantes = qtd_p

    def __str__(self):
        return f"Este é o {self.titulo} com {self.participantes} pessoas participando"


    def calcular_qtd_carne(self) -> float:
        return self.participantes * Churrasco.consumo_padrao


    def calcular_custo_total(self) -> float:
        #Escrita alternativa de Class.metodo()
        return self.calcular_qtd_carne() * self.__class__.preco_kg


    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.participantes


    def analisar(self):
        conteudo = f"Analisando [green]{self.titulo}[/] com [blue]{self.participantes} convidados[/]"
        conteudo += f"\nCada participante comerá {Churrasco.consumo_padrao} kg e cada kg custa R${Churrasco.preco_kg:,.2f}"
        conteudo += f"\nRecomendo [blue]comprar {self.calcular_qtd_carne():.3f} kg de carne[/]"
        conteudo += f"\nO custo total será de [green]R${self.calcular_custo_total():,.2f}[/]"
        conteudo += f"\nCada pessoa pagará [yellow]R${self.calcular_custo_individual():,.2f}[/]"
        painel = Panel(conteudo,title = self.titulo)
        print(painel)




c1 = Churrasco("Churras dos Amigos",15)
print(c1)
c1.analisar()


c2 = Churrasco("Festa do Último Herói da Terra",80)
c2.analisar()