import hashlib

class ContaBancaria:
    """Cria uma conta bancaria e permite fazer saques e depósitos"""

    def __init__(self,id,titular,saldo=0,chave=None):
        if chave is None:
            chave = self.pede_senha()
        senha_bytes = chave.encode("utf-8")
        hash_obj = hashlib.sha256(senha_bytes)
        hash_hex = hash_obj.hexdigest()
        self.__hash = hash_hex


        self._id = id
        self._titular = titular
        self.__saldo = saldo
        print(f"Conta {self._id} criada com sucesso! Saldo atual de R${self.__saldo:,.2f}")

    @property
    def nome(self):
            return self._titular
    @nome.setter
    def nome(self,novo_nome):
        chave = self.pede_senha()
        if self.validar_senha(chave):
            self._titular = novo_nome

    def depositar(self,valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:,.2f} autorizado na conta {self._id}")

    def sacar(self,valor,chave=None):
        if chave is None:
            chave = self.pede_senha()
        if self.validar_senha(chave):
            if valor > 0:
                self.__saldo -=  valor
                print(f"Saque de R${valor:,.2f} autorizado na conta {self._id}")
        else:
            print("Senha não confere. Saque não autorizado!")


    def pede_senha(self):
        senha = input("")
        return senha

    def validar_senha(self,chave):
        senha_bytes = chave.encode("utf-8")
        hash_obj = hashlib.sha256(senha_bytes)
        hash_hex = hash_obj.hexdigest()
        if self.__hash == hash_hex:
             return True
        else:
             return False



