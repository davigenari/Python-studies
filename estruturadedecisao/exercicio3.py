"""Peça ao usuário para inserir a idade de uma pessoa e classifique-a como "Criança" (0-12 anos),
"Adolescente" (13-17 anos), "Adulto" (18-64 anos) ou "Idoso" (65+ anos)."""

idade = int(input("Insira a idade de uma pessoa: "))

if idade >= 0 and idade <= 12:
    print("Criança. ")
elif idade >= 13 and idade <= 17:
    print("Adolescente")
elif idade >= 18 and idade <= 64:
    print("Adulto")
else:
    print("Idoso")