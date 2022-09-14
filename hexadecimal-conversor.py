
########### CONVERSOR HEXADECIMAL ###############
from re import X

while True:
    mensagem = "\nValor decimal: {0}\n\nValor hexadecimal: {1}"

    num_dec = int(input("\nDigite um número: "))

    num_hex = format(num_dec, 'X')

