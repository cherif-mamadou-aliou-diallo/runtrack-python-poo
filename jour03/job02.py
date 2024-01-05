class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Numéro de compte : {self.__numero_compte}")
        print(f"Nom : {self.__nom}")
        print(f"Prénom : {self.__prenom}")
        print(f"Solde : {self.__solde} €")
        print(f"Autorisation de découvert : {'Oui' if self.__decouvert else 'Non'}")

    def afficherSolde(self):
        print(f"Solde actuel : {self.__solde} €")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant} € effectué. Nouveau solde : {self.__solde} €")

    def retrait(self, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            print(f"Retrait de {montant} € effectué. Nouveau solde : {self.__solde} €")
        else:
            print("Solde insuffisant. Opération impossible.")

    def agios(self, taux_agios):
        if self.__solde < 0:
            agios = abs(self.__solde) * taux_agios
            self.__solde -= agios
            print(f"Des agios de {agios} € ont été appliqués. Nouveau solde : {self.__solde} €")

    def virement(self, compte_destinataire, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} € effectué vers le compte {compte_destinataire.__numero_compte}.")
        else:
            print("Solde insuffisant. Opération impossible.")

# Création d'une première instance de la classe CompteBancaire
compte1 = CompteBancaire(numero_compte="123456", nom="Dupont", prenom="Jean", solde=1000)

# Affichage des détails du compte
compte1.afficher()

# Versement sur le compte
compte1.versement(500)

# Affichage du solde
compte1.afficherSolde()

# Retrait du compte
compte1.retrait(200)

# Création d'une deuxième instance de la classe CompteBancaire à découvert
compte2 = CompteBancaire(numero_compte="789012", nom="Martin", prenom="Alice", solde=-200, decouvert=True)

# Affichage des détails du compte à découvert
compte2.afficher()

# Virement du compte1 vers le compte2 pour remettre le solde à zéro
compte1.virement(compte_destinataire=compte2, montant=1500)

# Affichage des détails mis à jour
compte1.afficher()
compte2.afficher()
