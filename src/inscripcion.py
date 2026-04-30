from src.estudiante import Estudiante
from src.curso import Curso


class Inscripcion:
    """
    Clase que representa la inscripción de un estudiante en un curso.
    Permite registrar calificaciones, calcular promedio y determinar estado académico.
    """

    def __init__(self, estudiante: Estudiante, curso: Curso):
        self._estudiante = estudiante
        self._curso = curso
        self._calificaciones = []

    @property
    def estudiante(self):
        return self._estudiante

    @property
    def curso(self):
        return self._curso

    @property
    def calificaciones(self):
        return self._calificaciones

    def registrar_calificacion(self, nota: float):
        """
        Registra una calificación si está dentro del rango válido chileno: 1.0 a 7.0.
        """
        if 1.0 <= nota <= 7.0:
            self._calificaciones.append(nota)
        else:
            print("La calificación debe estar entre 1.0 y 7.0.")

    def calcular_promedio(self) -> float:
        """
        Calcula el promedio de las calificaciones registradas.
        """
        if not self._calificaciones:
            return 0.0

        return round(sum(self._calificaciones) / len(self._calificaciones), 1)

    def determinar_estado(self) -> str:
        """
        Determina si el estudiante aprueba o reprueba.
        Se considera aprobado con promedio igual o superior a 4.0.
        """
        promedio = self.calcular_promedio()

        if promedio >= 4.0:
            return "Aprobado"
        else:
            return "Reprobado"

    def mostrar_resumen(self) -> str:
        """
        Muestra un resumen académico de la inscripción.
        """
        return (
            f"Estudiante: {self._estudiante.nombre} | "
            f"Curso: {self._curso.codigo} | "
            f"Asignatura: {self._curso.asignatura.nombre} | "
            f"Notas: {self._calificaciones} | "
            f"Promedio: {self.calcular_promedio()} | "
            f"Estado: {self.determinar_estado()}"
        )