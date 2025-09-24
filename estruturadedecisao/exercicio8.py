"""Peça ao usuário seu peso e altura, calcule o Índice de Massa Corporal (IMC) e classifique-o
como "Abaixo do peso",  "Peso normal", "Sobrepeso" ou "Obesidade"."""

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso / (altura * altura)

if imc < 18.5:
    print(f"Você está abaixo do peso.")
elif imc >= 18.5 and imc <= 24.9:
    print(f"Seu peso está normal.")
elif imc >= 25 and imc <= 29.9:
    print(f"Você está com sobrepeso.")
else:
    print(f"Você está com obesidade.")