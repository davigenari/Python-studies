'''Cálculo do tempo de viagem: Peça a distância a ser percorrida e a velocidade média, depois calcule o tempo da viagem'''

distancia = int(input("Insira a distância a ser percorrida: "))
vm = int(input("Insira a sua velocidade média: "))
tempo = distancia / vm

print(f"O tempo da sua viagem é {tempo: .2f} horas")