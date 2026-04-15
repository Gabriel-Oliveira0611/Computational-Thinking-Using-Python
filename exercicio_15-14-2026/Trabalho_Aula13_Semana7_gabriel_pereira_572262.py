#NOME: GABRIEL PEREIRA DE OLIVEIRA

#RM: 572262


# Exercício 1:
'''
Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado. 
Ele registrou a quantidade vendida de dois produtos: maçãs e bananas. Agora, ele precisa escrever um programa 
que identifique e exiba qual deles teve maior venda.

Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando 
qual deles vendeu mais. Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.

Exemplo de Entrada e Saída esperados:
    Digite a quantidade de maçãs vendidas: 15
    Digite a quantidade de bananas vendidas: 3

    As maçãs tiveram mais vendas.

'''

maca = int(input("Insira quantas maças foram vendidas: "))
bananas = int(input("Insira quantas bananas foram vendidas: "))

if maca > bananas: {

print(f"""
-> O número de maçãs vendidas foi de: {maca}.
-> O número de bananas vendidas foi de: {bananas}.
--> Logo, foram vendidas mais maças do que bananas.
      """)
}
elif maca < bananas: {

    print(f"""
-> O número de maçãs vendidas foi de: {maca}.
-> O número de bananas vendidas foi de: {bananas}.
--> Logo, foram vendidas mais bananas do que maçãs.
      """)
}
else :{
    
    print("Houve um empate.")
}


# Exercício 2:
'''Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C. 
No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos 
e não calcular o total.

Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. Se algum valor for 
negativo, mostre uma mensagem informando o erro.

Exemplo de Entrada e Saída esperados:
    Informe os dias para a atividade A: 5
    Informe os dias para a atividade B: -8
    Informe os dias para a atividade A: 10

    Erro: Os dias não podem ser negativos!


'''

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



# Exercício 3:
'''
Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C. 
Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.

Exemplo de Entrada e Saída esperados:
    Digite a temperatura atual da sala de servidores: 30
    
    Alerta!!! Temperatura acima do limite permitido (25ºC)

'''

temperatura = int(input("Insira auqi a temperatura: "))
limite = int(25)

if temperatura > limite: {
    print(f"""
Temperatura atual: {temperatura}°C
É necessário abaixar a temperatura!
""")
}
else: {
    print(f"""Temperatura atual: {temperatura}°C.
A temperatura está dentro do limite.
    """ )
}


# Exercício 4:
'''
Anna Júlia está criando um sistema para calcular o Índice de Massa Corporal (IMC) e fornecer recomendações básicas. 
O programa deve receber o peso e a altura de uma pessoa e exibir o valor do IMC, além de indicar se está abaixo do 
peso, com peso normal ou acima do peso. Crie um programa que receba o peso (em kg com precisão de .1f) e a altura 
(em metros com precisão de .2f) e calcule o IMC usando a fórmula: 

    IMC = peso / (altura ** 2) 

Depois, exiba o valor do IMC (com precisão de .2f) e uma mensagem indicando se está:
    abaixo do peso (IMC < 18.5), 
    peso normal (18.5 <= IMC < 25),
    ou acima do peso (IMC >= 25).

Exemplo de Entrada e Saída esperados:
    Digite seu peso em quilogramas (kg) com precisão de 1 casa depois da vírgula: 75.0
    Digite sua altura em metros (m) com precisão de 2 casa depois da vírgula: 1.68

    Seu IMC é de : 26.57
    Você pode estar acima do peso com base no IMC.

'''

peso = float(input("Insira aqui o peso: "))
altura = float(input("Insira aqui a altura: "))
imc = peso / (altura ** 2)

if imc < 18.5: {
    print(f"""
-> Seu peso atual: {peso}
-> Sua altura: {altura}
-> Seu IMC: {imc}

-> Você está abaixo do peso!
""")
}
elif imc <= 25: {
    print(f"""
-> Seu peso atual: {peso}
-> Sua altura: {altura}
-> Seu IMC: {imc}

-> Você está no peso normal.
""")
}
else :
    print(f"""
-> Seu peso atual: {peso}
-> Sua altura: {altura}
-> Seu IMC: {imc}

-> Você está acima do peso.
""")


# Exercício 5:
'''
Carlos quer monitorar seu orçamento semanal para evitar gastos excessivos. Ele estabeleceu um limite de R$ 1.000,00 
para seus gastos e precisa de um programa que ajude a controlar suas despesas. O programa deve receber o total de 
despesas realizadas da seguinte forma: 
    5 entradas (com precisão de .2f) 
    e assim somar e informar o total
    e também informar se ele ultrapassou o limite ou ainda está dentro do orçamento.

Exemplo de Entrada e Saída esperados:
    Digite o valor da despesa semanal 1 : 500.25
    Digite o valor da despesa semanal 1 : 256.62
    Digite o valor da despesa semanal 1 : 375.00

    Atenção o total foi de R$ 1131.87, e ultrapassou o limite de R 1000.00 semanais estipulado!


'''

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