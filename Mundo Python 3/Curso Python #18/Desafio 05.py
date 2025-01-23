# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
lista = []
temp = []

while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Nota 1: ')))
    temp.append(int(input('Nota 2: ')))
    media = (temp[1] + temp[2]) / 2
    temp.append(media)
    lista.append(temp[:])
    temp.clear()
    continuar = str(input('Quer continuar [S/N]? ')).upper()[0]
    if continuar == 'N':
        break
print('-='*13)
print(f'{'Nº':<4}{'NOME':<10}{'MÉDIA':>8}')
print('--------------------------')
for c in range(len(lista)):
    print(f'{c:<4}{lista[c][0]:<10}{lista[c][3]:>8.1f}')
print('--------------------------')
while True:
    aluno = int(input('Mostrar notas de qual aluno? (999 STOP): '))
    print(f'Notas de {lista[aluno][0]}: {lista[aluno][1]} e {lista[aluno][2]}.')
    if aluno == 999:
        break
