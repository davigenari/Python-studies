''' Conversão de dinheiro

Peça um valor em reais e converta para dólares. (Considere o valor do dólar como R$ 5,00)'''

reais = float(input("Digite o valor em reais: "))
dolar = reais * 5.00

print(f"O valor informado é R$ {reais}. Convertendo em dolar, ficam $ {dolar:.2f} dolares.")