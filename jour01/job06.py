class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nouveau_prenom):
        self.prenom = nouveau_prenom

# Instanciation de l'objet Animal
mon_animal = Animal()

# Affichage de l'âge initial et du prénom initial
print("Âge initial de l'animal :", mon_animal.age)
print("Prénom initial de l'animal :", mon_animal.prenom)

# Faire vieillir l'animal
mon_animal.vieillir()

# Nommer l'animal
mon_animal.nommer("Luna")

# Affichage de l'âge après avoir vieilli et du nouveau prénom
print("Âge de l'animal après avoir vieilli :", mon_animal.age)
print("Nouveau prénom de l'animal :", mon_animal.prenom)
