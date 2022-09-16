## CONTAGEM DE ALGORÍTIMOS EM UMA LISTA

# lista = [1,4,5,6,2,2,4,5,5,5,1,6,7,5]
# number = int(input("Digite o número que quer contar da lista: "))
# count = lista.count(number) 

# print(count)

## LIST COMPREHENSION

notas = [0,0,9.0,10,7.5,8,8,10,5,6,10,4,6,5,6.6,2.5,5.6]

notasValidas = [nota for nota in notas if nota > 0]

notasValidas.sort()

# OU PODE USAR TAMBEM {{{notasSorted = sorted(notasValidas)}}}

print(notasValidas)
