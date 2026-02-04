#Crie a classe Livro, que vai simular a passagem de páginas de um livro
#considerando também se o usuário chegou ao fim da leitura.

from rich import print
from time import sleep

class Livro:
    def __init__(self,titulo,paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1
        print(f":book: [blue]Você acabou de abrir o livro' [red]{self.titulo}[/]' que tem [green]{self.paginas} páginas[/] no total. Você agora está na [yellow]página {self.pagina_atual}[/][/]")


    def avancar_paginas(self,quant=1):
        paginas_restantes = self.paginas - quant
        if paginas_restantes < 0:
            quant = self.paginas - self.pagina_atual
        pagina = self.pagina_atual + quant
        while True:
            if self.pagina_atual == pagina:
                print(f"[blue]Você avançou {quant} páginas e agora está na página [yellow]{self.pagina_atual}[/]")
                if self.pagina_atual == self.paginas:
                    print(f":police_car_light: [red]Você chegou ao final do livro '{self.titulo}'[/]")
                    break
                else:
                    break
            self.pagina_atual += 1
            sleep(0.2)
            print(f"Pag {self.pagina_atual} :arrow_right: ",end="")




l1 = Livro("Suma Teológica",20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(100)


