vetor1 = [1, 0, 5, -2, -5, 7]
soma = sum([vetor1[0], vetor1[1], vetor1[5]]) #soma dos vetores - 1
print(f"a soma dos indices 0, 1 e 5 eh: {soma}")
vetor1[4] = 100 #mudando o valor do indice 4 para 100
for numero in vetor1: #mostrando o valor, um em cada linha
    print(numero)