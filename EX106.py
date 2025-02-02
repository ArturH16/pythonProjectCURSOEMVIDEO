def ajuda(a='Fim'):
    while True:
        titulo = 'SISTEMA DE AJUDA PYHELP'
        titulo3 = 'ATÉ LOGO!'
        tam3 = len(titulo3) + 4
        tam = len(titulo) + 4
        print('\033[m\033[042m~' * tam)
        print(f'  {titulo}')
        print('~' * tam)
        pergunta = str(input('\033[mFunção ou Biblioteca ->')).strip()
        if pergunta.upper() == 'FIM':
            print('\033[041m~'*tam3)
            print(f'  {titulo3}')
            print('~'*tam3)
            break
        titulo2 = f'Acessando o manual do comando {pergunta}'
        tam2 = len(titulo2) + 4
        print('\033[044m~'*tam2)
        print(f'  {titulo2}')
        print('~'*tam2)
        print('\033[40;7m',end='')
        ab = f'{help(pergunta)}'


ajuda()




