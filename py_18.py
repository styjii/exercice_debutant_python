nombres = range(50)
nombres_paires = []

for chiffre in nombres:
    if chiffre % 2 == 0:
        nombres_paires.append(chiffre)
        
print(nombres_paires)