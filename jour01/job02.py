class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
# instanciation de la classe Operation
operation_instance = Operation(nombre1=12, nombre2=3)

# Imprimer les valeurs des attributs
print("Le nombre1 est", operation_instance.nombre1)
print("Le nombre2 est", operation_instance.nombre2)
