class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def bonjour(self):
        print(f"Bonjour, je m'appelle {self.nom}.")

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours.")

class Professeur(Personne):
    def enseigner(self):
        print("Le cours commence.")

# Création d'un objet Eleve
eleve1 = Eleve(nom="Fatima", age=23)
eleve1.bonjour()  # Appeler la méthode bonjour de la classe Personne
eleve1.allerEnCours()  # Appeler la méthode allerEnCours de la classe Eleve

# Redéfinir l'âge de l'élève à 23 ans
eleve1.age = 23

# Création d'un objet Professeur
professeur1 = Professeur(nom="Professeur1", age=40)
professeur1.bonjour()  # Appeler la méthode bonjour de la classe Personne du Professeur
professeur1.enseigner()  # Appeler la méthode enseigner de la classe Professeur
