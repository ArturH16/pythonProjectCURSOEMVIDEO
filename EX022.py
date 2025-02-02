x = input('Digite seu nome completo').strip()
print('Seu nome completo com todas as letras maiúsculas fica assim: {}'.format(x.upper()))
print('Seu nome completo com todas as letras minúsculas fica assim: {}'.format(x.lower()))
print('Seu nome ao todo tem {} letras.'.format(len(x) - x.count(' ')))
firstname = x.split()[0]
print('Seu primeiro nome tem {} letras.'.format(len(firstname)))
