def voto(v=0):
    import datetime
    atual = datetime.date.today().year
    ano = atual - v
    if ano < 16:
        return f'Com {ano} anos: NÃO VOTA'
    elif 16 <= ano < 18 or ano > 65:
        return f'Com {ano} anos: VOTO OPCIONAL'
    else:
        return f'Com {ano} anos: VOTO OBRIGATÓRIO'


#Programa Principal
print('-'*20)
a = int(input('Em que ano você nasceu?'))
print(voto(a))




