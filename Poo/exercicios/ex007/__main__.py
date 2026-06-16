from ex007 import ContaBancaria

def main():
    c1 = ContaBancaria(111,"Maria",5000)
    c1.depositar(-500)
    c1._titular = "Pedro" #Ele deixa, mas não faça pois 'Adultos estão consentindo'...
    c1._ContaBancaria__saldo = 0 #Ele deixa, mas não faça pois 'Adultos estão consentindo'...
    print(c1)

if __name__ == "__main__":
        main()