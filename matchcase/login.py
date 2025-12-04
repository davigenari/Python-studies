"""O programa deve pedir ao usuário que informe seu nome de usuário e, com base nisso, conceder um nível de acesso:"""

usuario = int(input("Selecione qual tipo de usuário quer acessar: \n1. Admin\n2. Professor \n3. Aluno\n"))

match usuario:
    case 1:
        senhaadm = input("Insira a senha do usuário Admin: ")
        if senhaadm.upper() == 'A123D':
                print("Acesso total liberado.")
        else:
                print("Senha incorreta.")
    case 2:
        senhaprof = input("Insira a senha do usuário Professor: ")
        if senhaprof.upper() == 'P123R':
                print("Acesso ao ambiente acadêmico liberado.")
        else:
                print("Senha incorreta.")
    case 3:
        senhaaluno = input("Insira a senha do usuário Aluno: ")
        if senhaaluno.upper() == 'A123L':
                print("Acesso ao ambiente de estudos liberado.")
        else:
                print("Senha incorreta.")
    case _:
        print("Opção inválida, tente novamente.")