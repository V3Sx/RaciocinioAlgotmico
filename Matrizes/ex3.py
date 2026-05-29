matriz3 = []

maior_nota = 0
maior_matricula = 0

for i in range(5):
    linha = []

    matricula = int(input("Digite a matricula do aluno: "))
    media_provas = int(input("Digite a media das provas: "))
    media_trabalhos = int(input("Digite a media dos trabalhos: "))

    nota_final = media_provas + media_trabalhos #segunda parte

    linha.append(matricula)
    linha.append(media_provas)
    linha.append(media_trabalhos)
    linha.append(nota_final)

    matriz3.append(linha)

    if nota_final > maior_nota:
        maior_nota = nota_final
        maior_matricula = matricula

print("Matriz dos Alunos:")

for linha in matriz3:
    print(linha)

print(f"A matricula do aluno com a maior nota final: {maior_matricula}")