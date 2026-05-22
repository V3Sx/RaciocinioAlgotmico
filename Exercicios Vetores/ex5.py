vetor5 = []
count = 0
for i in range (10):
    valores = int(input("Insira um numero: "))
    vetor5.append(valores)
for i in (vetor5):
    if i % 2 == 0:
        count += 1
        print(i)
print(f"A quantidade de pares eh {count}")