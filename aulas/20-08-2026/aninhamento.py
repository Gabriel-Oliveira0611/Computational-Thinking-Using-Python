try:
    inputi = int(input("Digite um valor entre 0 e 10: "))
except Exception as e:
    print("Valor inválido.")
else:
    if inputi > 0: #Essa linha sempre executa
        if inputi < 10:
            print("Valor válido.")
        else:
            print("Valor inválido! Número maior que 10")
    else:
        print("Valor inválido! Número menor que 0")



