def fatorial(n):
    f=1
    for c in range(1, n+1):
        f *= c
    return f

def triplo(n):
    return n * 3

def metade(n):
    n /= 2
    return n

def dobro(n):
    n *= 2
    return n

def aumentar(n, j):
    juros = (n * j) / 100
    juros += n
    return juros

def diminuir(n, j):
    desconto = (n * j) / 100
    desconto = n - desconto
    return desconto