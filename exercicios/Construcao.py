"""Faça um algoritmo que leia a largura e altura de uma parede, calcule e mostre
a área a ser pintada e a quantidade de tinta necessária para o serviço
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados."""

largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))

area = largura * altura
tinta = area / 2

print(f"A área da parede é de {area} e você precisará de {tinta} litros de tinta para pintar a parede.")