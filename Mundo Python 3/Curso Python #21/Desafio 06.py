# Faça um mini sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar 'FIM' será encerrado.

while True:
    print('\033[1;49;93m~\033[m' * 30)
    print('\033[1;49;93m   SISTEMA DE AJUDA PyHELP   \033[m')
    print('\033[1;49;93m~\033[m' * 30)
    n = str(input('Função ou Biblioteca > '))
    if n == 'FIM':
        print('~' * 40)
        print('Encerrando...')
        break
    print('\033[1;34;34m~\033[m' * 40)
    print(f'\033[1;44;93m   Acessando o manual de comando {n}   \033[m')
    print('\033[1;34;34m~\033[m' * 40)
    help(n)

# OU

c = ('\033[m',         # 0 - sem cores
    '\033[0;30;41m',   # 1 - vermelho
    '\033[0;30;42m',   # 2 - verde
    '\033[0;30;43m',   # 3 - amarelo
    '\033[0;30;44m',   # 4 - azul
    '\033[0;30;45m',   # 5 - roxo
    '\033[7;30m',      # 6 - branco
    );

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        print('Encerrando...')
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
