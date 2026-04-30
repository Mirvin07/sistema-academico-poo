class Beca:
    """
    Clase que representa una beca o beneficio estudiantil.
    Permite calcular descuentos sobre un monto determinado.
    """

    def __init__(self, nombre: str, porcentaje_descuento: float):
        self._nombre = nombre
        self._porcentaje_descuento = porcentaje_descuento

    @property
    def nombre(self):
        return self._nombre

    @property
    def porcentaje_descuento(self):
        return self._porcentaje_descuento

    def calcular_descuento(self, monto: float) -> float:
        """
        Calcula el monto de descuento según el porcentaje de la beca.
        """
        return round(monto * (self._porcentaje_descuento / 100), 0)

    def mostrar_info(self) -> str:
        """
        Muestra la información general de la beca.
        """
        return (
            f"Beca: {self._nombre} | "
            f"Descuento: {self._porcentaje_descuento}%"
        )