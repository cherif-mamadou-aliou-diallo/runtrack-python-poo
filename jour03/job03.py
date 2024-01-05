class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, titre):
        self.taches = [t for t in self.taches if t.titre != titre]

    def marquerCommeFinie(self, titre):
        for t in self.taches:
            if t.titre == titre:
                t.statut = "terminée"

    def afficherListe(self):
        for t in self.taches:
            print(f"Titre: {t.titre}, Description: {t.description}, Statut: {t.statut}")

    def filterListe(self, statut):
        return [t for t in self.taches if t.statut == statut]

# Tester le code
tache1 = Tache("Faire les courses", "Acheter des fruits et légumes")
tache2 = Tache("Réviser pour l'examen", "Relire les chapitres 1 à 5")
tache3 = Tache("Faire du sport", "Jogging pendant 30 minutes")

listeDeTaches = ListeDeTaches()
listeDeTaches.ajouterTache(tache1)
listeDeTaches.ajouterTache(tache2)
listeDeTaches.ajouterTache(tache3)

# Afficher la liste initiale
print("Liste initiale:")
listeDeTaches.afficherListe()

# Marquer une tâche comme terminée
listeDeTaches.marquerCommeFinie("Faire les courses")

# Afficher la liste mise à jour
print("\nListe mise à jour:")
listeDeTaches.afficherListe()

# Filtrer les tâches à faire
taches_a_faire = listeDeTaches.filterListe("à faire")
print("\nTâches à faire:")
for t in taches_a_faire:
    print(f"Titre: {t.titre}, Description: {t.description}, Statut: {t.statut}")

# Supprimer une tâche
listeDeTaches.supprimerTache("Réviser pour l'examen")

# Afficher la liste mise à jour après suppression
print("\nListe après suppression:")
listeDeTaches.afficherListe()
