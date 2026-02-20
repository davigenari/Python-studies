###Peça um número ao usuário e exiba os múltiplos desse número de 1 a 10.###

numero = int(input("Digite um número para ver a tabuada: "))

for i in range(1, 11):  # De 1 a 10
    print(f"{numero} x {i} = {numero * i}")