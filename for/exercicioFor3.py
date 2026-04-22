numero = int(input("Insira aqui o número que deseja ver a tabuada: "))
multiplicacao = 0

for n in range (1, 101):
    multiplicacao = n * numero
    print(f"{numero} x {n} = {multiplicacao}")