import os

fichier = "C://Python36/python.exe"

# récupérer l'extention
# methode 1
# extention = (os.path.basename(fichier)).split('.')[1]

# methode 2
extention = os.path.splitext(fichier)[1]
extention = extention.strip(".")

print(extention)
