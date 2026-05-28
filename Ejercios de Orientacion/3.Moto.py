class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def arrancar(self):
        print(f"La {self.marca} {self.modelo} ha arrancado")


class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, color, cilindrada, peso):
        super().__init__(marca, modelo, año)
        self.color = color
        self.cilindrada = cilindrada
        self.peso = peso

    def mostrar_color(self):
        print("Color de la moto:", self.color)

    def mostrar_cilindrada(self):
        print("Cilindrada:", self.cilindrada)

    def mostrar_peso(self):
        print("Peso de la moto:", self.peso)


moto1 = Moto("Honda", "CBR600RR", 2024, "Rojo y negro", "600 cc", "194 kg")
print("\n=== MOTO ===")
moto1.mostrar_color()
moto1.mostrar_cilindrada()
moto1.mostrar_peso()
