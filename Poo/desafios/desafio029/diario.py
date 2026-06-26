from rich import print

class Diario:
    def __init__(self,senhamestra="CeV!@"):
        self.__senha = senhamestra
        self.__segredos = []

    @property
    def senha(self):
        raise PermissionError("Ninguém tem permissão de ver a senha")


    def escrever(self,msg):
        self.__segredos.append(msg)

    def ler(self,senha=None):
        if senha != self.__senha:
            raise PermissionError("Senha inválida! Você não pode ler meu diário!")
        else:
            print("[green]Diário LIBERADO![/]")
            for m in self.__segredos:
                print(f"- {m}")




