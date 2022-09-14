######## GRÁFICOS USANDO MATPLOTLIST ###########
import matplotlib.pyplot as plt
from cgi import print_environ


listaEixoX = [8,10,12,14,16]
listaEixoY = [1,9,4,15,12]

plt.plot(listaEixoX, listaEixoY)

plt.title("Vendas no dia DD/MM/AA")
plt.ylabel("Lista de vendas")
plt.xlabel("Horas do dia")

plt.grid(True)

plt.show()
