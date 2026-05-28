class plantas:
    def __init__(self, nombre, reino, habitat):
        self.nombre = nombre
        self.reino = reino
        self.habitat = habitat

    def crecer(self):
        print(f"La planta {self.nombre} está creciendo")


class Planta(plantas):
    def __init__(self, nombre, reino, habitat, altura, color_flor, tipo_raiz):
        super().__init__(nombre, reino, habitat)
        self.altura = altura
        self.color_flor = color_flor
        self.tipo_raiz = tipo_raiz

    def mostrar_altura(self):
        print("Altura de la planta:", self.altura)

    def mostrar_color_flor(self):
        print("Color de la flor:", self.color_flor)

    def mostrar_raiz(self):
        print("Tipo de raíz:", self.tipo_raiz)


planta1 = Planta("Girasol", "Plantae", "Campos soleados", "hasta 3 metros", "Amarillo brillante", "Raíz pivotante profunda")
print("\n=== PLANTA ===")
planta1.mostrar_altura()
planta1.mostrar_color_flor()
planta1.mostrar_raiz()
