firstvalor = int(input('Digite o primeiro valor:'))
secondvalor = int(input('Digite o segundo valor:'))
thirdvalor = int(input('Digite o terceiro valor:'))
if firstvalor > secondvalor and firstvalor > thirdvalor:
    print('O maior valor digitado foi {}'.format(firstvalor))
if secondvalor > firstvalor and secondvalor > thirdvalor:
    print('O maior valor digitado foi: {}'.format(secondvalor))
if thirdvalor > secondvalor and  thirdvalor > firstvalor:
    print('O maior valor digitado foi {}'.format(thirdvalor))
if firstvalor < secondvalor and  firstvalor < thirdvalor:
    print('O menor valor digitado foi: {}'.format(firstvalor))
if secondvalor < firstvalor and  secondvalor < thirdvalor:
    print('O menor valor digitado foi: {}'.format(secondvalor))
if thirdvalor < firstvalor and  thirdvalor < secondvalor:
    print('O menor valor digitado foi: {}'.format(thirdvalor))
if firstvalor == secondvalor and firstvalor == thirdvalor:
    print('Todos os números tem o mesmo valor')
