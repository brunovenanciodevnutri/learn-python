# Crie um programa que leia nome, ano de nascimento e CTPS e cadastre-os (com idade) em um dicionário. Se por acaso o CTPS for diferente de zero, o dic receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
dic = {'Nome': '',
       'Ano de Nascimento': '',
       'CTPS': ''}

dic['Nome'] = str(input('Nome: ')).capitalize()
dic['Ano de Nascimento'] = int(input('Ano de Nascimento: '))
idade = datetime.now().year - dic['Ano de Nascimento']
dic['CTPS'] = int(input('CTPS: '))

if dic['CTPS'] == 0:
    print('Não tem CTPS.')
else:
    dic['Contratação'] = int(input('Ano de Contratação: '))
    dic['Salário'] = float(input('Salário: R$'))
    dic['Aposentadoria'] = idade + ((dic['Contratação'] + 35) - datetime.now().year)

for k, v in dic.items():
    print(f'- {k} tem o valor {v}.')
