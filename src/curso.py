from src.asignatura import Asignatura
from src.docente import Docente
from src.estudiante import Estudiante


class Curso:
    """
    Clase que representa una sección o curso académico.
    Relaciona una asignatura, un docente y estudiantes inscritos.
    """

    def __init__(self, codigo: str, asignatura: Asignatura, horario: str, cupo: int):
        self._codigo = codigo
        self._asignatura = asignatura
        self._docente = None
        self._horario = horario
        self._cupo = cupo
        self._estudiantes = []

    @property
    def codigo(self):
        return self._codigo

    @property
    def asignatura(self):
        return self._asignatura

    @property
    def docente(self):
        return self._docente

    @property
    def horario(self):
        return self._horario

    @property
    def cupo(self):
        return self._cupo

    @property
    def estudiantes(self):
        return self._estudiantes

    def asignar_docente(self, docente: Docente):
        """
        Asigna un docente al curso y actualiza el listado de cursos del docente.
        """
        self._docente = docente
        docente.asignar_curso(self)

    def inscribir_estudiante(self, estudiante: Estudiante) -> bool:
        """
        Inscribe un estudiante en el curso si existe cupo disponible.
        Retorna True si la inscripción fue exitosa y False si no hay cupo.
        """
        if len(self._estudiantes) < self._cupo:
            self._estudiantes.append(estudiante)
            return True

        return False

    def listar_estudiantes(self):
        """
        Muestra el listado de estudiantes inscritos en el curso.
        """
        if not self._estudiantes:
            print("No hay estudiantes inscritos en este curso.")
            return

        print(f"Estudiantes inscritos en {self._codigo}:")
        for estudiante in self._estudiantes:
            print(f"- {estudiante.nombre} ({estudiante.rut})")

    def mostrar_info(self) -> str:
        """
        Muestra la información general del curso.
        """
        docente_nombre = self._docente.nombre if self._docente else "Sin docente asignado"

        return (
            f"Curso: {self._codigo} | "
            f"Asignatura: {self._asignatura.nombre} | "
            f"Docente: {docente_nombre} | "
            f"Horario: {self._horario} | "
            f"Cupo: {len(self._estudiantes)}/{self._cupo}"
        )
