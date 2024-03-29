class Commande:
    def __init__(self, numero_commande):
        self._numero_commande = numero_commande
        self._plats_commandes = {}  # Dictionnaire pour stocker les plats (nom, prix, statut)
        self._statut_commande = "en cours"

    # Méthode privée pour calculer le total de la commande
    def _calculer_total(self):
        total = sum(plat['prix'] for plat in self._plats_commandes.values())
        return total

    # Méthode pour ajouter un plat à la commande
    def ajouter_plat(self, nom_plat, prix_plat):
        if nom_plat not in self._plats_commandes:
            self._plats_commandes[nom_plat] = {'prix': prix_plat, 'statut': self._statut_commande}
            print(f"Plat '{nom_plat}' ajouté à la commande.")

    # Méthode pour annuler la commande
    def annuler_commande(self):
        self._statut_commande = "annulée"
        print("Commande annulée.")

    # Méthode pour afficher la commande avec le total à payer
    def afficher_commande(self):
        print(f"Commande #{self._numero_commande}:")
        for nom_plat, details_plat in self._plats_commandes.items():
            print(f"- {nom_plat}: {details_plat['prix']} €")
        total = self._calculer_total()
        print(f"Total à payer: {total} €")

    # Méthode pour calculer la TVA (20% par défaut)
    def calculer_tva(self, taux_tva=0.2):
        total = self._calculer_total()
        tva = total * taux_tva
        return tva


# Exemple d'utilisation
commande_1 = Commande(numero_commande=1)
commande_1.ajouter_plat("Pizza Margherita", 08.99)
commande_1.ajouter_plat("Pâtes Carbonara", 12.99)
commande_1.afficher_commande()  # Affiche la commande avec les plats ajoutés
tva_commande_1 = commande_1.calculer_tva()  # Calcule la TVA par défaut (20%)
print(f"TVA à payer pour la commande 1: {tva_commande_1} €")

commande_1.annuler_commande()  # Annule la commande
commande_1.afficher_commande()  # Affiche la commande annulée
