from datetime import date
p = int(input('Que ano quer analisar? Coloque 0 para o ano atual:'))
if p == 0:
    p = date.today().year
m = p % 4 and p % 100 or p % 400
if m == 0:
    print('O ano {} é bissexto!'.format(p))
else:
    print('O ano {} NÃO é bissexto!'.format(p))

