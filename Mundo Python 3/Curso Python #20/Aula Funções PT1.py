def linha():
    print('------------------------------')

linha()
print('      SISTEMA DE ALUNOS')
linha()
linha()
print('      CADASTRO DE ALUNOS')
linha()

# OU

def titulo(msg):
    linha()
    print(msg)
    linha()

titulo('      SISTEMA DE ALUNOS')
titulo('      CADASTRO DE ALUNOS')

# OU

def soma(a, b):
    s = a + b
    print(f'A = {a} e B = {b}')
    print(f'A soma A + B = {s}')

soma(4, 5)
soma(a=4, b=5)

# OU

def contador(* num):
    for v in num:
        print(f'{v} ', end='-> ')    

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

# OU

print()
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

# OU

def soma2(* valores2):
    s = 0
    for num in valores2:
        s += num
    print(f'Somando os valores {valores2} temos {s}')

soma2(5, 2)
soma2(2, 9, 4)