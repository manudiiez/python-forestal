# Standard library
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class Plantacion:
    """
    Representa una plantacion agricola.

    Attributes:
        nombre: Nombre de la plantacion
        superficie: Superficie total disponible
        agua_disponible: Agua disponible en litros
        cultivos: Lista de cultivos plantados
        trabajadores: Lista de trabajadores asignados
    """

    def __init__(self, nombre: str, superficie: float, agua: int):
        """
        Inicializa una plantacion.

        Args:
            nombre: Nombre identificatorio
            superficie: Superficie en m2
            agua: Agua inicial en litros

        Raises:
            ValueError: Si agua es negativa
        """
        if agua < 0:
            raise ValueError("El agua no puede ser negativa")

        self._nombre = nombre
        self._superficie = superficie
        self._agua_disponible = agua
        self._cultivos: List['Cultivo'] = []
        self._trabajadores = []

    def get_nombre(self) -> str:
        """Obtiene el nombre."""
        return self._nombre

    def get_superficie(self) -> float:
        """Obtiene la superficie total."""
        return self._superficie

    def get_agua_disponible(self) -> int:
        """Obtiene el agua disponible."""
        return self._agua_disponible

    def set_agua_disponible(self, agua: int) -> None:
        """
        Establece el agua disponible.

        Raises:
            ValueError: Si agua es negativa
        """
        if agua < 0:
            raise ValueError("El agua no puede ser negativa")
        self._agua_disponible = agua

    def get_cultivos(self) -> List['Cultivo']:
        """Obtiene la lista de cultivos (copia defensiva)."""
        return self._cultivos.copy()

    def agregar_cultivo(self, cultivo: 'Cultivo') -> None:
        """Agrega un cultivo a la plantacion."""
        self._cultivos.append(cultivo)

    def eliminar_cultivo(self, cultivo: 'Cultivo') -> None:
        """Elimina un cultivo de la plantacion."""
        if cultivo in self._cultivos:
            self._cultivos.remove(cultivo)

    def get_trabajadores(self):
        """Obtiene la lista de trabajadores (copia defensiva)."""
        return self._trabajadores.copy()

    def set_trabajadores(self, trabajadores) -> None:
        """Establece la lista de trabajadores."""
        self._trabajadores = trabajadores.copy()