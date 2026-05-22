vetor9 = []
count = 0
for i in range(10):
    preenche = int(input(f"Fale o numero para a posicao {count}: "))
    vetor9.append(preenche)
    count += 1
    
negativos = [x for x in vetor9 if x < 0]

def somar_positivos(vetor9):
    soma = 0
    for numero in vetor9:
        if numero > 0:
            soma += numero
    return soma

print(f"os numeros negativos sao: {negativos},\n e a soma dos postivos: {somar_positivos(vetor9)}")


