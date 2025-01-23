# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
matriz = [['0', '1', '2',],
          ['0', '1', '2',],
          ['0', '1', '2']]
temp = []

for c, v in enumerate(matriz):
    for c2 in range(len(matriz)):
        temp.append(int(input(f'Digite um valor [{c, c2}]: ')))
        matriz[c][c2] = temp[:]
        temp.clear()

for c in matriz:
    print(c)