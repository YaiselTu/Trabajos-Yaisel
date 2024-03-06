class Estudiante:
    def __init__(self, nombre, calificaciones, asistencia):
        self.nombre = nombre
        self.calificaciones = calificaciones
        self.asistencia = asistencia

    def promedio_calificaciones(self):
        return sum(self.calificaciones) / len(self.calificaciones)

    def evaluar_estudiante(self):
        promedio = self.promedio_calificaciones()
        if promedio >= 70 and self.asistencia >= 80:
            return "Aprobado"
        else:
            if promedio < 70:
                sugerencia = "Mejorar las calificaciones"
            else:
                sugerencia = "Mejorar la asistencia"
            return f"Reprobado. {sugerencia}"

# Ejemplo de uso
estudiante1 = Estudiante("Juan", [80, 75, 90, 85], 85)
print(f"{estudiante1.nombre}: {estudiante1.evaluar_estudiante()}")

estudiante2 = Estudiante("María", [60, 65, 70, 55], 75)
print(f"{estudiante2.nombre}: {estudiante2.evaluar_estudiante()}")
