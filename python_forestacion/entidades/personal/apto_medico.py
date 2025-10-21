from datetime import date

class AptoMedico:
    """
    Certificacion medica de un trabajador.

    Attributes:
        apto: Estado de aptitud
        fecha_emision: Fecha de emision del apto
        observaciones: Observaciones medicas
    """

    def __init__(self, apto: bool, fecha_emision: date, observaciones: str):
        """
        Inicializa un apto medico.

        Args:
            apto: True si esta apto
            fecha_emision: Fecha de emision
            observaciones: Observaciones medicas
        """
        self._apto = apto
        self._fecha_emision = fecha_emision
        self._observaciones = observaciones

    def esta_apto(self) -> bool:
        """Verifica si esta apto."""
        return self._apto

    def get_fecha_emision(self) -> date:
        """Obtiene la fecha de emision."""
        return self._fecha_emision

    def get_observaciones(self) -> str:
        """Obtiene las observaciones."""
        return self._observaciones
