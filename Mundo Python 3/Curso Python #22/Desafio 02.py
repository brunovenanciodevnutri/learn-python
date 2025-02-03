# Adapte o código do DESAFIO ANTERIOR, criando uma função adicional chamada moeda(), que consiga mostrar os valores como um valor monetário formatado.
from modulos.uteis.moeda import *

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda(p)} é {moeda(metade(p))}')
print(f'O dobro de {moeda(p)} é {moeda(dobro(p))}')
print(f'Aumentando 10% temos {moeda(aumentar(p, 10))}')
print(f'Reduzindo 15% temos {moeda(diminuir(p, 15))}')