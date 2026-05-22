vetor4 = []
for i in range (8):
    valores = int(input("Insira um numero: "))
    vetor4.append(valores)
x = int(input("Insira o primeiro indice: "))
y = int(input("Insira o segundo indice: "))
soma = vetor4[x] + vetor4[y]
print(f"A soma dos valores dos indices eh: {soma}")