tupla = 'Programador','Pessoa','Amigo','Academia'
for  c in tupla:
    print(f'\nNa palavra {c} temos:',end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')