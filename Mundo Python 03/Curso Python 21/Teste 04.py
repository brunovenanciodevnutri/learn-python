def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
print(par(num))

#OU PARA COMPLEMENTAR:

if par(num):
    print('É par!')
else:
    print('Não é par!')