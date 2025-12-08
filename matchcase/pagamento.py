"""O usuário escolhe uma forma de pagamento e o programa informa se há desconto ou acréscimo."""

pagamento = int(input("Escolha a forma de pagamento a ser utilizada: \n1. Pix\n2. Crédito \n3. Débito\n4. Dinheiro\n "))

match pagamento:
    case 1:
        print("Pagamentos no pix não tem desconto nem acréscimo. ")
    case 2:
        print("Pagamentos no crédito tem acréscimo de 3%. ")
    case 3:
        print("Pagamentos no débito não tem desconto nem acréscimo. ")
    case 4:
        print("Pagamentos em dinheiro tem desconto de 5%. ")
    case _:
        print("Forma de pagamento inválida. ")