"""Crie um programa que simule um sistema de login. Solicite um nome de usuário e senha e verifique se as credenciais
estão corretas."""
usuario = (input("Digite o seu usuário: "))
senha = (input("Digite a sua senha: "))

if usuario == "davigenari" and senha == "dgia":
    print("Credenciais corretas. Acesso liberado.")
else:
    print("Credenciais incorretas. Acesso negado.")