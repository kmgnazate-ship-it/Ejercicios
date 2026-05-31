class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.__sueldo = sueldo
    def trabajar(self):
        print("El empleado realiza sus tareas")
    def mostrar_sueldo(self):
        print("Sueldo:", self.__sueldo)

class Medico(Empleado):
    def __init__(self, nombre, sueldo, especialidad):
        super().__init__(nombre, sueldo)
        self.especialidad = especialidad

    def trabajar(self):
        print("El médico atiende pacientes")

class Enfermero(Empleado):
    def __init__(self, nombre, sueldo, turno):
        super().__init__(nombre, sueldo)
        self.turno = turno

    def trabajar(self):
        print("El enfermero administra medicamentos")


empleados = [
    Medico("Carlos", 2000, "Pediatría"),
    Enfermero("María", 1200, "Noche")
]

for emp in empleados:
    print("Empleado:", emp.nombre)
    emp.trabajar()
    emp.mostrar_sueldo()
    print()