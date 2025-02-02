def leiaInteiro(msg):
    validador = True
    global numero1
    numero1 = 0
    while validador:
        try:
             numero = int(input(msg))
        except (ValueError, TypeError):
                    print('\033[31mERRO! Por favor, digite um número inteiro válido!\033[m')
        except KeyboardInterrupt:
                    print('\033[31mO usuário preferiu não digitar o número\033[m')
                    numero = 0
                    numero1 = numero
                    validador = False
        else:
            numero1 = numero
            validador = False


def leiaReal(msg2):
    numero2 = 0
    validadoreal = True
    while validadoreal:
        try:
            valorreal = float(input(msg2))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número real válido!\033[m')
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar o número\033[m')
            print(f'O valor inteiro digitado foi {n} e o valor real digitado foi 0')
            validadoreal = False
        else:
            numero2 = valorreal
            validadoreal = False

    print(f'O valor inteiro digitado foi {numero1} e o valor real digitado foi {numero2}')


n = leiaInteiro('Digite um número inteiro: ')
n2 = leiaReal('Digite um número real: ')













