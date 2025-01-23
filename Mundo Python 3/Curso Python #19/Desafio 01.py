# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
dic = {'Nome': '', 'Média': ''}


dic['Nome'] = str(input('Digite o seu nome: ')).capitalize()
dic['Média'] = float(input('Digite a sua média: '))
print(f'Nome é igual a {dic['Nome']}.')
print(f'Média é igual a {dic['Média']}.')
if dic['Média'] >= 6:
    print('Situação é igual a Aprovado!')
else:
    print('Situação é igual a Reprovado!')