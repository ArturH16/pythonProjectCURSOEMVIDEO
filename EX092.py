import datetime
agora = datetime.datetime.now().year
dici = {}
while True:
    dici['Nome'] = str(input('Nome:'))
    dici['Idade'] = agora - int(input('Ano de Nascimento: '))
    dici['CTPS'] = int(input('Carteira de Trabalho ( 0 se não tiver): '))
    if dici['CTPS'] != 0:
        dici['Ano de Contratação'] = int(input('Ano de Contratação:'))
        dici['Salário'] = int(input('R$: '))
        dici['Aposentadoria'] = dici['Idade'] + (35 - (agora - dici['Ano de Contratação']))
    for k,v in dici.items():
        print(f'{k} recebe {v}')

