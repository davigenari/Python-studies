"""Solicite a idade do usuário e informe se ele é menor de idade,
maior de idade ou idoso (considerando 18 e 65 anos como limites)."""

idade = int(input("Digite a sua idade"))

if idade >= 65:
    print("Você é idoso.")
elif idade >= 18:
    print("Você é maior de idade. ")
else:
    print("Você é menor de idade. ")