############################# CALCULADORA IDADE GESTACIONAL #########################
from datetime import date, datetime
controle = 1
while True:
    print('\n-------------------------------------------')
    print('\n ######## CALCULADORA IDADE GESTACIONAL #####')
    print('\n1 - Fazer cálculo pela última menstruação')
    print('\n2 - Fazer cálculo pelo último ultrasom')
    controle = int(input('\nDigite um valor: '))
    ####### CÁLCULO PELA ULTIMA MENSTRUAÇÃO ######
    if controle == 1:
        print('\n-------------------------------------------')
        print('\nCÁLCULO PELA ULTIMA MENSTRUAÇÃO')
        lastPeriodYear = int(input("\nAno da ultima menstruação (AAAA): "))
        lastPeriodMonth = int(input("\nMês da ultima menstruação (MM): "))
        lastPeriodDay = int(input("\nDia da ultima menstruação: (DD): "))

        LastPeriod = datetime.strptime(f'{lastPeriodYear}{lastPeriodMonth}{lastPeriodDay}', "%Y%m%d")
        today = date.today()

        LastPeriodOrdinal = LastPeriod.toordinal()
        todayOrdinal = today.toordinal()

        weeksOrdinal = todayOrdinal - LastPeriodOrdinal
        daysTotal = (weeksOrdinal%7)
        weekTotal = (int(weeksOrdinal/7))
        print('\n-------------------------------------------')
        print(f"\nA idade gestacional é de {weekTotal} semanas e {daysTotal} dias.")
        print('\n-------------------------------------------')
        
        print('\n1 - Repetir cálculo pela última menstruação')
        print('\n2 - Fazer cálculo pelo último ultrasom')
        controle = int(input('\nDigite um valor: '))
        
        
     #  ####### CÁLCULO PELO ULTIMO ULTRASOM ######
    elif controle == 2:
        print('\n-------------------------------------------')
        print('\nCÁLCULO PELO ULTIMO ULTRASOM')
        ultraYear = int(input("\nAno do ultimo ultrasom (AAAA): "))
        ultraMonth = int(input("\nMês do ultimo ultrasom (MM): "))
        ultraDay = int(input("\nDia do ultimo ultrasom (DD): "))
        
        weeksAdd = int(input('\nQuantas semanas tinham no ultrasom: '))*7
        dayAdd = int(input('\nQuantos dias tinham no ultrasom: '))

        
        today = date.today()
        lastUltra = datetime.strptime(f'{ultraYear}{ultraMonth}{ultraDay}', "%Y%m%d")
        
        lastUltraOrdinal = lastUltra.toordinal()
        todayOrdinal = today.toordinal()
        
        dateTotal = (todayOrdinal - lastUltraOrdinal)+(weeksAdd+dayAdd)
        dateWeek = int(dateTotal/7)
        dateDay = (dateTotal%7)
        
        print('\n-------------------------------------------')
        print(f"\nA idade gestacional é de {dateWeek} semanas e {dateDay} dias.")
        print('\n-------------------------------------------')
        
        print('\n1 - Fazer cálculo pela última menstruação')
        print('\n2 - Repetir cálculo pelo último ultrasom')
        controle = int(input('\nDigite um valor: '))
        
    else:
        print('-------------------------------------------------')
        print('\nCOMANDO NÃO É VÁLIDO')
    