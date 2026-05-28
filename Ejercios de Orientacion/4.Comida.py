class Alimento:
    def __init__(self, nombre, origen, categoria):
        self.nombre = nombre
        self.origen = origen
        self.categoria = categoria

    def describir(self):
        print(f"Alimento: {self.nombre}")


class Comida(Alimento):
    def __init__(self, nombre, origen, categoria, calorias, ingredientes, tiempo_preparacion):
        super().__init__(nombre, origen, categoria)
        self.calorias = calorias
        self.ingredientes = ingredientes
        self.tiempo_preparacion = tiempo_preparacion

    def mostrar_calorias(self):
        print("Calorías:", self.calorias)

    def mostrar_ingredientes(self):
        print("Ingredientes principales:", self.ingredientes)

    def mostrar_tiempo(self):
        print("Tiempo de preparación:", self.tiempo_preparacion)


comida1 = Comida("Lasaña", "Italia", "Pasta", "15 gramos de calorias", "pasta, carne, tomate, bechamel", "45 minutos")
print("\n=== COMIDA ===")
comida1.mostrar_calorias()
comida1.mostrar_ingredientes()
comida1.mostrar_tiempo()

