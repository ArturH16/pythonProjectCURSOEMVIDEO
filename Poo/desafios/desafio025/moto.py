from transporte import Transporte

class Moto(Transporte):
    fator = 0.5
    def __init__(self,distancia):
        super().__init__(distancia)

    def calc_frete(self):
        return f" R${Moto.fator * self.distancia:.2f}"