print ("Converta Reais em Dolares: ")
Valor =float(input("Valor a ser convertido: "))
print ("\n1. Converter real para dolar")
print ("\n2. Converter dolar para real")
converter1 = Valor / 4.91
converter2 = Valor * 4.91
opção = int(input("Sua opção: "))
if opção == 1 :
    print ("Sua conversão de real para dolar é: ${}".format(converter1))
elif opção == 2 : 
    print ("Sua conversão de dolar para real é: R${}".format(converter2))
else:
    print ("Valor invalido seu jumento")
