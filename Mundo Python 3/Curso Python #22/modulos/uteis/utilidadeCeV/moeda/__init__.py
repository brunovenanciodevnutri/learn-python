def metade(n=0, m='R$', sit=False):
    n /= 2
    if sit == True:
        return(f'{m}{n:.2f}'.replace('.', ','))
    else:
        return n


def dobro(n=0, m='R$', sit=False):
    n *= 2
    if sit == True:
        return(f'{m}{n:.2f}'.replace('.', ','))
    else:
        return n
    
def aumentar(n=0, j=0, m='R$', sit=False):
    juros = (n * j) / 100
    juros += n
    if sit == True:
        return(f'{m}{n:.2f}'.replace('.', ','))
    else:
        return juros

def diminuir(n=0, j=0, m='R$', sit=False):
    desconto = (n * j) / 100
    desconto = n - desconto
    if sit == True:
        return(f'{m}{n:.2f}'.replace('.', ','))
    else:
        return desconto


def moeda(n=0, m='R$'):
    return(f'{m}{n:.2f}'.replace('.', ','))

def resumo(n=0, j=0, d=0):
    metade = n / 2
    dobro = n * 2
    juros = ((n * j) / 100) + n
    desconto = n - ((n * d) / 100)
    print('-='*20)
    print('RESUMO DO VALOR'.center(40))
    print('-='*20)
    print(f'Preço analisado: \tR${n:.2f}'.replace('.', ','))
    print(f'Dobro do preço: \tR${dobro:.2f}'.replace('.', ','))
    print(f'Metade do preço: \tR${metade:.2f}'.replace('.', ','))
    print(f'{j}% de aumento: \tR${juros:.2f}'.replace('.', ','))
    print(f'{d}% de redução: \tR${desconto:.2f}'.replace('.', ','))
    print('-' * 40)