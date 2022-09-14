############### CALCULO IMC ##################

def IMC():
    massa = float(input("Digite uma massa em kg: "))
    altura = float(input("Digite uma altura em cm: "))
    imc = massa/(altura**2)

    print(f"Seu IMC é: {imc*10000}")

IMC()