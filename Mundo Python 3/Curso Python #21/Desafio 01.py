# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se a uma pessoa tem voto NEGA, OPCIONAL ou OBRIGATÓRIO nas eleições.
def voto(n=0):
    idade = 2025 - n
    if idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'
    elif idade >= 16 and idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO NEGADO!'

num = int(input('Ano de nascimento: '))
print(voto(num))