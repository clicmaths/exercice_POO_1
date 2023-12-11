
import random
#Question 1
class StringFoo:
    def __init__(self):
        self.attribut = None

    def set_string(self, parametre):
        self.attribut = parametre

    def print_string(self):
        print(self.attribut.upper())


variable = StringFoo()
variable.set_string('allo')
variable.print_string()

#Question 2
class Rectangle:
    def __init__(self,longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def calcul_aire(self):
        return self.longueur * self.largeur

    def afficher_infos(self):
        print("longueur:", self.longueur)
        print("largeur:", self.largeur)
        print("aire:", self.calcul_aire())

forme = Rectangle(12, 2)
forme.afficher_infos()

#Question 3
from math import pi
class cercle:
    def __init__(self,rayon):
        self.rayon = float(rayon)
    def calcul_aire(self):
        return pi*self.rayon*self.rayon
    def calcul_circonference(self):
        return 2*self.rayon*pi

cercle1 = cercle(8)
print(cercle1.calcul_aire())
print(cercle1.calcul_circonference())

#Question 4

class hero:
    def __init__(self,nom):
        self.hp = random.randint(1,10) + random.randint(1,10)
        self.force_attaque = random.randint(1,6)
        self.force_defence = random.randint(1,6)
        self.nom_heros = nom

    def attaque(self):
        return random.randint(1,6)+self.force_attaque

    def dommages(self, nb_dommage):
        self.hp -= (nb_dommage - self.force_defence)

    def vivant(self):
        if self.hp > 0:
            return True
        else:
            False
        return self.hp > 0

