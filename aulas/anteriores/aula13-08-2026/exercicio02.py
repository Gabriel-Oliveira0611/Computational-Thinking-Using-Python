from dadosEx1_2_3 import produtos

"""
Ex 02: Update
Dada uma Lista de Dicionários de produtos [{"nome": "A", "preco": 10}, ...], 
escreva uma função faça o “update” do “preço” do registro, e aplique para o 
"Headset Wireless".

Objetivo: Praticar a correção na estrutura.

"""

nomeProduto = input("Insira o nome do produto:")
precoNovo = float(input("Insirsa o novo valor:"))

def updatePrecoProdutos(produtos:list, nomeProduto:str, precoNovo:float):
    for produto in produtos:
        if produto["nome"] == nomeProduto:

            print(f"Produto encontrado. O {nomeProduto} antes custava R${produto["preco"]}. Agora, custa R${precoNovo}")

            produto["preco"] = precoNovo
        else:
            print("Produto não encontrado.")
        break

updatePrecoProdutos(produtos, nomeProduto, precoNovo)

