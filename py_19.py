liste = ["Pierre", "Paul", "Marie"]

for i, nom in enumerate(liste):
    print(i, nom)

print(f"{'-'*15} *** {'-'*15}")

nombres = range(50)
nombre_paires = [i for i in nombres if i % 2 == 0]
print(nombre_paires)