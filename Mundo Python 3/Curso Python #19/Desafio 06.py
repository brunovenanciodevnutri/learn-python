# Aprimore o DESAFIO DOS JOGADORES para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
dic = {'Nome': '',
       'Gols': '',
       'Total': ''}
lista = []
gol = []

while True:
    totalgols = 0
    gol.clear()
    dic.clear()
    dic['Nome'] = str(input('Nome do Jogador: ')).capitalize()
    partidas = int(input(f'Quantas partidas {dic['Nome']} jogou? '))
    for c in range(partidas):
        gol.append(int(input(f'Quantos gols na partida {c}? ')))
    for g in gol:
        totalgols += g
    dic['Gols'] = gol[:]
    dic['Total'] = totalgols
    lista.append(dic.copy())
    continuar = str(input('Quer continuar [S/N]? ')).upper()[0]
    if continuar == 'N':
        print('-=' * 20)
        print(lista)
        print('-=' * 20)
        break
    print('----------------------------')

print(f'{'Nº':<4}{'NOME':<13}{'GOLS'}{'TOTAL':>18}')
print('-' * 40)
for c, v in enumerate(lista):
    print(f'{c:<4}{v['Nome']:<13}{v['Gols']}{v['Total']:>14}')
print('-' * 40)
while True:
    levantamento = int(input('Mostrar dados de qual jogador? '))
    for c, v in enumerate(lista):
        if c == levantamento:
            print(f'-> LEVANTAMENTO DO JOGADOR {v['Nome']}:')
            for c, g in enumerate(v['Gols']):
                print(f'  No jogo {c} fez {g} gols.')
    if levantamento == 999:
        break
print('<< VOLTE SEMPRE >>')