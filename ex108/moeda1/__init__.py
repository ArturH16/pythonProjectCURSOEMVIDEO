def metade(num=0):
    res = num / 2
    return res


def dobro(num=0):
    res =  num * 2
    return res


def aumentar(num=0,aumento=0):
    res = num * (1 + (aumento/100))
    return res


def diminuir(num=0,diminuicao=0):
    res = num * (1 - (diminuicao/100))
    return res


def moeda(num=0,moeda1='R$'):
    return f'{moeda1}{num:.2f}'.replace('.',',')