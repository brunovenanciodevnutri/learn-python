# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: O primeiro que indique o número a calcular e o outro chamado show. que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo fatorial.
from math import factorial
def fatorial(n=0, show=False):
    if show == True:
        for c in range(n, 0, -1):
            if c == 1:
                return f'{c} = {factorial(n)}'
            else:
                print(f'{c} x ', end='')
    else:
        return f'{factorial(n)}'


print(fatorial(20, show=True))