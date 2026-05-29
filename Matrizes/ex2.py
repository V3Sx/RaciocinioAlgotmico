matriz = []
maior = None
linha_maior = 0
coluna_maior = 0

for i in range(4):
    linha = []

    for j in range(4):
        numero = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(numero)

        if maior is None or numero > maior:
            maior = numero 
            linha_maior = i
            coluna_maior = j

    matriz.append(linha)

print("\nMatriz:")

for linha in matriz:
    print(linha)

print(f"Maior valor: {maior}")
print(f"Localizacao: linha {linha_maior}, coluna {coluna_maior}")