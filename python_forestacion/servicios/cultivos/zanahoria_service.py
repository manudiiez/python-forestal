from python_forestacion.patrones.strategy import AbsorcionConstanteStrategy
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class ZanahoriaService(CultivoService):
    """Servicio para Zanahorias."""

    def __init__(self):
        """Inicializa con estrategia constante."""
        super().__init__(AbsorcionConstanteStrategy(2))

    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """
        Muestra datos de la Zanahoria.

        Args:
            cultivo: Zanahoria a mostrar
        """
        super().mostrar_datos(cultivo)
        print(f"Es baby carrot: {cultivo.is_baby_carrot()}")