from python_forestacion.constantes import AGUA_INICIAL_LECHUGA, SUPERFICIE_LECHUGA
from python_forestacion.entidades.cultivos.hortaliza import Hortaliza


class Lechuga(Hortaliza):
    """
    Cultivo: Lechuga.

    Hortaliza de hoja verde cultivada en invernadero.
    """

    def __init__(self, variedad: str):
        """
        Inicializa una lechuga.

        Args:
            variedad: Variedad de lechuga (Crespa, Mantecosa, etc.)
        """
        super().__init__(
            agua=AGUA_INICIAL_LECHUGA,
            superficie=SUPERFICIE_LECHUGA,
            invernadero=True
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        """Obtiene la variedad de lechuga."""
        return self._variedad

    def set_variedad(self, variedad: str) -> None:
        """Establece la variedad de lechuga."""
        self._variedad = variedad
