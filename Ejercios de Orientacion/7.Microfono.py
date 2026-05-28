class EquipoAudio:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def activar(self):
        print(f"Micrófono {self.marca} {self.modelo} activado")


class Microfono(EquipoAudio):
    def __init__(self, marca, modelo, precio, tipo, frecuencia, conexion):
        super().__init__(marca, modelo, precio)
        self.tipo = tipo
        self.frecuencia = frecuencia
        self.conexion = conexion

    def mostrar_tipo(self):
        print("Tipo de micrófono:", self.tipo)

    def mostrar_frecuencia(self):
        print("Rango de frecuencia:", self.frecuencia)

    def mostrar_conexion(self):
        print("Tipo de conexión:", self.conexion)


microfono1 = Microfono("Shure", "SM7B", 399, "Samsung", "50 Hz - 20 kHz", "XLR")
print("\n=== MICRÓFONO ===")
microfono1.mostrar_tipo()
microfono1.mostrar_frecuencia()
microfono1.mostrar_conexion()
