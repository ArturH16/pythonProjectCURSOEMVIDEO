#Crie a classe Produto, onde podemos cadatrar nome e o preço.
#Crie também um método que mostre uma etiqueta de preço do produto
from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco
    def mostrar_etiqueta(self):
        tamanho_estilo_ponto = "." * 10
        tamanho_estilo_linha = "-" * 30
        conteudo = f"      {self.nome}    \n{tamanho_estilo_linha}\n{tamanho_estilo_ponto}R${self.preco}{tamanho_estilo_ponto}"
        etiqueta = Panel(conteudo,width=34)
        print(etiqueta)


p1 = Produto("Iphone 17 Pro Max",25_000.85)
p2 = Produto("Mouse",120)

p1.mostrar_etiqueta()
p2.mostrar_etiqueta()