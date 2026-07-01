class Retangulo:
    def __init__(self,base,altura):
        self._base = base
        self._altura = altura
        self._area = None
        self.medidas = f"Base = {self.base}\nAltura = {self.altura}\nÁrea = {self.area}"

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self,nova_base):
        if nova_base > 0:
            self._base = nova_base
        else:
            raise ValueError("Valor inválido para base")

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self,nova_altura):
        if nova_altura:
            self._altura = nova_altura
        else:
            raise ValueError("Valor inválido para a altura")
    @property
    def area(self):
        return self.base * self.altura

    def medidas(self, valores=()):
        self.base(valores[0])
        self.altura(valores[1])
        self.medidas = f"Base = {self.base}\nAltura = {self.altura}\nÁrea = {self.area}"


