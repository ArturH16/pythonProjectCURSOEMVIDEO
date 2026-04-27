from poligono import Poligono


class Quadrado(Poligono):
    def __init__(self,qtd_lados,lado):
        super().__init__(qtd_lados,lado)

    def area(self):
        return self.lado ** 2