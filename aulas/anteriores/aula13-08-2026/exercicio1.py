from dadosEx1_2_3 import produtos


"""
Ex 01: Leitura e Busca
Dada uma Lista de Dicionários de produtos [{"nome": "A", "preco": 10}, ...], 
escreva uma função que receba a lista e retorne o nome do produto mais caro.

Objetivo: Praticar iteração sobre registros e comparação de atributos.

"""

def buscaMaisCaro (produtos:list) -> str:
  '''Função que busca o mais caro'''
  nome = ""
  maisCaro = 0.0
  for produto in produtos:
    if produto["preco"] >= maisCaro:
      maisCaro = produto["preco"]
      nome = produto["nome"]
  return nome

def buscaMaisCaroLamda(produtos:list) -> str:
  dicioMaisCaro = max(produtos, key=lambda produto: produto["preco"])
  return (dicioMaisCaro["nome"], dicioMaisCaro["preco"])


if __name__ == '__main__':

    print("\nExecutando a busca pelo produto mais caro: \n")
    maisCaroVarNome = buscaMaisCaro(produtos)

    print(f'O produto mais caro da lista é o: {maisCaroVarNome} \n')

    print("\nExecutando a busca pelo produto mais caro usando a função max do Python: \n")
    maisCaroVarNomeLambda = buscaMaisCaroLamda(produtos)
  
    print(f'O produto mais caro da lista é o: {maisCaroVarNomeLambda[0]} \n')