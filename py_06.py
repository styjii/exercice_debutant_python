from time import time
# time actuel
a = time()
_ = [i*2 for i in range(9999999)]
# temps après l'exécution du _
print(f"Temps d'exécution: {time() - a}s")
# temps après l'exécution - temps actuel
