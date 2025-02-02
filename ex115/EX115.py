from ex115 import menu
from ex115.arquivo import *
from time import sleep

arq = 'cursoemvídeo'
if not arquivoexiste(arq):
    criararquivo(arq)
while True:
    resposta = menu.validacao()
    if resposta == 1:
        leiaarquivo(arq)
    elif resposta == 2:
        menu.tela2('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInteiro('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        menu.tela2('SAINDO DO SISTEMA... ATÉ LOGO')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida\033[m')
    sleep(1)


