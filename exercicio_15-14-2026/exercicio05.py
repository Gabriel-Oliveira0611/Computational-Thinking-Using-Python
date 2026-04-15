limite = float(3000)
despesas = float(input("Insira aqui o valor das suas despesas no mês: "))

if despesas < limite: {
    print(f"""
-> Despesas atuais: R${despesas:.2f}
-> Limite: R${limite:.2f}

-> Você ainda está dentro do limite.
""")
}
else :
    print(f"""
-> Despesas atuais: R${despesas:.2f}
-> Limite: R${limite:.2f}

-> Você ultrapassou o limite.
""")