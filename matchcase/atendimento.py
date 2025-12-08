"""O usuário seleciona uma opção de atendimento telefônico."""

while True:
    print("\n===== Atendimento Telefônico =====")
    print("1 - Suporte técnico")
    print("2 - Financeiro")
    print("3 - Cancelamento")
    print("4 - Falar com um atendente")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            print("Aguarde um pouco na linha e o atendente já entrará em contato.")

        case "2":
            print("Iremos te encaminhar ao setor financeiro. Por favor, aguarde um pouco na linha.")

        case "3":
            print("Sentimos muito por isso. Você será encaminhado ao setor de cancelamento para que possamos prosseguir.")

        case "4":
            print("Iremos te encaminhar a um atendente que possa te auxiliar.")

        case "5":
            print("Saindo. Obrigado por utilizar nosso sistema de atendimento!")
            break

        case _:
            print("Opção inválida. Por favor, selecione outra.")