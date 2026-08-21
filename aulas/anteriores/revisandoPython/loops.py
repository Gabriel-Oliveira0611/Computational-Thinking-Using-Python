# numero = 10
# while numero >= 1:
#     print(f"Número atual: {numero}")
#     numero -= 1

senha = "senhaCorreta"
tentativaSenha = ""
while senha != tentativaSenha:
    tentativaSenha = input("Digite sua senha: ")
    if tentativaSenha != senha:
        print("Senha incorreta! Tente novamente.")