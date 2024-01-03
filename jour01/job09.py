class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
        prixTTC = self.prixHT * (1 + self.TVA / 100)
        return prixTTC

    def afficher(self):
        info_produit = f"Nom: {self.nom}, Prix HT: {self.prixHT}, TVA: {self.TVA}%"
        return info_produit

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def getNom(self):
        return self.nom

    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA

# Création de plusieurs produits
produit1 = Produit("Produit A", 50.0, 20)
produit2 = Produit("Produit B", 30.0, 10)

# Affichage des informations initiales
print(produit1.afficher())
print(produit2.afficher())

# Calcul des prix TTC
prix_ttc_produit1 = produit1.calculerPrixTTC()
prix_ttc_produit2 = produit2.calculerPrixTTC()

print(f"Prix TTC de {produit1.getNom()}: {prix_ttc_produit1}")
print(f"Prix TTC de {produit2.getNom()}: {prix_ttc_produit2}")

# Modification du nom et du prix de chaque produit
produit1.modifierNom("Nouveau Produit A")
produit1.modifierPrixHT(60.0)

produit2.modifierNom("Nouveau Produit B")
produit2.modifierPrixHT(40.0)

# Affichage des nouvelles informations
print(produit1.afficher())
print(produit2.afficher())

# Calcul des nouveaux prix TTC
nouveau_prix_ttc_produit1 = produit1.calculerPrixTTC()
nouveau_prix_ttc_produit2 = produit2.calculerPrixTTC()

print(f"Nouveau prix TTC de {produit1.getNom()}: {nouveau_prix_ttc_produit1}")
print(f"Nouveau prix TTC de {produit2.getNom()}: {nouveau_prix_ttc_produit2}")
