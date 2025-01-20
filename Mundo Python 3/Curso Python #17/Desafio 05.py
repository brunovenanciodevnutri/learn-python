# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
lista = []
par = []
impar = []

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    continuar = str(input('Quer continuar [S/N]? ')).upper()[0]
    if continuar == 'N':
        break
print(f'Lista Principal: {lista}. \nLista PAR: {par}. \nLista IMPAR: {impar}.')