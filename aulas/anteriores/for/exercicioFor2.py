palavra = input("Insira aqui a palavra: ")
quantidadeVogais = 0

for l in palavra:
    if l == "a" or l == "e" or l == "i" or l == "o" or l == "u":
        quantidadeVogais += 1
    else:
        continue

print(quantidadeVogais)