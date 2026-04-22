# Primeiro exemplo

# contador = 0

# #-------------------Caixa while------------------------------------------
# while contador <= 8:
#     print(f"O contador está no valor {contador}")
#     contador += 1

# #--------------------Caixa while-----------------------------------------

# Segundo exemplo

# while True:
#     numero = int(input("Insir um númeor par: "))
#     if numero % 2 == 0:
#         print("Você digitou um número par! Obrigado")
#         break
#     else:
#         print("Você não digitou um número par!")

# print("Fim do programa.")

# Terceiro exemplo

# numeros = [5, 8, 2, 9, 0, 1, 3, 4]
# for n in numeros:
#     if n % 2 != 0:
#         continue
#     print(f"O npumero {n} é par")

# Quarto exemplo
dados = {"nome":"Gabriel Pereira", "Idade": 24, "área de estudo":"Análise e Desenvolvimento de Sistemas"}

for c, v in dados.items():
    print(f"{c}: {v}")