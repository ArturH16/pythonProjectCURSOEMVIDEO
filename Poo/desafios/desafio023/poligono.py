from abc import ABC, abstractmethod


class Poligono(ABC):
    def __init__(self,qtd_lados,lado):
        self.qtd_lados = qtd_lados
        self.lado = lado

    def perimetro(self):
        return self.qtd_lados * self.lado

    @abstractmethod
    def area(self):
        pass