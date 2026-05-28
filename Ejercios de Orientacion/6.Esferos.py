class MaterialEs:
    def __init__(self, nombre, marca, precio):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio

    def usar(self):
        print(f"Usando {self.nombre} de marca {self.marca}")


class Esfero(MaterialEs):
    def __init__(self, nombre, marca, precio, color, tipo_punta, material):
        super().__init__(nombre, marca, precio)
        self.color = color
        self.tipo_punta = tipo_punta
        self.material = material

    def mostrar_color(self):
        print("Color del esfero:", self.color)

    def mostrar_punta(self):
        print("Tipo de punta:", self.tipo_punta)

    def mostrar_material(self):
        print("Material:", self.material)


esfero1 = Esfero("Esfero BIC", "BIC", 0.50, "Azul", "Punta fina 0.7mm", "Plástico resistente")
print("\n=== ESFERO ===")
esfero1.mostrar_color()
esfero1.mostrar_punta()
esfero1.mostrar_material()

