"""O usuário informa uma cor em português (vermelho, azul, verde, amarelo), e o programa exibe sua tradução para inglês."""

cor = int(input("Escolha a cor que você quer traduzir o nome: \n1. Vermelho\n2. Azul \n3. Verde\n4. Amarelo\n"))

match cor:
    case 1:
        print("Vermelho em inglês é: red.")
    case 2:
        print("Azul em inglês é: blue.")
    case 3:
        print("Verde em inglês é: green.")
    case 4:
        print("Amarelo em inglês é: yellow.")
    case _:
        print("Cor inválida, por favor, selecione outra.")