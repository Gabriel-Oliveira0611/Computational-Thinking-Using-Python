passouTeste1 = input("Você passou no teste 01?")
passouTeste2 = input("Você passou no teste 02?")

passouTeste1 = passouTeste1.lower()
passouTeste2 = passouTeste2.lower()

if passouTeste1 == "sim":
    print("Passou no teste 01")
    if passouTeste2 == "sim":
        print("Passou no teste 02")
        print("Você passou nos dois testes.")
    else:
        print("Você passou no teste 01, mas não passsou no teste 02.")
else:
    print("Você não passou.")