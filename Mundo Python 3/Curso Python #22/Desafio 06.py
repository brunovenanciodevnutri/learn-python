# Dentro do pacote 'utilidadesCeV' que criamos, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input() mas com validação de dados para aceitar apenas valores que sejam monetários.
from modulos.uteis.utilidadeCeV.moeda import *
from modulos.uteis.utilidadeCeV.dado import *

p = leiaDinheiro('Digite o preço: R$')
resumo(p, 80, 35)