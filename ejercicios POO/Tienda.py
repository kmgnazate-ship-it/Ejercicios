class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.__sueldo = sueldo
    def trabajar(self):
        print("El empleado trabaja")
    def mostrar_sueldo(self):
        print("Sueldo:", self.__sueldo)

class Vendedor(Empleado):
    def __init__(self, nombre, sueldo, seccion):
        super().__init__(nombre, sueldo)
        self.seccion = seccion
    def trabajar(self):
        print("El vendedor atiende clientes")

class Bodeguero(Empleado):
    def __init__(self, nombre, sueldo, bodega):
        super().__init__(nombre, sueldo)
        self.bodega = bodega
    def trabajar(self):
        print("El bodeguero organiza productos")

empleados = [
    Vendedor("Sofía", 1100, "Electrónica"),
    Bodeguero("Miguel", 950, "Bodega A")
]

for emp in empleados:
    print("Empleado:", emp.nombre)
    emp.trabajar()
    emp.mostrar_sueldo()
    print()