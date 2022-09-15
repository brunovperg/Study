
############### CALCULO IMC ##################

def IMC():
    while True:
        massa = float(input("\nDigite uma massa em kg: "))
        altura = float(input("Digite uma altura em cm: "))
        imc = (massa/(altura**2))*10000

        print(f"\nSeu IMC é: {round(imc, 2)}")
        
        if imc < 18.5:
            print("\nVocê está abaixo do peso ideal")
        elif 18.5 <= imc < 25:
            print("\nVocê está no peso ideal")
        elif 25 <= imc < 30:
            print("\nVocê está acima do peso ideal")
        elif 30 <= imc < 35:
            print("\nVocê está com Obesidade Grau I")
        elif 35 <= imc < 40:
            print("\nVocê está com Obesidade Grau II")
        else:
            print("\nVocê está com Obesidade Grau III")

IMC()