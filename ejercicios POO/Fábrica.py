class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.__sueldo = sueldo
    def trabajar(self):
        print("El empleado trabaja")
    def mostrar_sueldo(self):
        print("Sueldo:", self.__sueldo)

class Operario(Empleado):
    def __init__(self, nombre, sueldo, maquina):
        super().__init__(nombre, sueldo)
        self.maquina = maquina
    def trabajar(self):
        print("El operario maneja maquinaria")

class Supervisor(Empleado):
    def __init__(self, nombre, sueldo, area):
        super().__init__(nombre, sueldo)
        self.area = area
    def trabajar(self):
        print("El supervisor controla la producción")


empleados = [
    Operario("Juan", 1000, "Torno"),
    Supervisor("Marta", 1800, "Producción")
]

for emp in empleados:
    print("Empleado:", emp.nombre)
    emp.trabajar()
    emp.mostrar_sueldo()
    print()