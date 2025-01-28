# Faça um programa que tenha uma função chamada contador() que receba três paramêtros: início, fim e passo e realize a contagem. O programa tem que realizar três contagens através da função criada:
# De 1 até 10, de 1 em 1;
# De 10 até 0, de 2 em 2;
# Uma contagem personalizada.
from time import sleep
def contador(i, f, p):
    print('-=' * 30)
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    if f > i:
        for c in range(i, f+1, p):
            print(f'{c} ', end='', flush=True)
            sleep(0.5)
        print()
    else:
        for c in range(i, f-p, -p):
            print(f'{c} ', end='', flush=True)
            sleep(0.5)
        print()


contador(i = 1, f = 10, p = 1)
contador(i = 10, f = 1, p = 1)

print('-=' * 30)
inicio = int(input('Início: '))
fim = int(input('Fim: '))
pular = int(input('Pular: '))
contador(inicio, fim, pular)