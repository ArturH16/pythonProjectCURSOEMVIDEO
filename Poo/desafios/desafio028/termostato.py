class Termostato:
    def __init__(self):
        self.__temperatura = 24
        self.ftemperatura = f"{self.__temperatura}°C"

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self,valor):
        if valor < 16:
            self.__temperatura = 16
            self.ftemperatura = f"{self.__temperatura}°C"
        elif valor > 30:
            self.__temperatura = 30
            self.ftemperatura = f"{self.__temperatura}°C"
        elif (valor * 10) % 5 == 0:
            self.__temperatura = valor
            self.ftemperatura = f"{self.__temperatura}°C"
        else:
            raise ValueError(f"Temperatura de {valor}°C é inválida!")