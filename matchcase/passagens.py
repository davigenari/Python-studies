"""O usuário escolhe um destino (São Paulo, Rio de Janeiro, Curitiba, Salvador) e recebe o valor da passagem."""

passagem = int(input("Escolha a passagem que você quer comprar: \n1. São Paulo\n2. Rio de Janeiro \n3. Curitiba\n4. Salvador\n"))

match passagem:
    case 1:
        print("O valor da passagem para São Paulo está R$ 500,00.")
    case 2:
        print("O valor da passagem para Rio de Janeiro está R$ 900,00.")
    case 3:
        print("O valor da passagem para Curitiba está R$ 621,70.")
    case 4:
        print("O valor da passagem para Salvador está R$ 1.090,79.")
    case _:
        print("Destino inválido. Selecione outro.")