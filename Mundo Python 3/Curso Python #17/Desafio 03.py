# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta (sem usar o sort()). No fim, mostre a lista ordenada.
lista = []

for c in range(0, 5):
    n = (int(input('Digite um valor: ')))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    elif c == 1 and n < lista[0]:
        lista.insert(0, n)
    elif c == 2 and n >= lista[0] and n <= lista[1]:
        lista.insert(1, n)
    elif c == 2 and n <= lista[0]:
        lista.insert(0, n)
    elif c == 3 and n >= lista[0] and n <= lista[1]:
        lista.insert(1, n)
    elif c == 3 and n >= lista[0] and n <= lista[2]:
        lista.insert(2, n)
    elif c == 3 and n <= lista[0]:
        lista.insert(0, n)
    elif c == 4 and n >= lista[0] and n <= lista[1]:
        lista.insert(1, n)
    elif c == 4 and n >= lista[0] and n <= lista[2]:
        lista.insert(2, n)
    elif c == 4 and n >= lista[0] and n <= lista[3]:
        lista.insert(3, n)
    elif c == 4 and n <= lista[0]:
        lista.insert(0, n)
print(f'Os valores são {lista}')

# OU

lista2 = []

for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > lista2[-1]:
        lista2.append(num)
        print(f'Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista2):
            if num <= lista2[pos]:
                lista2.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1
print(f'Os valores são {lista2} /2')