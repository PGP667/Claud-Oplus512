from games.nim import Nim
from random import randint

jeu = Nim(8)

print(jeu.get_state())

possibilite = jeu.get_state()[3]
tour = jeu.get_state()[0]
nombreAlummette = jeu.get_state()[1]
tourAI = jeu.get_state()[2]

print(f"Nombre d'allumettes restantes : {nombreAlummette}")
print(f"Nombre de tours effectués : {tour}")
print(f"Nombre d'allumettes retirées lors du dernier tour : {tourAI}")
print(f"Possibilités de choix : {possibilite}")


# choix = possibilite[randint(0,1)]
# print(f"Le choix est {choix}")
# 
# 
# print(jeu.play(choix))
