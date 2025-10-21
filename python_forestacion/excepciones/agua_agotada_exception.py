"""
Excepcion para casos de agua agotada en plantaciones.

Se lanza cuando se intenta regar pero no hay suficiente agua
disponible en la plantacion.
"""

from python_forestacion.excepciones.forestacion_exception import ForestacionException


class AguaAgotadaException(ForestacionException):
    """
    Excepcion lanzada cuando no hay suficiente agua para regar.

    Args:
        agua_requerida: Cantidad de agua requerida
        agua_disponible: Cantidad de agua disponible
    """

    def __init__(self, agua_requerida: int, agua_disponible: int):
        self._agua_requerida = agua_requerida
        self._agua_disponible = agua_disponible

        mensaje_usuario = (
            f"Agua agotada. "
            f"Requerida: {agua_requerida} L, "
            f"Disponible: {agua_disponible} L"
        )

        mensaje_tecnico = (
            f"AguaAgotadaException: "
            f"agua_requerida={agua_requerida}, "
            f"agua_disponible={agua_disponible}"
        )

        super().__init__(mensaje_usuario, mensaje_tecnico)

    def get_agua_requerida(self) -> int:
        """Obtiene el agua requerida."""
        return self._agua_requerida

    def get_agua_disponible(self) -> int:
        """Obtiene el agua disponible."""
        return self._agua_disponibleble