import hashlib
from rich import print

class Credencial:
    def __init__(self):
        self.senha = ""
        self.__hash = ""

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self,valor):
        if valor != "":
            valor_bytes = valor.encode("utf-8")
            hash_obj = hashlib.sha256(valor_bytes)
            hash_hex = hash_obj.hexdigest()
            self.__hash = hash_hex
        else:
            return

    def validar(self,chave):
        chave_bytes = chave.encode("utf-8")
        hash_obj = hashlib.sha256(chave_bytes)
        hash_hex = hash_obj.hexdigest()
        if self.senha != hash_hex:
            print("Senha não bate!")
            return f"[red]{False}[/]"
        else:
            print("Senha confere!")
            return f"[green]{True}[/]"
