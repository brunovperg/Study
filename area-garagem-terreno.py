#################### AREA DO TERRENO COM ZONA DE LOCALIZAÇÃO ############################

#### calcular porcentagem da area de garagem dentro de area de terreno #############
def areaUrbana():
    lGaragem = float(input("Largura da garagem em metros: "))
    cGaragem = float(input("Comprimento da garagem em metros: "))
    lTerreno = float(input("Largura do terreno em metros: "))
    cTerreno = float(input("Comprimento do terreno em metros: "))  
    
    # Áreas
    areaGaragem = lGaragem*cGaragem
    areaTerreno = lTerreno*cTerreno
    porcentTotal = ((areaGaragem/areaTerreno)*100)

    print("Porcentagem de garagem no terreno =", round(porcentTotal),"%")
    zona = input("Defina a zona da cidade do terreno (NORTE=N ; SUL=S ; LESTE=L ; OESTE=O): ")

    if(zona == "N" and porcentTotal <= 25):
        print("Projeto atende a norma")
    elif(zona=="S" and porcentTotal <=40):
        print("Projeto atende a norma")
    elif(zona=="L" or zona=="O" and porcentTotal <=30):
        print("Projeto atende a norma")
    else:
        print("Projeto não atende a norma, favor revisar")

areaUrbana()