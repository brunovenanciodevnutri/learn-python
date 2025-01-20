# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# Quantos números foram digitados;
# A lista de valores ordenada de forma decrescente;
# Se o valor 5 foi digitado e está ou não na lista.
lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja continuar [S/N]? ')).upper()[0]
    if continuar == 'N':
        break
print(f'Foram digitados no total {len(lista)} números.') # Poderia utilizar um contador, mas preferi o len para menor quantidade de linhas de código.
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é {lista}.')
if lista.count(5) > 0:
    print(f'O número 5 foi digitado na lista.')
else:
    print(f'O número 5 não foi digitado na lista.')