class Mundo:
    def __init__(self, nombre, tipo, distancia_sol):
        self.nombre = nombre
        self.tipo = tipo
        self.distancia_sol = distancia_sol

    def describir(self):
        print(f"Cuerpo celeste: {self.nombre}")


class Planeta(Mundo):
    def __init__(self, nombre, tipo, distancia_sol, diametro, masa, periodo_orbital):
        super().__init__(nombre, tipo, distancia_sol)
        self.diametro = diametro
        self.masa = masa
        self.periodo_orbital = periodo_orbital

    def mostrar_diametro(self):
        print("Diámetro del planeta:", self.diametro)

    def mostrar_masa(self):
        print("Masa del planeta:", self.masa)

    def mostrar_periodo(self):
        print("Período orbital:", self.periodo_orbital)


planeta1 = Planeta("Saturno", "Planeta gaseoso", "1.430 millones km", "116.460 km", "5.68 × 10²⁶ kg", "29.5 años terrestres")
print("\n=== PLANETA ===")
planeta1.mostrar_diametro()
planeta1.mostrar_masa()
planeta1.mostrar_periodo()

