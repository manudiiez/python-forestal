"""
Excepciones especificas del dominio forestal.
"""

# Local application
from python_forestacion.excepciones.forestacion_exception import ForestacionException

class SuperficieInsuficienteException(ForestacionException):
    """
    Excepcion lanzada cuando no hay suficiente superficie para plantar.

    Args:
        superficie_requerida: Superficie total requerida
        superficie_disponible: Superficie actualmente disponible
    """

    def __init__(self, superficie_requerida: float, superficie_disponible: float):
        self._superficie_requerida = superficie_requerida
        self._superficie_disponible = superficie_disponible

        mensaje_usuario = (
            f"No hay suficiente superficie disponible. "
            f"Requerida: {superficie_requerida} m2, "
            f"Disponible: {superficie_disponible} m2"
        )

        mensaje_tecnico = (
            f"SuperficieInsuficienteException: "
            f"superficie_requerida={superficie_requerida}, "
            f"superficie_disponible={superficie_disponible}"
        )

        super().__init__(mensaje_usuario, mensaje_tecnico)

    def get_superficie_requerida(self) -> float:
        """Obtiene la superficie requerida."""
        return self._superficie_requerida

    def get_superficie_disponible(self) -> float:
        """Obtiene la superficie disponible."""
        return self._superficie_disponible

