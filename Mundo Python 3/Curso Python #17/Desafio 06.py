# Crie um programa onde usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correto.
exp = str(input('Digite a expressão: '))
pilha = []

for c in exp:
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão não está válida! Tente novamente.')

# OU

lista = []

lista.append(str(input('Digite a expressão: ')))
for c in lista:
    if c.count('(') == c.count(')'):
        print('Sua expressão está válida!')
    else:
        print('Sua expressão não está válida! Tente novamente.')