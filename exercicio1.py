"""Receba dois números do usuário e mostre qual deles é o maior."""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O número {num1} é maior que o número {num2}.")
else:
    print(f"O número {num2} é maior que o número {num1}.")