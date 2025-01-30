# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum não tenha sido informado corretamente.
def ficha(n='<desconhecido>', g=0):
    print('-=' * 30)
    n = str(input('Nome do Jogador: ')).capitalize()
    if n == '':
        n = '<desconhecido>'
    g = str(input('Número de Gols: '))
    if g.isnumeric():
        g = int(g)
    else:
        g = 0
    return f'O jogador {n} fez {g} gol(s) no campeonato.'

print(ficha())