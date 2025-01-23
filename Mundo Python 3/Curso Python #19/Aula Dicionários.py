# Dicionários {}
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])

dados['Sexo'] = 'M'
print(dados)

del dados['idade']
print(dados)

print('--------------------')

filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'
         }

print(filme.values())
print(filme.keys())
print(filme.items())

print('--------------------')

for k, v in filme.items():
    print(k, v)

print('--------------------')

brasil = []
estado1 = {'uf': 'Rio deJaneiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)

print('--------------------')

estado = {}
brasill = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasill.append(estado.copy()) # Nos Dicionários não é utilizado [:] mas sim o comando .copy().
print(brasill)
for e in brasill:
    for v in e.values():
        print(v, end=' ')
    print()