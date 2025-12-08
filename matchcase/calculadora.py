"""O usuário escolhe uma operação matemática (+, -, *, /) e insere dois números. O programa exibe o resultado."""

operacao = int(input("Escolha a operação matemática que você quer realizar: \n1. Soma\n2. Subtração \n3. Multiplicação\n4. Divisão\n"))

match operacao:
    case 1:
        soma1 = float(input("Digite o 1° número: "))
        soma2 = float(input("Digite o 2° número: "))
        soma = soma1 + soma2
        print(f"O resultado desta operação matemática é: {soma:.2f}.")
    case 2:
        subtracao1 = float(input("Digite o 1° número: "))
        subtracao2 = float(input("Digite o 2° número: "))
        subtracao = subtracao1 - subtracao2
        print(f"O resultado desta operação matemática é: {subtracao:.2f}.")
    case 3:
        multiplicacao1 = float(input("Digite o 1° número: "))
        multiplicacao2 = float(input("Digite o 2° número: "))
        multiplicacao = multiplicacao1 * multiplicacao2
        print(f"O resultado desta operação matemática é: {multiplicacao:.2f}.")
    case 4:
        divisao1 = float(input("Digite o 1° número: "))
        divisao2 = float(input("Digite o 2° número: "))
        divisao = divisao1 / divisao2
        print(f"O resultado desta operação matemática é: {divisao:.2f}.")
    case _:
        print("Operação matemática inválida.")