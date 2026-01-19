
#Criando a classe ContaBancaria
class ContaBancaria:
    """
    A classe ContaBancaria possui os seguintes atributos: seu id, o nome do titular
    da conta, o saldo da conta, que pode ser informado ou não ( se não for, valor padrão é 0).
    Em relação aos seus métodos, a classe possui os métodos de depositar, que vão adicionar um valor
    para o atributo saldo, e o método sacar, que vai retirar um valor determinado do atributo saldo, caso
    o saldo seja suficiente.
    """

    def __init__(self,id,titular,saldo=0):
        self.id = id
        self.titular = titular
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucesso!")

    #Dunder Methods
    def __str__(self):
        return f"A conta {self.id} do titular {self.titular} tem R${self.saldo:_.2f}\n"


    #Métodos próprios da Classe
    def depositar(self,valor):
        self.saldo += valor
        print(f'\033[32mDEPÓSITO PARA A CONTA {self.id} NO VALOR DE R${self.saldo:_.2f} FEITO COM SUCESSO!\033[m\n')

    def sacar(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return f"\033[32mSAQUE NO VALOR DE R${self.saldo:_.2f} FEITO COM SUCESSO NA CONTA {self.id}!\033[m\n"
        else:
            return f"\033[31mSALDO INSUFICIENTE NA CONTA {self.id}\033[m\n"

#Instanciando objetos da classe ContaBancaria


c1 = ContaBancaria(1,"Artur",10000)
c1.depositar(700)
print(c1.sacar(10700))
print(c1)
print(c1.__doc__)