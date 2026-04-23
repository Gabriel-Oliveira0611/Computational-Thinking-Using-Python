#SEQUENCIA
#HOMOGENEA /

inicio = int (input('inicio'))
fim = int(input('fim'))

pares = 0

for n in range(inicio,fim):
    if n%2 ==0:
     print(f'{n}')

print(f" nesse range tem{pares}tem numero pares ")


