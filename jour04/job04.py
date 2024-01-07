class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

# Création d'une instance de la classe Rectangle avec une largeur de 5 et une hauteur de 10
rectangle_instance = Rectangle(5, 10)

# Affichage du résultat de la méthode aire de la classe Rectangle
print("L'aire du rectangle est :", rectangle_instance.aire())
