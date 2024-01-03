class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y -= 1

    def bas(self):
        self.y += 1

    def position(self):
        return (self.x, self.y)

# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'un personnage à la position (2, 3)
    joueur = Personnage(2, 3)

    # Affichage de la position initiale
    print("Position initiale :", joueur.position())

    # Déplacement vers la gauche et le haut
    joueur.gauche()
    joueur.haut()

    # Affichage de la nouvelle position
    print("Nouvelle position :", joueur.position())
