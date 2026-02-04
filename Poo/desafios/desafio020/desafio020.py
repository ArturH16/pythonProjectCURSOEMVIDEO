#Crie a classe Gamer, onde podemos cadastrar nome, nick e os
#jogos favoritos de uma pessoa. Crie também um método que permita
#mostar a ficha desse gamer

from rich import print
from rich.panel import Panel


class Gamer:
    def __init__(self,nome,nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = []

    def add_favoritos(self,favorito):
        self.favoritos.append(favorito)


    def mostrar_ficha(self):
        conteudo = f"Nome Real: [black on blue]{self.nome}[/]\nJogos Favoritos:\n"
        self.favoritos.sort()
        for v in self.favoritos:
            conteudo += f":video_game: [blue]{v}[/]\n"

        ficha = Panel(conteudo,title=f" Jogador <{self.nick}>")
        print(ficha)




j1 = Gamer("Fabricio da Silva","detonator 2025")
j1.add_favoritos("Mario")
j1.add_favoritos("God of War")
j1.add_favoritos("Sonic")
j1.add_favoritos("Fortnite")
j1.mostrar_ficha()
j2 = Gamer("Pedrão","pedrogameplays2021")
j2.add_favoritos("Lego Batman")
j2.add_favoritos("Among Us")
j2.mostrar_ficha()







