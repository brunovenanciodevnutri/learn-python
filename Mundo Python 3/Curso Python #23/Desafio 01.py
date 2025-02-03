# Reescreva a função leiaint() que fizemos no desafio 'DESAFIO FUNÇÃO INPUT', incluindo agora a possibilidade da digitação de um número tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Tivemos um problema com os tipos de dados que você digitou.')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não informar os dados.')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Tivemos um problema com os tipos de dados que você digitou.')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não informar os dados.')
            return 0
        else:
            return n

num = leiaint('Digite um valor: ')
print(f'O valor digitado foi {num}.')
num2 = leiafloat('Digite um valor: ')
print(f'O valor digitado foi {num2}.')