# Faça um programa que leia nome e peso de várias pessoas guardando em uma lista. No final, mostre:
# Quantas pessoas foram cadastradas;
# Uma listagem com as pessoas mais pesadas;
# Uma listagem com as pessoas mais leves.
dados = []
listacompleta = []
maior = ['', 0]
menor = ['', 0]

while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    listacompleta.append(dados[:])
    dados.clear()
    continuar = str(input('Quer continuar [S/N]? ')).upper()[0]
    if continuar == 'N':
        for c, p in enumerate(listacompleta):
            if c == 0:
                dados.append(p)
                maior = dados[:]
                menor = dados[:]
            elif p[1] > maior[0][1]:
                dados.append(p)
                maior = dados[:]
            elif p[1] < menor[0][1]:
                dados.append(p)
                menor = dados[:]
            dados.clear()
        break

print(f'No total foram cadastradas {len(listacompleta)} pessoas.')

print(f'O maior peso foi de {maior[0][1]}Kg. Peso de ', end='')
for p in listacompleta:
    if p[1] == maior[0][1]:
        print(f'{p[0]} ', end='')
        
print(f'\nO menor peso foi de {menor[0][1]}Kg. Peso de ', end='')
for p in listacompleta:
    if p[1] == menor[0][1]:
        print(f'{p[0]} ', end='')
print('')

# OU

temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    elif temp[1] > mai:
        mai = temp[1]
    elif temp[1] < men:
        men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar [S/N]? ')).upper()[0]
    if resp == 'N':
        break
print(f'No total foram cadastradas {len(princ)} pessoas.')

print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]} ', end='')

print(f'\nO menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'{p[0]} ', end='')