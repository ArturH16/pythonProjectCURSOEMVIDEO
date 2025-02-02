R = str(input('Digite uma expressão algébrica:'))
if R.count("(") == R.count(")"):
    print('A expressão está CERTA!')
else:
    print('A expressão está ERRADA!')
