"""
Entidades de cultivos del sistema forestal.
"""

# Standard library
from abc import ABC


# =============================================================================
# CLASE BASE: CULTIVO
# =============================================================================

class Cultivo(ABC):
    """
    Clase base abstracta para todos los cultivos.

    Atributos:
        agua: Cantidad de agua almacenada (litros)
        superficie: Superficie ocupada (metros cuadrados)
        id_cultivo: Identificador unico del cultivo
    """

    _contador_id = 0

    def __init__(self, agua: int, superficie: float):
        """
        Inicializa un cultivo.

        Args:
            agua: Agua inicial en litros
            superficie: Superficie en metros cuadrados
        """
        Cultivo._contador_id += 1
        self._id_cultivo = Cultivo._contador_id
        self._agua = agua
        self._superficie = superficie

    def get_id_cultivo(self) -> int:
        """Obtiene el ID del cultivo."""
        return self._id_cultivo

    def get_agua(self) -> int:
        """Obtiene el agua almacenada."""
        return self._agua

    def set_agua(self, agua: int) -> None:
        """Establece el agua almacenada."""
        self._agua = agua

    def get_superficie(self) -> float:
        """Obtiene la superficie ocupada."""
        return self._superficie

    def set_superficie(self, superficie: float) -> None:
        """Establece la superficie ocupada."""
        self._superficie = superficie


