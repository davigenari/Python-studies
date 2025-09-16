'''Conta de luz
Peça a quantidade de kWh consumidos e o valor por kWh, depois calcule o valor da conta de energia.'''

quantidade = float(input("Digite a quantidade de kWh consumidos: "))
valor = float(input("Digite o valor por kWh: "))
conta = quantidade * valor

print(f"O valor da sua conta de energia este mês é: {conta:.2f}")