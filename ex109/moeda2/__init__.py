def metade(num=0,moeda2='R$',f=False):
    res = num / 2
    if f:
        return f'{moeda2}{res:.2f}'.replace('.', ',')
    return res



def dobro(num=0,moeda2='R$',f=False):
    res =  num * 2
    if f:
        return f'{moeda2}{res:.2f}'.replace('.', ',')
    return res


def aumentar(num=0,aumento=0,moeda2='R$',f=False):
    res = num * (1 + (aumento/100))
    if f:
        return f'{moeda2}{res:.2f}'.replace('.', ',')
    return res


def diminuir(num=0,diminuicao=0,moeda2='R$',f=False):
    res = num * (1 - (diminuicao/100))
    if f:
        return f'{moeda2}{res:.2f}'.replace('.', ',')
    return res


def moeda(num=0,moeda2='R$',f=False):
    if f:
        return f'{moeda2}{num:.2f}'.replace('.',',')
    return f'{num}'



