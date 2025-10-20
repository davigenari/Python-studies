"""Sistema de login com usuário e senha."""

user_correto = "admin"
senha_correta = "4dm1n"

usuario = input("Digite o seu usuário: ")
if usuario == user_correto:
    print("Usuário correto.")
    senha = input("Agora, digite sua senha: ")
    if senha == senha_correta:
        print("Acesso liberado.")
    else: print("Acesso negado.")
else:
    print("Usuário não encontrado.")