"""Solicite o preço de um produto e aplique um desconto de 10% se o preço for maior que R$ 100.
Exiba o valor final."""

produto = float(input("Digite o preço do produto: "))
desconto = produto * 0.10

if produto > 100:
    print(f"O valor de desconto é {desconto:.2f}. O valor final do produto é de R$ {produto - desconto}")
else:
    print("O produto não tem desconto.")