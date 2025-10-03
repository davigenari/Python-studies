"""Faça um programa que leia a idade e a categoria de um jogador de futebol (juvenil, adulto, veterano) e calcule a sua
classificação no time."""

idade = int(input("Digite sua idade: "))

if idade >=0 and idade <= 17:
    print("Você está na categoria Juvenil.")
elif idade >=18 and idade <= 21:
    print("Você está na categoria Adulto")
elif idade >= 22 and idade <= 40:
    print("Você está na categoria Veterano")
else:
    print("Inválido")