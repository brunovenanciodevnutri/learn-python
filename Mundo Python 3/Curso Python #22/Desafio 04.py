# Adicione ao módumo 'moeda.py' uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que temos no módulo criado até aqui.
from modulos.uteis.moeda import *

p = float(input('Digite o preço: R$'))
resumo(p, 80, 35)