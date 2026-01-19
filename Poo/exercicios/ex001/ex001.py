#Declaração de Classes
class Carro:
    #Criando Documentação da classe/DocStrings
    """
    A classe Carro possui seu construtor, que recebe como parâmetros a marca e o ano, que serão os atributos do objeto, respectivamente.
    Além disso, a classe Carro possui o método mostrarInformacoes, o qual informará acerca dos seus atributos.
    """
    def __init__(self,marca="desconhecida",ano=0): #Método COnstrutor
        #Atributos
        self.marca = marca
        self.ano = ano

    #Métodos
    def mostrarInformacoes(self):
        print(f'O seu carro é da marca {self.marca}\nO ano do seu carro é {self.ano}\n')

    #Dunder Methods -> TODA classe tem
    def __str__(self):
        return f'MARCA: {self.marca}\nANO: {self.ano}\n'

    def __getstate__(self):
        return f'MARCA DO OBJETO: {self.marca}\nANO DO OBJETO: {self.ano}'

#Declaração de Objetos
lamborguini = Carro("lamborguini",2008)
lamborguini.mostrarInformacoes()

bmw = Carro("bmw",2010)
bmw.mostrarInformacoes()

byd = Carro()
byd.mostrarInformacoes()

#Mostrando nosso objeto diretamente
print(lamborguini) #Só é possível porque modificamos/criamos o dunder method str

#Acessando documentação da nossa classe
print(lamborguini.__doc__) #Dunder Attribute -> TODA classe tem esse atributo

#Mostrando a classe em formato de dicionário
print(lamborguini.__dict__) #Dunder Attribute .__dict__

#Outra forma de mostrar como dicionário | OBS: Se o método não for sobrescrito
print(bmw.__getstate__()) #Dunder Method .__getstate()__

#Descobrindo qual a classe de um determinado objeto
print(bmw.__class__)