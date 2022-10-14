# Titre : EXERCICE DU 14 Octobre 2022
# Nom du projet : EXERCICES
# Dernière révision : 14 oct 2022
# Auteur : Théo Lalande
# IDE : VSCode
# Client : 


############################
#Programme principal
############################

from codecs import latin_1_decode
from random import *

#Exercice a -> Retourne un chiffre aléatoire entre 1 & 10
print(randint(1,10))
print(random.randrange(1,10))
#Exercice b -> Retourne la longueur de la chaine de caractère a
a = "lait"
print(len(a))
#Exercice c -> Permet de savoir si un mot se trouve dans une chaine de caractère ou non
a= "voila la phrase"
if("la" in a):
  print("La est dans la phrase")
else:
  print("pas dans le texte")
#Exercice d -> Meme chose que exercice c mais inversé
a= "voila la phrase"
if("Li" not in a):
  print("Li n'est pas dans la phrase")
else:
  print("Li est dans la phrase")
#Exercice e ->
a="Exemple"
print(a[2:4])
#EXERCICE 1 -> Exercice de déclaration de variables
age = 20
majeur = True
compte_en_banque = 20135.384
amis = ["Marie", "Julien", "Adrien"]
parents = ("Marc", "Caroline")

print(age)
print(majeur)
print(compte_en_banque)
print(amis)
print(parents)

#EXERCICE 2 (corriger l'erreur) -> L'erreur était une double appostrophe au lieu d'un guillement
site_web = "google"
print(site_web)

#EXERCICE 3 -> Exercice de concaténation
nombre = 17
print("Le nombre est " + str(nombre))

#EXERCICE 4 : Trouver la valeur de la variable. On veut "printer" la valeur que contient la variable a
a=3
b=6
a=b
b=7

print(a)   # => Retourn 6

#EXERCICE 5 : Comment printer la somme de 3 valeurs
table = [2, 6, 3]
print(sum(table)) # -> Retourne 2+6+3

#EXERCICE 6 : Corriger le code
list1 = range(3) # On a remplacer list par list1 (list étant une mot clé reservé)
list2 = range(5)
print(list(list2))

#EXERCICE 7 : Vérifier qu'une variable est bien d'un certain type
prenom = "Vincent"
if isinstance(prenom, str): # Si il s'agit d'un string
  print("C'est un String")
elif isinstance(prenom, int): # Si il s'agit d'un int
  print("C'est un Int")
else:
  print("Ni l'un ni l'autre") # Si il s'agit ni d'un string ni d'un int

#EXERCICE 8 : Remplacer un mot par un autre 
chaine1 = "salut les dev, salut alors ca va" 
print(chaine1.replace("salut" , "Bonsoir", 1)) # -> Remplace le premier salut par bonsoir