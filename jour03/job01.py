class Ville:
    def __init__(self, nom, nombre_habitants):
        self._nom = nom
        self._nombre_habitants = nombre_habitants

    def get_nombre_habitants(self):
        return self._nombre_habitants

    def augmenter_population(self, nombre=1):
        self._nombre_habitants += nombre


class Personne:
    def __init__(self, nom, age, ville):
        self._nom = nom
        self._age = age
        self._ville = ville

    def ajouterPopulation(self):
        self._ville.augmenter_population()


# Créer un objet Ville avec comme arguments “Paris” et 1000000.
paris = Ville("Paris", 1000000)

# Afficher en console le nombre d’habitants de la ville de Paris.
print(f"Nombre d'habitants à {paris._nom}: {paris.get_nombre_habitants()}")

# Créer un autre objet Ville avec comme arguments “Marseille” et 861635.
marseille = Ville("Marseille", 861635)

# Afficher en console le nombre d’habitants de la ville de Marseille.
print(f"Nombre d'habitants à {marseille._nom}: {marseille.get_nombre_habitants()}")

# Créer les objets suivants :
# - John, 45 ans, habitant à Paris
# - Myrtille, 4 ans, habitant à Paris.
# - Chloé, 18 ans, habitant à Marseille.
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Afficher le nombre d’habitants de Paris et de Marseille après l’arrivée de ces nouvelles personnes.
print(f"Nombre d'habitants à {paris._nom} après l'arrivée de John et Myrtille: {paris.get_nombre_habitants()}")
print(f"Nombre d'habitants à {marseille._nom} après l'arrivée de Chloé: {marseille.get_nombre_habitants()}")
