from abc import ABC
from datetime import date

class Pessoa(ABC):
    def __init__(self,nome,nasc):
        self._nome = nome
        self._nascimento = nasc
        self.idade = date.today().year - self.nascimento

    @property
    def nascimento(self):
        return self._nascimento
    @nascimento.setter
    def nascimento(self,ano_novo):
        if ano_novo >  date.today().year or ano_novo < 1900:
            raise ValueError(f"Ano {ano_novo} é inválido")
        else:
            self._nascimento = ano_novo
            self.idade = date.today().year - self.nascimento
