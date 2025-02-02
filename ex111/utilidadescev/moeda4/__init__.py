def metade(num=0,moeda4='R$',f=False):
    res = num / 2
    if f:
        return f'{moeda4}{res:.2f}'.replace('.', ',')
    return res



def dobro(num=0,moeda4='R$',f=False):
    res =  num * 2
    if f:
        return f'{moeda4}{res:.2f}'.replace('.', ',')
    return res


def aumentar(num=0,aumento=0,moeda4='R$',f=False):
    res = num * (1 + (aumento/100))
    if f:
        return f'{moeda4}{res:.2f}'.replace('.', ',')
    return res


def diminuir(num=0,diminuicao=0,moeda4='R$',f=False):
    res = num * (1 - (diminuicao/100))
    if f:
        return f'{moeda4}{res:.2f}'.replace('.', ',')
    return res


def moeda(num=0,moeda4='R$',f=False):
    if f:
        return f'{moeda4}{num:.2f}'.replace('.',',')
    return f'{num}'


def resumo(valor=0,a=0,d=0):
    frase = 'RESUMO DO VALOR'
    tot = len(frase) + 4
    print('-'*tot)
    print(f'  {frase}')
    print('-'*tot)
    print('-='*30)
    print(f'Preço Analisado:   {moeda(valor,f=True)}')
    print(f'Dobro do Preço:    {dobro(valor,f=True)}')
    print(f'Metade do Preço:   {metade(valor,f=True)}')
    print(f'{a}% de Aumento:   {aumentar(valor,aumento=a,f=True)}')
    print(f'{a}% de Redução:   {diminuir(valor,diminuicao=a,f=True)} ')
    print('-='*30)