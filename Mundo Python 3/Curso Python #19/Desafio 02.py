# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionários.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
dic = {'Jogador 1': randint(1, 6),
       'Jogador 2': randint(1, 6),
       'Jogador 3': randint(1, 6),
       'Jogador 4': randint(1, 6)}
ranking = []

print('Valores sorteados:')
for k, v in dic.items():
    print(f'O {k} tirou {v}.')
    sleep(1)
print('Ranking dos Jogadores:')

ranking = sorted(dic.items(), key=itemgetter(1), reverse=True) # O itemgetter serviu para recuperar apenas os [1] valores do dicionário, assim podendo colocar em ordem descrecente.
print(ranking)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)