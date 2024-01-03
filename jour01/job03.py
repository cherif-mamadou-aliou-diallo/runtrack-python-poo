class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        result = self.nombre1 + self.nombre2
        print("Résultat de l'addition :", result)

# Exemple
operation_instance = Operation(nombre1=15, nombre2=5)
operation_instance.addition()
