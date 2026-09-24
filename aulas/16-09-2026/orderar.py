vetor = [55, 8, 17]

def ordena3(vetor:list) -> list:

    auxiliar = 0

    for i in range(0, 3-1):
        for j in range(i+1, 3):
            print(f'Elemento índice i({i}) é: {vetor[i]}')
            print(f'Elemento índice i+j({j}) é: {vetor[j]}')
            if vetor[i] > vetor[j]:
                print(f'Elementos i e i+j foram trocados!')
                auxiliar = vetor[i]
                vetor[i] = vetor[j]
                vetor[j] = auxiliar
                print(vetor)
            else:
                print(f'Elementos i e i+j não foram trocados.')
                print(vetor)
        return vetor

ordena3(vetor)