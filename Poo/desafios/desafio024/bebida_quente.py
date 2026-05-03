from abc import ABC,abstractmethod

class BebidaQuente(ABC):

    def preparar(self):
        print("--- Iniciando o Preparo ---")
        print(self.ferver_agua())
        print(self.misturar())
        print(self.servir())
        print("--- Bebida Pronta ---")
        print()

    def ferver_agua(self):
        return "1. Fervendo água a 100 graus Celsius"

    @abstractmethod
    def misturar(self):
        pass
    @abstractmethod
    def servir(self):
        pass