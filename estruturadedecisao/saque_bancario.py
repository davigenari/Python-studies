"""Saque bancário: conta ativa e saldo suficiente."""

saldo_conta = 1000
conta = input("Você tem uma conta ativa neste banco?")
if conta.upper() == "SIM":
    print("Qual valor de saque desejado?")
    saque = float(input("Valor do saque: "))
    if saque > saldo_conta:
        print(f"Você não tem este saldo disponível. Saldo atual: R$ {saldo_conta}.")
    if saque < saldo_conta:
            print(f"Saque realizado. Saldo atual: R$ {saldo_conta - saque}.")

else:
    print("Você não pode realizar nenhuma ação.")