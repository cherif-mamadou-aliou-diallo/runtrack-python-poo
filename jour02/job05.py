class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._kilometrage = kilometrage
        self._en_marche = False
        self._reservoir = 50  # attribut ajouté

    # Assesseurs
    def get_marque(self):
        return self._marque

    def get_modele(self):
        return self._modele

    def get_annee(self):
        return self._annee

    def get_kilometrage(self):
        return self._kilometrage

    def get_en_marche(self):
        return self._en_marche

    # Mutateurs
    def set_marque(self, nouvelle_marque):
        self._marque = nouvelle_marque

    def set_modele(self, nouveau_modele):
        self._modele = nouveau_modele

    def set_annee(self, nouvelle_annee):
        self._annee = nouvelle_annee

    def set_kilometrage(self, nouveau_kilometrage):
        self._kilometrage = nouveau_kilometrage

    def set_en_marche(self, nouvel_etat):
        self._en_marche = nouvel_etat

    # Méthodes
    def demarrer(self):
        if self.verifier_plein():
            print("La voiture démarre.")
            self.set_en_marche(True)
        else:
            print("Le réservoir est trop bas, la voiture ne peut pas démarrer.")

    def arreter(self):
        print("La voiture s'arrête.")
        self.set_en_marche(False)

    # Méthode privée
    def verifier_plein(self):
        return self._reservoir > 5


# Exemple d'utilisation
ma_voiture = Voiture("Toyota", "Corolla", 2022, 40000)
ma_voiture.demarrer()  # La voiture ne peut pas démarrer car le réservoir est trop bas
ma_voiture.set_en_marche(True)
print("En marche:", ma_voiture.get_en_marche())  # Affiche True
ma_voiture.arreter()
print("En marche:", ma_voiture.get_en_marche())  # Affiche False
