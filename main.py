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