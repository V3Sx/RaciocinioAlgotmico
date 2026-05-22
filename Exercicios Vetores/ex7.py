vetor7 = []
for i in range (10):
    ask_numeros = int(input("Digite um numero para amazenarmos no vetor: "))
    vetor7.append(ask_numeros)
maior = max(vetor7)
posicao = vetor7.index(maior)
print(f"O maior numero eh {maior} e o index dele eh {posicao}.")