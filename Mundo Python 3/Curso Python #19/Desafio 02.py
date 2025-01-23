# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionários.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
dic = {'Jogador 1': randint(1, 6),
       'Jogador 2': randint(1, 6),
       'Jogador 3': randint(1, 6),
       'Jogador 4': randint(1, 6)}

print('Valores sorteados:')
for k, v in dic.items():
    print(f'O {k} tirou {v}.')
print('Ranking dos Jogadores:')

maior = 0
for k, v in dic.items():
    if v > maior:
        maior = v
        dic['Jogador 1'] = v

    print(maior)