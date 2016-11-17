#!/usr/bin/python3

import sys

# affiche les infos de  la version
print(sys.version_info)
# affiche la version
print(sys.version)

# Affiche la plateforme: linux
print(sys.platform)

# affiche hello world
print("hello world")

# affiche les guillemets
print('"hello world"')

# il y'a également les trilpes cotes: conserve la structure du text
print("""test
    sur la structure
        du text""")

# caractères spéciaux: doubler pour afficher l'anti slash
print("c'est le text dans c:\\user")

# Chaines de caractères
str = "Spam"
print(str)

# Création d'une liste
strAdresse = "Spam"
print(strAdresse)

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# afficher les 4 premiers caractères
print(a[:4])

# afficher les 4 derniers caractères
#print(a[4:8]) si on connait le length
print(a[-4:])

# afficher les 4 caractères du milieu
#print(a[3:5])
print(a[3:-3])


# formatage des chaines de caractères pour afficher une variable: %d pour les entiers et %s pour les strings
i = 5
mykey = "temps"
fois = 20
print('la valeur {} et le mot \'{}\' apparaissent {} fois.' .format (i, mykey, fois))

# Tests conditionnels
valeur = "toto"
if valeur == "cat":
    print("ok")
elif valeur == "dog":
    print(" dog ok")
else:
    print("valeur inconnue", '\n')


# séquence de liste
seq = [1, 2, 3, 4]
a, b, c, d = seq
print(b, '\n')

# boucle for
for letter in "spam":
    print("current letter", letter, '\n')


fruits = ['banane', 'pomme', 'mangue']
for fruit in fruits:
    print("mon fruit", fruit, '\n')

for num in range(1,10):
    print(num)

fruits = ['banane', 'pomme', 'mangue']
for fruit in fruits:
    if fruit == "banane":
        print(fruit[2], '\n')
    print(" mon fruit", fruit)

for num in range(1,10):
    print(num)
    if num == 5:
        continue
        if num == 7:
            break

var = 10
while True:
    var -= 1
    if(var == 6):
        continue
    print(var)
    if (var == 0):
        break
print("fin de la boucle", '\n')

# comprehension list
a = [1,2,3,4,5,6,7,8,9,10]
squares = [x**2 for x in a]
print(squares)