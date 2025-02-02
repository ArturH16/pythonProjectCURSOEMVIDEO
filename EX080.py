lista = []
for c in range(0,4):
    r = int(input('Digite um valor'))
    if c ==0 or r > lista[-1]:
        lista.append(r)
    else:
        pos = 0
        while pos < len(lista):
            if r <= lista[pos]:
                lista.insert(pos,r)
                break
            pos += 1
print(lista)







print(lista)