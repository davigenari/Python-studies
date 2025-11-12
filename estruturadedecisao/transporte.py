"""Transporte escolar: distância >2 km e frequência ≥80%."""

distancia = float(input("informe a distância da casa do aluno até a escola: "))
if distancia >= 2:
    print("A frequência do aluno é maior que 80%? ")
    frequencia = input("")
    if frequencia.upper() == "SIM":
        print("O aluno está apto ao transporte escolar.")
    else:
        print("O aluno não está apto ao transporte escolar.")
else:
    print("O aluno NÃO está apto ao transporte escolar.")