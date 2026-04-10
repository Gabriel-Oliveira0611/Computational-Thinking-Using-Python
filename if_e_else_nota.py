print("Digite 1 para atendimento" \
"Digite 2 para cadastro" \
"Digite 3 para relatórios")

menuInput = int(input("Deseje a opção desejada: "))

match menuInput:
    case 1:
        print("Você selecionou a opção atendimento")
    
    case 2:
        print("Você seelcionou a opção cadastro")

    case 3:
        print("Você selecionou a opção relatórios")
    
    case _:
        print("Opção inválida.")