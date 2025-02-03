def leiaDinheiro(msg):
    valido = False
    while True:
        n = input(msg)
        if n.isnumeric():
            valido = True
            return float(n)
        else:
            print(f'ERRO: "{n}" é um preço inválido!')
        if valido == True:
            break