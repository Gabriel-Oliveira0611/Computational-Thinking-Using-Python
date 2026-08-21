V = [1,2,3,4,5]

V.append(6) # Adiciona elemento ao final da lista, restrito a apenas um elemento por vez.
# vetorTeste = V.copy()

# print(f"Vetor teste: {vetorTeste}")

# V[4] = 'substituído'

# print(f"Vetor original após a substituição: {V}")

vetorTeste = V

print(f"Vetor teste antes da alteração: {vetorTeste}")

V.append(7)

print(f"Vetor teste após a alteração: {vetorTeste}")

elementoExtraido = V.pop()
print(f"Elemento extraído: {elementoExtraido}")