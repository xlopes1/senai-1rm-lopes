salario = float(input("Digite o valor do seu salario atual "))
Salariosup = salario *0.10
salarioinf = salario *0.15
novosalario = Salariosup + salario 
novosalario2 = salarioinf + salario 
print("Seu salario com reajuste é: {} {}".format(novosalario,novosalario2))
if novosalario >= 8250 : 
    print("Aumento de 10% ")   
elif novosalario2 < 8250 :
    print("Aumento de 15% ")
