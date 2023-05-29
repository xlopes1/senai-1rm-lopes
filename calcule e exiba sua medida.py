print ("Calcule sua média")
num1 = float(input("Digite sua nota 1:"))
num2 = float(input("Digite sua nota 2:"))
num3 = float(input("Digite sua nota 3:"))
media = (num1 + num2 + num3) / 3
print (f"Sua média final é: {media}")
if media >= 6 :
    print("aprovado")   
else:
    print("reprovado")