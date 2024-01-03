class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Point: ({self.x}, {self.y})")

    def afficherX(self):
        print(f"Coordonnée horizontale (x): {self.x}")

    def afficherY(self):
        print(f"Coordonnée verticale (y): {self.y}")

    def changerX(self, nouveau_x):
        self.x = nouveau_x

    def changerY(self, nouveau_y):
        self.y = nouveau_y

# Exemple d'utilisation
point1 = Point(2, 4)

# Afficher les coordonnées initiales
point1.afficherLesPoints()

# Afficher les coordonnées séparément
point1.afficherX()
point1.afficherY()

# Changer les coordonnées
point1.changerX(6)
point1.changerY(9)

# Afficher les nouvelles coordonnées
point1.afficherLesPoints()
