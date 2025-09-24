"""Receba a nota de um aluno e classifique-a como A (90-100), B (80-89),
C (70-79), D (60-69), ou F (menos de 60)."""

nota = int(input("Digite a nota do aluno: "))

if nota >= 90 and nota <= 100:
    print("Você tirou nota A.")
elif nota >= 80 and nota <= 89:
    print("Você tirou nota B.")
elif nota >= 70 and nota <= 79:
    print("Você tirou nota C.")
elif nota >= 60 and nota <= 69:
    print("Você tirou nota D.")
else:
    print("Você tirou nota F.")