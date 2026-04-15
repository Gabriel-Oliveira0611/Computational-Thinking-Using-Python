a = int(input("Insira aqui o tempo da atividade A: "))
b = int(input("Insira aqui o tempo da atividade B: "))
c = int(input("Insira aqui o tempo da atividade C: "))
total = 0

if (a < 0) or (b < 0) or (c < 0): {
    print(f"""
          -> O tempo da atividade A foi de: {a}
          -> O tempo da atividade B foi de: {b}
          -> O tempo da atividade C foi de: {c}

          Nenhum dos valores deve ser negativo!""")
}
else :
    total = a + b + c
    print(f"""
          -> O tempo da atividade A foi de: {a}
          -> O tempo da atividade B foi de: {b}
          -> O tempo da atividade C foi de: {c}

          O tempo total de dias para as atividades é de: {total}
          """)
