<<<<<<< HEAD
######################## CONTAGEM E SOMA EM TABELA COM WHILE ######################################
cont = 1
soma = 0

print("Interacao do while \tCondicao testada\tcont\tsoma")
numMax = int(input("Somar números até: "))
while cont <=numMax:
    soma+=cont
    status = cont <=numMax
    print(f"{cont}a vez\t\t\t{status}\t\t\t{cont}\t{soma}")
    cont+=1
status = cont<=numMax
=======
######################## CONTAGEM E SOMA EM TABELA COM WHILE ######################################
cont = 1
soma = 0

print("Interacao do while \tCondicao testada\tcont\tsoma")
numMax = int(input("Somar números até: "))
while cont <=numMax:
    soma+=cont
    status = cont <=numMax
    print(f"{cont}a vez\t\t\t{status}\t\t\t{cont}\t{soma}")
    cont+=1
status = cont<=numMax
>>>>>>> 8f69615397bbb9a044236392521906546b2babae
print(f"Fim do While\t\t{status}\t\t\t{cont}\t{soma}")