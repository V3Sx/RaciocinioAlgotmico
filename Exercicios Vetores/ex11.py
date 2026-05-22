vetor11 = []
count = 0
for i in range(5):
    numeros = int(input(f"{count}/5 - digite um numero: "))
    vetor11.append(numeros)
    count += 1
maior = max(vetor11)
menor = min(vetor11)

posicao1 = vetor11.index(maior)
posicao2 = vetor11.index(menor)
print(f"O maior numero se localiza no index: {posicao1} e o menor no index: {posicao2}.")