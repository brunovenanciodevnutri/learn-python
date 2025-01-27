# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (L x C) e mostre a área m² do terreno.
def area(a, b):
    a = float(input('LARGURA (m): '))
    b = float(input('COMPRIMENTO (m): '))
    m = a * b
    print(f'A área de um terreno {a}x{b} é de {m}m².')

area(a=0, b=0)

# OU

def terreno(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')

l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
terreno(l, c)