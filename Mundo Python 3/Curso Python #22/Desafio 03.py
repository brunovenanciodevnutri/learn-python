# Modifique as funções que foram criadas no DESAFIO ANTERIOR, para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda().
from modulos.uteis.moeda import *

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda(p)} é {metade(p, sit=True)}')
print(f'O dobro de {moeda(p)} é {dobro(p, sit=True)}')
print(f'Aumentando 10% temos {aumentar(p, 10, sit=True)}')
print(f'Reduzindo 15% temos {diminuir(p, 15, sit=True)}')