class Persona:
    """
    Clase base que representa a una persona dentro del sistema académico.
    Contiene atributos comunes para estudiantes y docentes.
    """

    def __init__(self, rut: str, nombre: str, correo: str):
        self._rut = rut
        self._nombre = nombre
        self._correo = correo

    @property
    def rut(self):
        return self._rut

    @property
    def nombre(self):
        return self._nombre

    @property
    def correo(self):
        return self._correo

    def mostrar_info(self) -> str:
        """
        Método polimórfico que será sobrescrito por las clases hijas.
        """
        return f"RUT: {self._rut} | Nombre: {self._nombre} | Correo: {self._correo}"