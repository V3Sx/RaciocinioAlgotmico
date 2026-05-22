vetor8 = []
count = 0
for i in range (15):
    notas = float(input(f"{count}/15 - Insira a nota do aluno: "))
    count += 1
    vetor8.append(notas)
media = sum(vetor8) / 15
print(f"A media da turma foi: {media}")