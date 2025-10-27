"""Empréstimo na biblioteca: precisa estar cadastrado e sem atraso."""

usuario = input("O leitor está cadastrado? ")
if usuario.upper() == "SIM":
    atraso = input("O leitor tem algum atraso? ")
    if atraso.upper() == "SIM":
        print("O leitor não pode pegar nenhum livro por conta de atraso.")
    else:
        print("Empréstimo liberado.")
else: print("Faça o cadastro para prosseguir com o empréstimo do livro.")