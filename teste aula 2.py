nota_aluno = float(input("Informe a nota do aluno:"))
media = 7
if nota_aluno >= media:
  print("Aprovado")
elif nota_aluno >= 5:
  print("Recuperação")
else:
  print("Reprovado")