######################## SEQUENCIA FIBONACCI #####################

def contador():
    controle=1

    while controle==1:
        num=int(input("Digite quantos elementos deseja: "))
        a, b = 0, 1
        cont=2
        print("Sequencia Fibonacci")
        print(a,b, end=" ")
        while cont<num:
            a,b = b, a+b
            print(b, end=" ")
            cont+=1
        print()

        controle = int(input("Digite 0 para parar ou 1 para continuar: "))
    # contador()

contador()
