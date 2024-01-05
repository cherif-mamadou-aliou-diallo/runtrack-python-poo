class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        print(f"{self.nom} attaque {adversaire.nom}!")
        adversaire.vie -= 10
        print(f"{adversaire.nom} perd 10 points de vie. Vie restante : {adversaire.vie}")

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisirNiveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1, 2 ou 3) : "))

    def lancerJeu(self):
        self.choisirNiveau()

        points_de_vie_joueur = self.niveau * 50
        points_de_vie_ennemi = self.niveau * 40

        joueur = Personnage("Joueur", points_de_vie_joueur)
        ennemi = Personnage("Ennemi", points_de_vie_ennemi)

        print(f"\nLa bataille commence ! Niveau {self.niveau}")
        self.deroulementPartie(joueur, ennemi)

    def verifierSante(self, personnage):
        if personnage.vie <= 0:
            print(f"{personnage.nom} a perdu la partie!")

    def verifierGagnant(self, joueur, ennemi):
        if joueur.vie <= 0:
            print("Vous avez perdu la partie. L'ennemi a gagné!")
        elif ennemi.vie <= 0:
            print("Félicitations ! Vous avez vaincu l'ennemi!")

    def demanderAction(self):
        return input("Appuyez sur 'A' pour attaquer : ")

    def deroulementPartie(self, joueur, ennemi):
        while joueur.vie > 0 and ennemi.vie > 0:
            action = self.demanderAction()

            if action.upper() == 'A':
                joueur.attaquer(ennemi)
                ennemi.attaquer(joueur)

                self.verifierSante(joueur)
                self.verifierSante(ennemi)

                self.verifierGagnant(joueur, ennemi)

# Exemple d'utilisation
jeu = Jeu()
jeu.lancerJeu()
