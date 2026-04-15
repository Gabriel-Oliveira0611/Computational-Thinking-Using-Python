temperatura = int(input("Insira auqi a temperatura: "))
limite = int(25)

if temperatura > limite: {
    print(f"""
Temperatura atual: {temperatura}°C
É necessário abaixar a temperatura!
""")
}
else: {
    print(f"""Temperatura atual: {temperatura}°C.
A temperatura está dentro do limite.
    """ )
}