# inverser l'ordre des lettres d'un mot
mot = "Udemy"

# Pour valider l'exercice, il faut que la première lettre de votre chaîne de caractère résultat soit en majuscule ('Ymedu' et non 'ymedU')
# methode 1
# mot = ''.join([mot[i] for i in range(len(mot)-1, -1, -1)]).capitalize()

# methode 2
# mot = list(mot)
# mot.reverse()
# mot = ''.join(mot).capitalize()

# methode 3
mot = mot[::-1].capitalize()

print(mot)
