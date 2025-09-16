'''Crie um programa que leia o número de dias trabalhados em um mês e mostre o salário de um funcionário, sabendo que
ele trabalha 8 horas por dia e ganha R$25,00 por hora trabalhada.'''

dias = int(input("Informe quantos dias você trabalhou este mês: "))
valor = 25 * 8
salario = valor * dias

print(f"Seu salário este mês será R$ {salario}.")