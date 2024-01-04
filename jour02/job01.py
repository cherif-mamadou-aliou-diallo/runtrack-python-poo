class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # Assesseurs
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    # Mutateurs
    def set_longueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur

    def set_largeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur

# Créer un rectangle avec les valeurs initiales
mon_rectangle = Rectangle(10, 5)

# Afficher les valeurs initiales
print("Longueur initiale:", mon_rectangle.get_longueur())
print("Largeur initiale:", mon_rectangle.get_largeur())

# Modifier les valeurs
mon_rectangle.set_longueur(14)
mon_rectangle.set_largeur(9)

# Afficher les valeurs après modification
print("Nouvelle longueur:", mon_rectangle.get_longueur())
print("Nouvelle largeur:", mon_rectangle.get_largeur())
