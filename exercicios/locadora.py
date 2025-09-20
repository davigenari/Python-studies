"""A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva um programa que pergunte a quantidade de
 Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar,
 sabendo que o carro custa R$ 90,00 por dia e R$ 0,20 por Km rodado."""

dias = int(input("Informe quantos dias o carro foi alugado? "))
km = float(input("Informe quantos km foram percorridos: "))

preco = (dias * 90) + (km * 0.20)

print(f"O preço a pagar é de R$ {preco:.2f}")