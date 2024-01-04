class Student:
    def __init__(self, nom, prenom, numero_etudiant, credits=0):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = credits
        self.__level = self.__student_eval()

    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom

    def get_numero_etudiant(self):
        return self.__numero_etudiant

    def get_credits(self):
        return self.__credits

    def get_level(self):
        return self.__level

    def set_nom(self, nouveau_nom):
        self.__nom = nouveau_nom

    def set_prenom(self, nouveau_prenom):
        self.__prenom = nouveau_prenom

    def set_numero_etudiant(self, nouveau_numero_etudiant):
        self.__numero_etudiant = nouveau_numero_etudiant

    def add_credits(self, nombre_credits):
        if nombre_credits > 0:
            self.__credits += nombre_credits
            self.__level = self.__student_eval()
        else:
            print("Erreur : Le nombre de crédits ajouté doit être supérieur à zéro.")

    def student_info(self):
        print(f"Nom : {self.__nom}")
        print(f"Prénom : {self.__prenom}")
        print(f"Numéro d'étudiant : {self.__numero_etudiant}")
        print(f"Niveau : {self.__level}")
        print(f"Crédits : {self.__credits}")

    # Méthode privée pour évaluer le niveau de l'étudiant
    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

# Exemple d'utilisation de la classe Student
john_doe = Student("Doe", "John", 145)
john_doe.add_credits(40)
john_doe.add_credits(20)
john_doe.add_credits(25)

# Afficher les informations de l'étudiant
john_doe.student_info()
