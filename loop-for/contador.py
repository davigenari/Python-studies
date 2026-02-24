### Crie um contador que peça ao usuário um número inicial, um número final e um incremento e exiba os valores gerados.

inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))
passo = int(input("Digite o incremento: "))

for numero in range(inicio, fim + 1, passo):
    print(numero)