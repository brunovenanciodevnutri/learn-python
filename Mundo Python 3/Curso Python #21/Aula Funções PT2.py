# INTERACTIVE HELP:

help(print)
print(input.__doc__)

# DOCSTRINGS:

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :para p: passo da contagem
    :return: sem retorno
    Função criada por Bruno Venâncio.
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')

# PARÂMETROS OPCIONAIS:

def somar(a, b, c=0): # Não vai dar erro caso só coloque 2 números pois o "0" diz que caso não tenha um valor pra "c", logo o "c" será anulado.
    s = a + b + c
    print(f'A soma vale {s}.')

somar(3, 2)
print('-----------')

def soma2(a=0, b=0, c=0): # Não vai dar erro caso só coloque 2 números pois o "0" diz que caso não tenha um valor pra "c", logo o "c" será anulado.
    s = a + b + c
    print(f'A soma vale {s}.')

soma2(2)
soma2()
print('-----------')

# ESCOPO DE VARIÁVEIS:

def teste():
    x = 8 # Escopo local
    print(f'Na função teste, n vale {n}.')

n = 2 # Escopo global
print(f'No programa principal, n vale {n}.')
teste()
print('-----------')

def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}.')

n1 = 2
funcao()
print(f'N1 fora vale {n1}.')
print('-----------')

def testando(b):
    global a # Tornei o "a" de dentro da função em um valor global, fora da função também.
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}.')
    print(f'B dentro vale {b}.')
    print(f'C dentro vale {c}.')

a = 5
testando(a)
print(f'A fora vale {a}.')
print('-----------')

# RETORNANDO VALORES:

def somatorio(a=0, b=0, c=0):
    s = a + b + c
    return(s)

r1 = somatorio(3, 2, 5)
r2 = somatorio(2, 2)
r3 = somatorio(1)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')