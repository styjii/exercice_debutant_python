# The f-string
nombre = 2938.48872
decimales = 3

# nombre:.3f => rounding 3 number after comma
print("Nombre tronqué: {0:.{1}f}".format(nombre, decimales))
# round(float, number of the float)
print(f"Nombre tronqué: {round(nombre, decimales)}")