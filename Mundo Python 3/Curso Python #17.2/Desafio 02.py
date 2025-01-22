# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e impares.
# No final, mostre os valores pares e impares em ordem crescente.
lista = [[], []]

for c in range(0, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        lista[0].insert(0, n)
    else:
        lista[1].insert(0, n)
lista[0].sort()
lista[1].sort()
print(lista)