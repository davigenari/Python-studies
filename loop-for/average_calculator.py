quantidade = int(input("Quantos números você quer inserir? "))

soma = 0  # Variável para armazenar a soma dos números
for i in range(quantidade):
    numero = float(input(f"Digite o {i+1}º número: "))
    soma += numero  # Acumula a soma dos números

media = soma / quantidade  # Calcula a média
print(f"A média dos números digitados é {media:.2f}")