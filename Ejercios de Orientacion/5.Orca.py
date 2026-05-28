class Animal:
    def __init__(self, especie, clase, longevidad):
        self.especie = especie
        self.clase = clase
        self.longevidad = longevidad

    def nadar(self):
        print(f"La {self.especie} está nadando")


class Orca(Animal):
    def __init__(self, especie, clase, longevidad, longitud, peso, velocidad):
        super().__init__(especie, clase, longevidad)
        self.longitud = longitud
        self.peso = peso
        self.velocidad = velocidad

    def mostrar_longitud(self):
        print("Longitud de la orca:", self.longitud)

    def mostrar_peso(self):
        print("Peso de la orca:", self.peso)

    def mostrar_velocidad(self):
        print("Velocidad de la orca:", self.velocidad)


orca1 = Orca("Orcinus orca", "Mamífero marino", "60-80 años", "7 metros", "5500 kg", "56 km/h")
print("\n=== ORCA ===")
orca1.mostrar_longitud()
orca1.mostrar_peso()
orca1.mostrar_velocidad()
