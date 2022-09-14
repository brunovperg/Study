
def pita():
    a = float(input("Valor do primeiro cateto: "))
    b = float(input("Valor do segundo cateto: "))

    c = ((a**2)+(b**2))**(1/2)

    print(f"Valor da hipotenusa é: {round(c,2)}")

pita()

