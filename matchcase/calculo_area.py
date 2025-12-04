"""Desenvolva um programa que permita ao usuário escolher entre calcular a área de um quadrado, retângulo ou triângulo e
insira os valores necessários para o cálculo."""

opcao = int(input("Escolha uma opção para calcular a área: \n1. Quadrado\n2. Retângulo \n3. Triângulo\n"))

match opcao:
    case 1:
        quadrado = int(input("Insira a medida de um lado do quadrado: "))
        print(f"A área do quadrado é: {quadrado * 2}")
    case 2:
        baseretangulo = int(input("Insira a base do retângulo: "))
        alturaretangulo = int(input("Insira a altura do retângulo: "))
        print(f"A área do retângulo é: {baseretangulo * alturaretangulo}")
    case 3:
        triangulo = int(input("Insira a medida de um lado do quadrado: "))
        basetriangulo = int(input("Insira a base do triângulo: "))
        alturatriangulo = int(input("Insira a altura do triângulo: "))
        print(f"A área do triângulo é: {(basetriangulo * alturatriangulo) /2}")
    case _:
        print("Opção inválida, tente novamente.")