# Local application
from python_forestacion.constantes import (
    SUPERFICIE_PINO,
    AGUA_INICIAL_PINO,
    ALTURA_INICIAL_ARBOL,
)
from python_forestacion.entidades.cultivos.arbol import Arbol


class Pino(Arbol):
    """
    Cultivo: Pino.

    Arbol forestal con variedad especifica.
    """

    def __init__(self, variedad: str):
        """
        Inicializa un pino.

        Args:
            variedad: Variedad del pino (Parana, Elliott, etc.)
        """
        super().__init__(
            agua=AGUA_INICIAL_PINO,
            superficie=SUPERFICIE_PINO,
            altura=ALTURA_INICIAL_ARBOL
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        """Obtiene la variedad del pino."""
        return self._variedad

    def set_variedad(self, variedad: str) -> None:
        """Establece la variedad del pino."""
        self._variedad = variedad