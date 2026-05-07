from abc import ABC,abstractmethod


class Transporte(ABC):
    def __init__(self,distancia):
        self.distancia = distancia

    @abstractmethod
    def calc_frete(self):
        pass