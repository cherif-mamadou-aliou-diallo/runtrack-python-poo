class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print("Âge de la personne:", self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, new_age):
        self.age = new_age


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print("J'ai", self.age, "ans")


class Professeur(Personne):
    def __init__(self, age=14, matiereEnseignee=""):
        super().__init__(age)
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")


# Instanciation d'une classe Personne avec l'âge par défaut
personne = Personne()
personne.afficherAge()  # Affiche : Âge de la personne: 14
personne.bonjour()  # Affiche : Hello

# Instanciation d'une classe Eleve
eleve = Eleve()
eleve.afficherAge()  # Affiche : J'ai 14 ans
eleve.bonjour()  # Affiche : Hello
eleve.allerEnCours()  # Affiche : Je vais en cours

# Instanciation d'une classe Professeur
professeur = Professeur(age=30, matiereEnseignee="Mathématiques")
professeur.afficherAge()  # Affiche : Âge de la personne: 30
professeur.enseigner()  # Affiche : Le cours va commencer
