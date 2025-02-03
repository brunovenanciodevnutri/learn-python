# Crie um pacote chamado utilidadeCeV que tenha dois módulos internos chamados moeda() e dado().
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
from modulos.uteis.utilidadeCeV.moeda import *

p = float(input('Digite o preço: R$'))
resumo(p, 80, 35)