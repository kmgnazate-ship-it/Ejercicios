class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.__sueldo = sueldo
    def trabajar(self):
        print("El empleado trabaja")
    def mostrar_sueldo(self):
        print("Sueldo:", self.__sueldo)

class Docente(Empleado):
    def __init__(self, nombre, sueldo, carrera):
        super().__init__(nombre, sueldo)
        self.carrera = carrera
    def trabajar(self):
        print("El docente dicta clases")

class Coordinador(Empleado):
    def __init__(self, nombre, sueldo, facultad):
        super().__init__(nombre, sueldo)
        self.facultad = facultad
    def trabajar(self):
        print("El coordinador organiza actividades académicas")

empleados = [
    Docente("Andrea", 1700, "Software"),
    Coordinador("Ricardo", 2200, "Ingeniería")
]

for emp in empleados:
    print("Empleado:", emp.nombre)
    emp.trabajar()
    emp.mostrar_sueldo()
    print()