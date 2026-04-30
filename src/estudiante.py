from src.persona import Persona


class Estudiante(Persona):
    """
    Clase que representa a un estudiante del sistema académico.
    Hereda atributos y métodos desde Persona.
    """

    def __init__(self, rut: str, nombre: str, correo: str, carrera: str):
        super().__init__(rut, nombre, correo)
        self._carrera = carrera
        self._beca = None
        self._pagos = []

    @property
    def carrera(self):
        return self._carrera

    @property
    def beca(self):
        return self._beca

    @property
    def pagos(self):
        return self._pagos

    def asignar_beca(self, beca):
        """
        Asigna una beca al estudiante.
        """
        self._beca = beca

    def agregar_pago(self, pago):
        """
        Agrega un pago al historial del estudiante.
        """
        self._pagos.append(pago)

    def mostrar_info(self) -> str:
        """
        Sobrescribe el método mostrar_info de Persona.
        Esto demuestra polimorfismo.
        """
        beca_nombre = self._beca.nombre if self._beca else "Sin beca"

        return (
            f"Estudiante: {self._nombre} | "
            f"RUT: {self._rut} | "
            f"Correo: {self._correo} | "
            f"Carrera: {self._carrera} | "
            f"Beca: {beca_nombre}"
        )