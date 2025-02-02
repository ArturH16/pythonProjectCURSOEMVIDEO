x = str(input('Se você digitar a cidade que você nasceu e ela começar por santo, o programa retornará verdadeiro')).strip()
n = x.lower().split()
b = n[0]
if b== 'santo':
    a= True
    print(a)
else:
    print('False')