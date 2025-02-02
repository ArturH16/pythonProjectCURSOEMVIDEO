tupla ='zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte',
numero = int(input('Digite um número de 0 a 20:'))
print(tupla[numero])
if numero > 20 or numero < 0:
    print('Tente novamente.Digite um número de 0 a 20: ')
    numero = int(input('Digite um número de 0 a 20:'))
    print(tupla[numero])