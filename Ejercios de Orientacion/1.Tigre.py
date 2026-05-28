class Animal:
    def __init__(self, nombre, habitat, dieta):
        self.nombre = nombre
        self.habitat = habitat
        self.dieta = dieta

    def describir(self):
        print(f"Animal: {self.nombre}")


class Tigre(Animal):
    def __init__(self, nombre, habitat, dieta, color, peso, velocidad):
        super().__init__(nombre, habitat, dieta)
        self.color = color
        self.peso = peso
        self.velocidad = velocidad

    def mostrar_color(self):
        print("Color del tigre:", self.color)

    def mostrar_peso(self):
        print("Peso del tigre:", self.peso)

    def mostrar_velocidad(self):
        print("Velocidad del tigre:", self.velocidad)


tigre1 = Tigre("Tigre de Bengala", "Selva tropical", "Carnívoro", "Naranja con rayas negras", "220 kg", "65 km/h")
print("=== TIGRE ===")
tigre1.mostrar_color()
tigre1.mostrar_peso()
tigre1.mostrar_velocidad()