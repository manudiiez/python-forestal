# Local application
from python_forestacion.patrones.strategy import AbsorcionConstanteStrategy
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

# Standard library
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class LechugaService(CultivoService):
    """Servicio para Lechugas."""

    def __init__(self):
        """Inicializa con estrategia constante."""
        super().__init__(AbsorcionConstanteStrategy(1))

    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """
        Muestra datos de la Lechuga.

        Args:
            cultivo: Lechuga a mostrar
        """
        super().mostrar_datos(cultivo)
        print(f"Variedad: {cultivo.get_variedad()}")
        print(f"Invernadero: {cultivo.esta_en_invernadero()}")
