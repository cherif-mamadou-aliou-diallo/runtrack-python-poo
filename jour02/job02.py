class Livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages

    # Assesseurs (getters)
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nombre_de_pages(self):
        return self.__nombre_de_pages

    # Mutateurs (setters) avec validation
    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def set_auteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur

    def set_nombre_de_pages(self, nouveau_nombre_de_pages):
        if isinstance(nouveau_nombre_de_pages, int) and nouveau_nombre_de_pages > 0:
            self.__nombre_de_pages = nouveau_nombre_de_pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

    # Méthode pour afficher les informations du livre
    def afficher_informations(self):
        print(f"Titre : {self.__titre}")
        print(f"Auteur : {self.__auteur}")
        print(f"Nombre de pages : {self.__nombre_de_pages}")


# Exemple d'utilisation de la classe Livre
livre_example = Livre("Solutions", "SONKO", 500)
livre_example.afficher_informations()

# Modifier le titre
livre_example.set_titre("Pétrol et Gaz au Sénégal")

# Modifier le nombre de pages (avec une valeur invalide)
livre_example.set_nombre_de_pages(-100)

# Afficher les informations mises à jour
livre_example.afficher_informations()
