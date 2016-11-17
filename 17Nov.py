#!/usr/bin/python3

import sys

# On a 2 variables temps et distance, calculer la vitesse
temps = 6.896
distance = 19.7
vitesse = distance/temps

#affichage
print("la vitesse est de {:.2f} par métre seconde".format(vitesse), '\n')

# En utilisant la fonction range, afficher les entiers de 0 à 3
for num in range(0,4):
    print(num)

print('\n')

# afficher les entiers de 4 à 7
for num in range(0,10):
    if num > 3 and num < 8:
        print(num)

# avec une boucle for afficher les caractères de la chaine suivante
msg = "C'est la formation DevOps"

for c in msg:
    print("caractère: ", c)

# Sur la liste suivante faire les actions:
liste = [17, 38, 10, 25, 72]
# trier et afficher la liste:
liste.sort()
print(liste)
# ajouter l'élément 12
liste.append(12)
print(liste)
# afficher l'indice de l'élément 17
print(liste.index(17))
# enlever l'élément 38
liste.remove(38)
# afficher la liste
print(liste)
# afficher la sous-liste du 3eme élément jusqu'à la fin de la liste
print(liste[2:])

a = ['a','b','c','d','e','f','g','h']
print(a[:4])

#
print(liste[2:])
