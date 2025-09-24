"""Peça um número ao usuário e informe se ele é par ou ímpar."""

num = int(input("Digite um número: "))

if num % 2 == 0:
    print(f"O número é par.")
else: print("O número é ímpar.")