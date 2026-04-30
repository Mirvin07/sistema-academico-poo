from src.persona import Persona


class Docente(Persona):
    """
    Clase que representa a un docente del sistema académico.
    Hereda atributos y métodos desde Persona.
    """

    def __init__(self, rut: str, nombre: str, correo: str, especialidad: str):
        super().__init__(rut, nombre, correo)
        self._especialidad = especialidad
        self._cursos_asignados = []

    @property
    def especialidad(self):
        return self._especialidad

    @property
    def cursos_asignados(self):
        return self._cursos_asignados

    def asignar_curso(self, curso):
        """
        Asigna un curso al docente.
        """
        self._cursos_asignados.append(curso)

    def mostrar_info(self) -> str:
        """
        Sobrescribe el método mostrar_info de Persona.
        Esto demuestra polimorfismo.
        """
        return (
            f"Docente: {self._nombre} | "
            f"RUT: {self._rut} | "
            f"Correo: {self._correo} | "
            f"Especialidad: {self._especialidad} | "
            f"Cursos asignados: {len(self._cursos_asignados)}"
        )