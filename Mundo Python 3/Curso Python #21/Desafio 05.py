# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# Quantidade de notas;
# A maior nota;
# A menor nota;
# A média da turma;
# A situação (Opcional).

def notas(* n, sit=False):
    dic = {'Total': 0,
       'Maior': 0,
       'Menor': 0,
       'Média': 0}
    somanotas = 0
    for c in range(len(n)):
        somanotas += n[c]
        if c == 0:
            dic['Maior'] = n[c]
            dic['Menor'] = n[c]
        elif dic['Maior'] < n[c]:
            dic['Maior'] = n[c]
        elif dic['Menor'] > n[c]:
            dic['Menor'] = n[c]
    dic['Total'] = len(n)
    dic['Média'] = somanotas / len(n)
    if sit == True:
        if dic['Média'] >= 6:
            dic['Situação'] = 'APROVADO'
        else:
            dic['Situação'] = 'REPROVADO'
    print(dic)

notas(4, 5, 6, sit=False)

# OU

print('-------------------------------------')
def notas2(* n, sit=False):
    r = {}
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit == True:
        if r['Média'] > 6:
            r['Situação'] = 'APROVADO'
        else:
            r['Situação'] = 'REPROVADO'
    return r

resp = notas2(3, 9, 8, sit=True)
print(resp)