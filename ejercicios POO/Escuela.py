class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.__sueldo = sueldo
    def trabajar(self):
        print("El empleado trabaja")
    def mostrar_sueldo(self):
        print("Sueldo:", self.__sueldo)

class Profesor(Empleado):
    def __init__(self, nombre, sueldo, materia):
        super().__init__(nombre, sueldo)
        self.materia = materia
    def trabajar(self):
        print("El profesor imparte clases")

class Secretario(Empleado):
    def __init__(self, nombre, sueldo, oficina):
        super().__init__(nombre, sueldo)
        self.oficina = oficina
    def trabajar(self):
        print("El secretario organiza documentos")

empleados = [
    Profesor("Pedro", 1500, "Matemáticas"),
    Secretario("Laura", 1000, "Rectorado")
]

for emp in empleados:
    print("Empleado:", emp.nombre)
    emp.trabajar()
    emp.mostrar_sueldo()
    print()