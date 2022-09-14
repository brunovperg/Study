<<<<<<< HEAD
##### MINI CALCULADORA ############

controle = 1
while True:
    print('\nMini calculadora')
    print()
    print('1 - Somar dois números')
    print('2 - Subtrair dois números')
    print('3 - Multiplicar dois números')
    print('4 - Dividir dois números')
    print('5 - Fatorial de um número')
    print('6 - Potência entre dois números')
    print('7 - SAIR')
    print()
    #### SAIR
    controle = int(input('Escolha uma opção: '))
    if controle==7:
        print('\n-------------------------------------------------', end='\n')
        print("\nFIM DA CALCULADORA")
        print('\n-------------------------------------------------', end='\n')
        break
    print('-------------------------------------------------', end='\n')
    
    
    ### TESTE DE OPÇÕES
    ### SOMA   

    if controle == 1:
        num01 = float(input('Digite o primeiro número: '))
        num02 = float(input('Digite o segundo número: '))
        print('\nA soma entre os números é: ', num01+num02)
        print('-------------------------------------------------', end='\n')
        
    ### SUBTRAÇÃO
    elif controle == 2:
        num01 = float(input('Digite o primeiro número: '))
        num02 = float(input('Digite o segundo número: '))
        print('\nA subtração entre os números é: ', num01-num02 )
        print('-------------------------------------------------', end='\n')

    ###MULTIPLICAÇÃO
    elif controle == 3:
        num01 = float(input('Digite o primeiro número: '))
        num02 = float(input('Digite o segundo número: '))
        print('\nA multriplicação entre os números é: ', num01*num02)
        print('-------------------------------------------------', end='\n')

    ### DIVISÃO
    elif controle == 4:
        num01 = float(input('Digite o primeiro número: '))
        num02 = float(input('Digite o segundo número: '))
        if num02==0:
            print('\nNÃO É POSSIVEL FAZER DIVISÃO POR ZERO')
            print('-------------------------------------------------', end='\n')
        else:
            print('\nA divisão entre os números é: ', num01/num02)
            print('-------------------------------------------------', end='\n')

    ### FATORIAL
    elif controle == 5:
        num01 = int(input('Digite o número: '))
        factorial=1
        for value in range(1, num01 + 1):
            factorial*=value
        print(f'\nO fatorial de {num01} é: {factorial}')
        print('-------------------------------------------------', end='\n')

    ### EXPONENCIAL
    elif controle == 6:
        num01 = float(input('Digite o primeiro número: '))
        num02 = float(input('Digite o segundo número: '))
        print(f'{num01} elevado à {num02} é igual a: ', num01**num02)
        print('-------------------------------------------------', end='\n')

    else:
        print('\nCOMANDO NÃO É VÁLIDO')
        print('')
        print('-------------------------------------------------')
=======
##### MINI CALCULADORA ############

controle = 1
while True:
    print('\nMini calculadora')
    print()
    print('1 - Somar dois números')
    print('2 - Subtrair dois números')
    print('3 - Multiplicar dois números')
    print('4 - Dividir dois números')
    print('5 - Fatorial de um número')
    print('6 - Potência entre dois números')
    print('7 - SAIR')
    print()
    #### SAIR
    controle = int(input('Escolha uma opção: '))
    if controle==7:
        print('\n-------------------------------------------------', end='\n')
        print("\nFIM DA CALCULADORA")
        print('\n-------------------------------------------------', end='\n')
        break
    print('-------------------------------------------------', end='\n')
    
    
    ### TESTE DE OPÇÕES
    ### SOMA   

    if controle == 1:
        num01 = float(input('Digite o primeiro número: '))
        num02 = float(input('Digite o segundo número: '))
        print('\nA soma entre os números é: ', num01+num02)
        print('-------------------------------------------------', end='\n')
        
    ### SUBTRAÇÃO
    elif controle == 2:
        num01 = float(input('Digite o primeiro número: '))
        num02 = float(input('Digite o segundo número: '))
        print('\nA subtração entre os números é: ', num01-num02 )
        print('-------------------------------------------------', end='\n')

    ###MULTIPLICAÇÃO
    elif controle == 3:
        num01 = float(input('Digite o primeiro número: '))
        num02 = float(input('Digite o segundo número: '))
        print('\nA multriplicação entre os números é: ', num01*num02)
        print('-------------------------------------------------', end='\n')

    ### DIVISÃO
    elif controle == 4:
        num01 = float(input('Digite o primeiro número: '))
        num02 = float(input('Digite o segundo número: '))
        if num02==0:
            print('\nNÃO É POSSIVEL FAZER DIVISÃO POR ZERO')
            print('-------------------------------------------------', end='\n')
        else:
            print('\nA divisão entre os números é: ', num01/num02)
            print('-------------------------------------------------', end='\n')

    ### FATORIAL
    elif controle == 5:
        num01 = int(input('Digite o número: '))
        factorial=1
        for value in range(1, num01 + 1):
            factorial*=value
        print(f'\nO fatorial de {num01} é: {factorial}')
        print('-------------------------------------------------', end='\n')

    ### EXPONENCIAL
    elif controle == 6:
        num01 = float(input('Digite o primeiro número: '))
        num02 = float(input('Digite o segundo número: '))
        print(f'{num01} elevado à {num02} é igual a: ', num01**num02)
        print('-------------------------------------------------', end='\n')

    else:
        print('\nCOMANDO NÃO É VÁLIDO')
        print('')
        print('-------------------------------------------------')
>>>>>>> 8f69615397bbb9a044236392521906546b2babae
        