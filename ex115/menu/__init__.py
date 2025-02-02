def leiaInteiro(msg):
    while True:
        try:
             numero = int(input(msg))
        except (ValueError, TypeError):
                    print('\033[31mERRO! Por favor, digite um número inteiro válido!\033[m')
                    continue
        except KeyboardInterrupt:
                    print('\033[31mO usuário preferiu não digitar o número\033[m')
                    return 0
        else:
            return numero


def tela2(msg2=''):
        if msg2 == '':
            msg2 = 'INSIRA UMA MENSAGEM AQUI'
        tam = 30
        print('-' * tam)
        print(f'{msg2.center(tam)}')
        print('-' * tam)


def tela(msg=''):
    if msg == '':
        msg = 'MENU PRINCIPAL'
    tam = 30
    print('-'*tam)
    print(f'{msg.center(tam)}')
    print('-'*tam)
    print('\033[32m1 - \033[34mVer Pessoas Cadastradas\033[m')
    print('\033[32m2 - \033[34mCadastrar Nova Pessoa\033[m')
    print('\033[32m3 - \033[34mSair do Sistema\033[m')
    print('-'*tam)


def validacao(opcao=0):
    tela()
    opcao = leiaInteiro('\033[32mSua Opção: \033[m')
    return opcao












