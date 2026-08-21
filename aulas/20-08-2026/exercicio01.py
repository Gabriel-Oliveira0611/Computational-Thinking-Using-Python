"""
Ex 05: Conversor Seguro (ValueError)
Crie uma função converter_para_inteiro(texto) que receba uma string do usuário e retorne o valor inteiro. Caso o texto não seja um número válido, capture ValueError e retorne None exibindo uma mensagem personalizada.
"""

def converterParaInteiro(texto:str) -> int:
    try:
        output = int(texto)
        return output

    except ValueError as e:
        print(f"{e} - Digite um número inteiro!")
        return None

converterParaInteiro(20)