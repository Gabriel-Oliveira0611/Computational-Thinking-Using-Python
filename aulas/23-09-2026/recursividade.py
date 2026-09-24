vetor = [1,2,3,4,5]

def fat(vetor: list) -> int:
    if len(vetor) == 0 or len(vetor) == 1:
        return vetor[0]
    else:
        return vetor[0] * fat(vetor[1:])

print(fat(vetor))