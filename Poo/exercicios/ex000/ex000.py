#Declaração de Classes
class Carro:
    def __init__(self): #Método COnstrutor
        #Atributos
        self.marca = ""
        self.ano = 0

    #Métodos
    def mostrarInformacoes(self):
        print(f'O seu carro é da marca {self.marca}\nO ano do seu carro é {self.ano}')

#Declaração de Objetos
lamborguini = Carro()
lamborguini.marca = "lamborguini"
lamborguini.ano = 2008
lamborguini.mostrarInformacoes()


bmw = Carro()
bmw.marca = "BMW"
bmw.ano = 2010
bmw.mostrarInformacoes()