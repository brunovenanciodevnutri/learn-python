# Crie um programa que gerencia o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois leia a quantidade de gols em cada partida.
# No fim, tudo isso será guardado em um dicionário incluindo o total de gols feitos durante o campeonato.
dic = {'Nome': '',
       'Gols': '',
       'Total': ''}
gol = []
totalgols = 0

dic['Nome'] = str(input('Nome do Jogador: ')).capitalize()
partidas = int(input(f'Quantas partidas {dic['Nome']} jogou? '))
for c in range(partidas):
    gol.append(int(input(f'Quantos gols na partida {c}? ')))
for g in gol:
    totalgols += g
dic['Gols'] = gol[:]
dic['Total'] = totalgols

print('-='*20)
print(dic)
print('-='*20)
for k, v in dic.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*20)
print(f'O jogador {dic['Nome']} jogou {partidas} partidas.')
for k, v in enumerate(dic['Gols']):
    print(f'-> Na partida {k}, fez {v} gols.')
print(f'Foram um total de {dic['Total']} gols.')