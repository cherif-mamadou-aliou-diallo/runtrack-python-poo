import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = self.creer_paquet()

    def creer_paquet(self):
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        return paquet

    def melanger_paquet(self):
        random.shuffle(self.paquet)

    def distribuer_cartes(self):
        main_joueur = [self.tirer_carte(), self.tirer_carte()]
        main_croupier = [self.tirer_carte(), self.tirer_carte()]
        return main_joueur, main_croupier

    def tirer_carte(self):
        carte = self.paquet.pop()
        return carte

    def calculer_points(self, main):
        points = 0
        as_present = False

        for carte in main:
            if carte.valeur.isdigit():
                points += int(carte.valeur)
            elif carte.valeur in ['J', 'Q', 'K']:
                points += 10
            elif carte.valeur == 'A':
                as_present = True
                points += 11

        # Gérer les as
        if as_present and points > 21:
            points -= 10

        return points

    def afficher_main(self, main, joueur):
        print(f"Main {joueur}:")
        for carte in main:
            print(f"{carte.valeur} de {carte.couleur}")
        print(f"Total des points: {self.calculer_points(main)}")

# Exemple d'utilisation
jeu = Jeu()
jeu.melanger_paquet()
main_joueur, main_croupier = jeu.distribuer_cartes()

jeu.afficher_main(main_joueur, "Joueur")
jeu.afficher_main(main_croupier, "Croupier")
