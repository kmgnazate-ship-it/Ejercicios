class Movil:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def encender(self):
        print(f"Encendiendo {self.marca} {self.modelo}")


class Telefono(Movil):
    def __init__(self, marca, modelo, precio, color, almacenamiento, bateria):
        super().__init__(marca, modelo, precio)
        self.color = color
        self.almacenamiento = almacenamiento
        self.bateria = bateria

    def mostrar_color(self):
        print("Color del teléfono:", self.color)

    def mostrar_almacenamiento(self):
        print("Almacenamiento:", self.almacenamiento)

    def mostrar_bateria(self):
        print("Batería:", self.bateria)


telefono1 = Telefono("Samsung", "Galaxy S24", 899, "Negro", "256 GB", "5000 mAh")
print("\n=== TELÉFONO ===")
telefono1.mostrar_color()
telefono1.mostrar_almacenamiento()
telefono1.mostrar_bateria()