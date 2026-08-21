from dadosEx1_2_3 import produtos

nomeProduto = input("Insira o nome do produto a ser excluído:") 

def deleteProduto(produtos:list, nomeProduto:str):
    localizado = False

    for produto in produtos:
        if produto["nome"] == nomeProduto:
            localizado = True

            produtos.remove(produto)
            print(produtos)
        else:
            print("Produto não encontrado")
        break

deleteProduto(produtos, nomeProduto)