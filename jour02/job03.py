class Livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages
        self.__disponible = True

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nombre_de_pages(self):
        return self.__nombre_de_pages

    def get_disponible(self):
        return self.__disponible

    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def set_auteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur

    def set_nombre_de_pages(self, nouveau_nombre_de_pages):
        if isinstance(nouveau_nombre_de_pages, int) and nouveau_nombre_de_pages > 0:
            self.__nombre_de_pages = nouveau_nombre_de_pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Le livre a été emprunté avec succès.")
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")

    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print("Le livre a été rendu avec succès.")
        else:
            print("Le livre est déjà disponible.")

    def afficher_informations(self):
        print(f"Titre : {self.__titre}")
        print(f"Auteur : {self.__auteur}")
        print(f"Nombre de pages : {self.__nombre_de_pages}")
        print(f"Disponible : {self.__disponible}")


# Exemple d'utilisation de la classe Livre avec les nouvelles fonctionnalités
livre_example = Livre("Solutions", "SONKO", 500)
livre_example.afficher_informations()

# Vérifier la disponibilité
print("Disponible :", livre_example.verification())

# Emprunter le livre
livre_example.emprunter()

# Vérifier la disponibilité après l'emprunt
print("Disponible :", livre_example.verification())

# Rendre le livre
livre_example.rendre()

# Vérifier la disponibilité après le rendu
print("Disponible :", livre_example.verification())
