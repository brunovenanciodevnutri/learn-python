dados = ['Pedro', '25']
pessoas = []

pessoas.append(dados[:]) # Foi criada uma lista dentro de outra lista, onde 'Pedro' [0] e '25' [1] tornam-se 'Pedro 25' [0].
# Exemplo: pessoas = [['Pedro, 25], ['Maria', 19]] > print(pessoas[0][0]) == Pedro.

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13]]
print(galera[2][1])

gente = []
dado = []
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    gente.append(dado[:])
    dado.clear()
print(gente)

for p in gente:
    if p[1] >= 21: # Se a idade for maior ou igual a 21.
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')