"""Votação: idade ≥16 e título válido."""

idade = int(input("informe a sua idade: "))
if idade >= 16:
    print("O seu título de eleitor está válido? ")
    titulo = input("")
    if titulo.upper() == "SIM":
        print("Você pode votar.")
    else:
        print("Você não pode votar.")
else:
    print("Você não pode votar.")