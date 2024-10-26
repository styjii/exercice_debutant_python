import random

mot = "Bonjour"

# mélanger les lettres d'un mot

# methode 1
# n = []
# for i in range(len(mot)):
#     r = random.randint(0, len(mot)-1)
#     while r in n:
#         r = random.randint(0, len(mot)-1)
#     n.append(r)
# mot = ''.join([mot[i] for i in n]).capitalize()

# methode 2
mot = list(mot)
random.shuffle(mot)
mot = ''.join(mot).capitalize()

print(mot)
