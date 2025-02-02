firstnumber = float(input('Digite o primeiro valor:'))
secondnumber = float(input('Digite o segundo valor:'))
if firstnumber > secondnumber:
    print('O {} é maior'.format(firstnumber))
elif secondnumber > firstnumber:
    print('O {} é maior'.format(secondnumber,))
else:
    print('Não há valor maior, os dois são iguais')