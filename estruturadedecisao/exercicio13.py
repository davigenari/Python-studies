"""Desconto extra em compras altas se pagamento à vista."""

desconto = 0.10
forma_pagamento = input("Informe se o pagamento é a vista ou parcelado: ")
if forma_pagamento.upper() == "PARCELADO":
    valor_compra = float(input("Valor da compra: "))
    if valor_compra >= 500:
        print(f"Você terá um desconto de R$ {valor_compra * desconto:.2f}.")
    else:
        print("Desconto liberado somente para compras acima de R$ 500,00.")
else:
    print("Compra sem desconto.")