from transporte import Transporte

class Caminhao(Transporte):
    fator = 1.2
    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        if self.distancia < 50:
            return "Raio mínimo de 50km"
        else:
            return  f" R${Caminhao.fator * self.distancia:.2f}"