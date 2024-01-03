class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def sePresenter(self):
        return f"Je m'appelle {self.nom} {self.prenom}"

# Instanciation de plusieurs personnes
personne1 = Personne("Doe", "John")
personne2 = Personne("Diallo", "Cherif")
personne3 = Personne("Dupont", "Pierre")

# Appel à la méthode SePresenter pour vérifier
print(personne1.sePresenter())
print(personne2.sePresenter())
print(personne3.sePresenter())
