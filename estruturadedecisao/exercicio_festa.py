#Entrada em festa: idade ≥18 ou acompanhado dos pais

idade = int(input("Informe a sua idade: "))
acompanhado = input("Você está acompanhado dos seus pais? Caso esteja, digite: Acompanhado. Se não, digite Não acompanhado")
if idade >= 18 or acompanhado == "Acompanhado":
    print("Você pode entrar na festa.")
else idade < 18 or acompanhado =="Não acompanhado"
    print("Você não pode entrar na festa.")
