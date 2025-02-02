def leiadinheiro(money):
    valido = False
    while not valido:
        verificador = str(input(money)).replace(',','.').strip()
        if verificador.isalpha() or verificador == '':
            print(f'\033[31mERRO! \"{verificador}\" é um preço inválido\033[m')
        else:
            valido = True
            return  float(verificador)







