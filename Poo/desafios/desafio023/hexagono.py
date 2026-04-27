from poligono import Poligono

class Hexagono(Poligono):
    def __init__(self,qtd_lados,lado):
        super().__init__(qtd_lados,lado)

    def area(self):
        return f"{(6 * ((self.lado ** 2) * 3 ** 0.5 ) / 4):,.2f}"