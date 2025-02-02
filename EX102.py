def fatorial(v,show=False):
    """
    -> Calcula o Fatorial de um número
    :param v: o número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: o valor do fatorial de um número v
    """
    print('-'*40)
    f = 1
    for c in range(v,0,-1):
        f *= c
    if show:
        for c in range(v,0,-1):
            print(f'{c}', end='')
            print(' x ' if c > 1 else ' = ', end='')
        return f'{f}'
    else:
        return f


help(fatorial)
print(fatorial(6))





