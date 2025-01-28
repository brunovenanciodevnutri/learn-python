# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
def maior(* valores):
    maiorn = 0
    print('Analisando os valores recebidos...')
    for num in valores:
        print(f'{num} ', end= '', flush=True)
        sleep(0.5)
        if num > maiorn:
            maiorn = num
    print(f'Foram informados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi {maiorn}.')
    print('-=' * 30)

print('-=' * 30)
maior(2, 4, 3, 8)
maior(7, 1, 2, 4)