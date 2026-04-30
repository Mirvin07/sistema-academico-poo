from datetime import date
from src.beca import Beca


class Pago:
    """
    Clase que representa un pago de arancel académico.
    Permite calcular el pago final considerando una beca.
    """

    def __init__(self, arancel: float, fecha_pago: date):
        self._arancel = arancel
        self._fecha_pago = fecha_pago
        self._estado = "Pendiente"

    @property
    def arancel(self):
        return self._arancel

    @property
    def fecha_pago(self):
        return self._fecha_pago

    @property
    def estado(self):
        return self._estado

    def calcular_pago_final(self, beca: Beca = None) -> float:
        """
        Calcula el monto final a pagar.
        Si existe beca, aplica el descuento correspondiente.
        """
        if beca:
            descuento = beca.calcular_descuento(self._arancel)
            return self._arancel - descuento

        return self._arancel

    def marcar_pagado(self):
        """
        Cambia el estado del pago a Pagado.
        """
        self._estado = "Pagado"

    def mostrar_info(self, beca: Beca = None) -> str:
        """
        Muestra la información del pago, considerando beca si existe.
        """
        monto_final = self.calcular_pago_final(beca)

        return (
            f"Arancel original: ${self._arancel:,.0f} | "
            f"Fecha de pago: {self._fecha_pago} | "
            f"Estado: {self._estado} | "
            f"Monto final a pagar: ${monto_final:,.0f}"
        )