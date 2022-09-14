<<<<<<< HEAD
########### CONVERSOR HEXADECIMAL ###############
from re import X

while True:
    mensagem = "\nValor decimal: {0}\n\nValor hexadecimal: {1}"

    num_dec = int(input("\nDigite um número: "))

    num_hex = format(num_dec, 'X')

=======
########### CONVERSOR HEXADECIMAL ###############
from re import X

while True:
    mensagem = "\nValor decimal: {0}\n\nValor hexadecimal: {1}"

    num_dec = int(input("\nDigite um número: "))

    num_hex = format(num_dec, 'X')

>>>>>>> 8f69615397bbb9a044236392521906546b2babae
    print(mensagem.format(num_dec, num_hex))