# Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante a função input() do Python, só que fazendo a validação para aceitar apenas um valor numério.
def leiaint(msg):
    OK = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            int(n)
            OK = True
            return n
        else:
            print('ERRO! Digite um número inteiro válido.')
        if OK == True:
            break


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')