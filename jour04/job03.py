class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # Méthode pour calculer le périmètre du rectangle
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    # Méthode pour calculer la surface du rectangle
    def surface(self):
        return self.__longueur * self.__largeur

    # Assesseurs pour récupérer les valeurs des attributs
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    # Mutateurs pour modifier les valeurs des attributs
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    # Méthode pour calculer le volume du parallélépipède
    def volume(self):
        return self.surface() * self.__hauteur

    # Assesseur pour récupérer la valeur de l'attribut hauteur
    def get_hauteur(self):
        return self.__hauteur

    # Mutateur pour modifier la valeur de l'attribut hauteur
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur


# Instanciation de la classe Rectangle
rectangle = Rectangle(4, 8)

# Utilisation des méthodes et affichage des résultats
print("Rectangle:")
print("Périmètre:", rectangle.perimetre())
print("Surface:", rectangle.surface())

# Modification des valeurs avec les mutateurs
rectangle.set_longueur(14)
rectangle.set_largeur(9)

# Affichage des nouvelles valeurs
print("\nNouvelles valeurs du rectangle:")
print("Longueur:", rectangle.get_longueur())
print("Largeur:", rectangle.get_largeur())
print("Périmètre:", rectangle.perimetre())
print("Surface:", rectangle.surface())

# Instanciation de la classe Parallelepipede
parallelepipede = Parallelepipede(6, 9, 3)

# Utilisation des méthodes de la classe Parallelepipede
print("\nParallélépipède:")
print("Volume:", parallelepipede.volume())

# Modification de la hauteur avec le mutateur
parallelepipede.set_hauteur(5)

# Affichage de la nouvelle valeur de la hauteur et du nouveau volume
print("\nNouvelle hauteur du parallélépipède:", parallelepipede.get_hauteur())
print("Nouveau volume:", parallelepipede.volume())
