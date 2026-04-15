peso = float(input("Insira aqui o peso: "))
altura = float(input("Insira aqui a altura: "))
imc = peso / (altura ** 2)

if imc < 18.5: {
    print(f"""
-> Seu peso atual: {peso}
-> Sua altura: {altura}
-> Seu IMC: {imc}

-> Você está abaixo do peso!
""")
}
elif imc <= 25: {
    print(f"""
-> Seu peso atual: {peso}
-> Sua altura: {altura}
-> Seu IMC: {imc}

-> Você está no peso normal.
""")
}
else :
    print(f"""
-> Seu peso atual: {peso}
-> Sua altura: {altura}
-> Seu IMC: {imc}

-> Você está acima do peso.
""")