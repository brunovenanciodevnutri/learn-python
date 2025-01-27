# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No fim, mostre:
# Quantas pessoas foram cadastradas;
# A média de idade do grupo;
# Uma lista com todas as mulheres;
# Uma lista com todas as pessoas com a idade acima da média.
dic = {'Nome': '',
       'Sexo': '',
       'Idade': ''}
lista = []
media = 0

while True:
    dic['Nome'] = str(input('Nome: ')).capitalize()
    dic['Sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
    dic['Idade'] = int(input('Idade: '))
    lista.append(dic.copy())
    media += dic['Idade']
    continuar = str(input('Quer continuar [S/N]? ')).upper()[0]
    if continuar == 'N':
        break
print('-=' * 20)
print(f'A) O grupo tem {len(lista)} pessoas.')
media /= len(lista)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for c, v in enumerate(lista):
    if v['Sexo'] == 'F':
        print(f'{v['Nome']}', end=' ')
print()
print(f'D) Lista das pessoas acima da média: ')
for c, v in enumerate(lista):
    if v['Idade'] > media:
        print(f'     ')
        for k, v in v.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')