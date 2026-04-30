class Asignatura:
    """
    Clase que representa una asignatura dentro del sistema académico.
    """

    def __init__(self, codigo: str, nombre: str, creditos: int):
        self._codigo = codigo
        self._nombre = nombre
        self._creditos = creditos

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def creditos(self):
        return self._creditos

    def mostrar_info(self) -> str:
        """
        Muestra la información general de la asignatura.
        """
        return (
            f"Asignatura: {self._nombre} | "
            f"Código: {self._codigo} | "
            f"Créditos: {self._creditos}"
        )
