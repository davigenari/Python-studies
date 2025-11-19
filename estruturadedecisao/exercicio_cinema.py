#Meia-entrada no cinema: estudante ou menor de 18 anos.

estudante = input("Você é estudante? ")
idade = int(input("Informe a sua idade: "))
if estudante == "sim" or idade <= 18:
    print("Você tem meia-entrada no cinema.")
else:
    print("Você não tem direito a meia-entrada no cinema.")