from rich import print
import time

class Livro:
    def __init__(self,titulo,paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1

        print(f":open_book: [blue]Você acabou de abrir o livro [red]'{self.titulo}'[/] que tem [green]{self.total_paginas} páginas[/] no total. Você agora está na [yellow]página {self.pagina_atual}[/][/]")

    def avancar_paginas(self,qtd_paginas = 0):
        cont = 0
        for pg in range(0,qtd_paginas ,1):
            if not self.final_livro():
                self.pagina_atual += 1
                cont += 1
                print(f"Pág {self.pagina_atual} :arrow_forward: ",end="")
                time.sleep(0.2)
        print(f" [blue]Você avançou {cont} páginas e agora está na [yellow]página {self.pagina_atual}[/][/]")
        if self.final_livro():
            print(f":closed_book: [red]Você chegou ao final do livro '{self.titulo}'[/]")
    def final_livro(self) -> bool:
        return True if self.pagina_atual == self.total_paginas else False


l1 = Livro("10 coisas que eu aprendi",20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(50)