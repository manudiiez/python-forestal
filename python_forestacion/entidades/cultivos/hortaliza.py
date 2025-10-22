# Local application
from python_forestacion.entidades.cultivos.cultivo import Cultivo

# =============================================================================
# SUBCLASE: HORTALIZA
# =============================================================================

class Hortaliza(Cultivo):
    """
    Clase base para cultivos horticolas.

    Las hortalizas pueden cultivarse en invernadero.

    Atributos adicionales:
        invernadero: Indica si esta en invernadero
    """

    def __init__(self, agua: int, superficie: float, invernadero: bool):
        """
        Inicializa una hortaliza.

        Args:
            agua: Agua inicial en litros
            superficie: Superficie en metros cuadrados
            invernadero: True si esta en invernadero
        """
        super().__init__(agua, superficie)
        self._invernadero = invernadero

    def esta_en_invernadero(self) -> bool:
        """Verifica si esta en invernadero."""
        return self._invernadero

    def set_invernadero(self, invernadero: bool) -> None:
        """Establece si esta en invernadero."""
        self._invernadero = invernadero

