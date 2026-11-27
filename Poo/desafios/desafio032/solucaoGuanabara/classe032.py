from hashlib import sha256
class ContaBancaria:
    """
    A classe ContaBancaria possui os seguintes atributos: seu id, o nome do titular
    da conta, o saldo da conta, que pode ser informado ou não ( se não for, valor padrão é 0).
    Em relação aos seus métodos, a classe possui os métodos de depositar, que vão adicionar um valor
    para o atributo saldo, e o método sacar, que vai retirar um valor determinado do atributo saldo, caso
    o saldo seja suficiente.
    """

    def __init__(self,id:int,nome:str=None,saldo:float=0,chave:str=None):
        self._id = id #PUBLICO (+)
        self._titular = nome #PROTEGIDO (#)
        self.__saldo = saldo #PRIVADO (-)
        if chave is None:
            chave = self.pede_senha()
        self.__hash = sha256(chave.encode('utf-8')).hexdigest()
        print(f"Conta {self._id} criada com sucesso! Saldo atual de R${self.__saldo}")

    def pede_senha(self):
        from pwinput import pwinput

        while True:
            senha = str(pwinput("Senha: ").strip())
            if len(senha) >= 6:
                break

        return senha

    def validar_senha(self,chave:str):
        usuario = sha256(chave.encode()).hexdigest()
        if usuario == self.__hash:
            return True
        else:
            return False
    #Dunder Methods
    def __str__(self):
        #return f"A conta {self.id} do titular {self.titular} tem R${self.saldo:,.2f}\n"
        return f"Estado atual da conta: {self.__dict__}"

    #Métodos próprios da Classe
    def depositar(self,valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f'\033[32mDEPÓSITO PARA A CONTA {self._id} NO VALOR DE R${valor:,.2f} FEITO COM SUCESSO!\033[m\n')

    def sacar(self,valor,chave=None):
        valor = abs(valor)
        if chave is None:
            chave = self.pede_senha()
        if self.validar_senha(chave):
            if self.__saldo >= valor:
                self.__saldo -= valor
                return f"\033[32mSAQUE NO VALOR DE R${self.__saldo:,.2f} FEITO COM SUCESSO NA CONTA {self._id}!\033[m\n"
            else:
                return f"\033[31mSALDO INSUFICIENTE NA CONTA {self._id}\033[m\n"
        else:
            return "Senha não confere. Saque não autorizado."

    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self,novonome=None):
        chave = self.pede_senha()

        if self.validar_senha(chave):
            if len(novonome) > 5:
                self._titular = novonome
        else:
            print("Senha não confere. Não posso alterar o nome.")