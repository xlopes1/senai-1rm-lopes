print("Digite o número para abrir o menu de opção:")
n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))
d = 0
while d != 5:
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos númeors
[5] sair do programa''')
    d = int(input("Digite: "))
    if d == 1:
        print("A soma é: {}".format(n1+n2))
    elif d == 2:
        print("A multiplicação é: {}".format(n1*n2))
    elif d == 3:
        if n1 > n2:
            print("O maior é: {}".format(n1))
        else:
            print("O maior é {}".format(n2))
    elif d == 4:
        n1 = float(input("Primeiro número: "))
        n2 = float(input("Segundo número: "))
    else:
        print("Número inválido.DIGITE NOVAMENTE")
        
        print("Fim")