class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts_marques += 1

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        print(f"Statistiques de {self.nom} (#{self.numero}, {self.position}):")
        print(f"Buts marqués: {self.buts_marques}")
        print(f"Passes décisives: {self.passes_decisives}")
        print(f"Cartons jaunes: {self.cartons_jaunes}")
        print(f"Cartons rouges: {self.cartons_rouges}")
        print()


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.liste_joueurs = []

    def ajouterJoueur(self, joueur):
        self.liste_joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques de l'équipe {self.nom}:")
        for joueur in self.liste_joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, numero_joueur, action):
        for joueur in self.liste_joueurs:
            if joueur.numero == numero_joueur:
                if action == 'but':
                    joueur.marquerUnBut()
                elif action == 'passe':
                    joueur.effectuerUnePasseDecisive()
                elif action == 'jaune':
                    joueur.recevoirUnCartonJaune()
                elif action == 'rouge':
                    joueur.recevoirUnCartonRouge()


# Création des joueurs
joueur1 = Joueur("Messi", 10, "Attaquant")
joueur2 = Joueur("Ronaldo", 7, "Attaquant")
joueur3 = Joueur("Mbappe", 11, "Attaquant")

# Création des équipes
equipe1 = Equipe("Équipe A")
equipe2 = Equipe("Équipe B")

# Ajout des joueurs aux équipes
equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur3)

# Affichage des statistiques initiales des joueurs
print("Statistiques initiales des joueurs:")
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()

# Simulation du match
equipe1.mettreAJourStatistiquesJoueur(10, 'but')  # Messi marque un but
equipe1.mettreAJourStatistiquesJoueur(7, 'jaune')  # Ronaldo reçoit un carton jaune
equipe2.mettreAJourStatistiquesJoueur(11, 'passe')  # Mbappe effectue une passe décisive

# Affichage des statistiques après le match
print("Statistiques après le match:")
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()
