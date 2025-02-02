num = int(input('Digite um número inteiro:'))
divisores = 0
for c in range (1,num + 1):
   if num % c == 0:
       divisores += 1
       print('\033[32:1m{} '.format(c),end = '')
   else:
       print('\033[31:1m{} '.format(c), end = '')
print('\n \033[mO número {} teve um total de {} divisores'.format(num,divisores))
if divisores == 2:
    print(' O número {} é PRIMO!'.format(num))
else:
    print('O número {} NÃO é PRIMO!'.format(num))