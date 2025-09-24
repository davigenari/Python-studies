"""Crie uma calculadora simples que permita ao usuário escolher uma operação
(adição, subtração, multiplicação ou divisão) e dois números, e então exiba o resultado."""

operacao = input("Escolha uma operação entre adição, subtração, multiplicação ou divisão: ")
num1 = float(input("Digite um número: "))
num2 = float(input("Digite mais um número: "))
adicao = (num1 + num2)
subtracao = (num1 - num2)
multiplicacao = (num1 * num2)
divisao = (num1 / num2)

if operacao == "adicao":
    print(f"{num1 + num2:.2f}")
elif operacao == "subtracao":
    print(f"{num1 - num2:.2f}")
elif operacao == "multiplicacao":
    print(f"{num1 * num2:.2f}")
elif operacao == "divisao":
    print(f"{num1 / num2:.2f}")
else:
    print("Operação inválida")