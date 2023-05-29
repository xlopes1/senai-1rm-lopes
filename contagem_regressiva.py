from time import sleep
print("CONTAGEM REGRESSIVA ATE 0:")
n1 =int(input("Informe o numero: "))
for cont in range(n1, -1, -1):
    print(cont)
    sleep (1)
