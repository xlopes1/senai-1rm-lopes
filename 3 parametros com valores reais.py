print ("Qual o numero maior? ")

n1 =int(input("Informe seu primeiro numero: "))
n2 =int(input("Informe seu segundo numero: "))
n3 =int(input("Informe seu terceiro numero: "))

maior = n1

if (n2 > maior):
  maior = n2

if (n3 > maior):
   maior = n3

print("Seu numero Maior e :", maior)

