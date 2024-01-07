class Forme:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur


class Cercle(Forme):
    def __init__(self, radius):
        super().__init__(radius, radius)
        self.radius = radius

    def aire(self):
        return 3.14 * self.radius**2


# Création d'une instance de la classe Rectangle
rectangle = Forme(5, 10)

# Affichage de l'aire du rectangle
print("Aire du rectangle:", rectangle.aire())

# Création d'une instance de la classe Cercle
cercle = Cercle(7)

# Affichage de l'aire du cercle
print("Aire du cercle:", cercle.aire())
