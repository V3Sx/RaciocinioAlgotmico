vetor3 = []
quadrado = []
count = 0
for i in range (10):
    reais = float(input("Insira um numero: "))
    vetor3.append(reais)
while count < 10:
    operacao = (vetor3[count] * vetor3[count])
    quadrado.append(operacao)
    count += 1
print(vetor3)
print(quadrado)