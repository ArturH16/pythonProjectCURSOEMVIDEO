from transporte import Transporte

class Drone(Transporte):
    fator = 9.5
    def __init__(self,distancia):
        super().__init__(distancia)

    def calc_frete(self):
        if self.distancia > 10:
            return "Raio máximo de 10km"
        else:
            return  f" R${Drone.fator * self.distancia:.2f}"