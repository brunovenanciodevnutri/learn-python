# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somapar():
# A primeira função vai sortar 5 números e colocá-los dentra da lista;
# A segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep
lista = []

def sorteio(* num):
    print(f'Sorteando os 5 valores da lista: ', end='')
    for c in range(0, 5):
        c = randint(1, 10)
        print(f'{c} ', end= '', flush=True)
        sleep(0.5)
        lista.append(c)
    print()

def somapar(lista):
    pos = 0
    soma = 0
    print(f'Somando os valores pares de {lista}, temos: ', end='')
    while pos < len(lista):
        if lista[pos] % 2 == 0:
            soma += lista[pos]
            pos += 1
        else:
            pos += 1
    print(soma)

sorteio()
somapar(lista)