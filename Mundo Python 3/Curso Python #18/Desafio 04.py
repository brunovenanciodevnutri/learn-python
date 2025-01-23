# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai pergutar quantos jogos serão gerador e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando em uma lista composta.
from random import randint
from time import sleep
lista = []
temp = []

n = int(input('Quantos jogos você quer que sorteie? '))
print('-=-=-=-= SORTEANDO JOGOS =-=-=-=-')
for c in range(0, n):
    for j in range(0, 6):
        sorteio = randint(1, 60)
        temp.append(sorteio)
    temp.sort()
    lista.append(temp[:])
    temp.clear()
    sleep(1)
    print(f'Jogo {c+1}: {lista[c]}')
print('-=-=-=-= < BOA SORTE > =-=-=-=-')