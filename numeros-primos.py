
############ NUMEROS PRIMOS ###################

numPrimos=[]
numeroMax = int(input("Descobrir numeros primos até: "))
for numero in range(numeroMax):
    div=0
    for divisor in range(1, numero+1):
        if(numero % divisor) == 0:
            div+=1
    if div==2:
        numPrimos.append(numero)

print(numPrimos)
qntdPrimos = 0
for primes in numPrimos:
    qntdPrimos+=1
