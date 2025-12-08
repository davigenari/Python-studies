"""O usuário deve informar o tipo de produto (Eletrônico, Roupas, Alimentos, Móveis), e o programa exibirá o percentual
de desconto correspondente."""

tipo = int(input("Selecione qual tipo de produto quer comprar: \n1. Eletrônicos\n2. Roupas \n3. Alimentos\n4. Móveis\n"))

match tipo:
    case 1:
        print("O desconto para eletrônicos é de 5%.")
    case 2:
        print("O desconto para roupas é de 8%.")
    case 3:
        print("O desconto para Alimentos é de 10%.")
    case 4:
        print("O desconto para móveis é de 15%.")
    case _:
        print("Este tipo de produto não tem desconto.")