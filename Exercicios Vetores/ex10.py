vetor10 = []
count = 0
for i in range(5):
    numeros = int(input(f"{count}/5 - Digite um valor: "))
    vetor10.append(numeros)
    count += 1

maior = max(vetor10)
menor = min(vetor10)
media = sum(vetor10) / 5
print(vetor10)
print(f"maior: {maior}")
print(f"menor: {menor}")
print(f"media: {media}")