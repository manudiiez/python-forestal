
from datetime import date


from python_forestacion.constantes import CRECIMIENTO_PINO
from python_forestacion.patrones.strategy import AbsorcionSeasonalStrategy
from python_forestacion.servicios.cultivos.arbol_service import ArbolService


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class PinoService(ArbolService):
    """Servicio para Pinos."""

    def __init__(self):
        """Inicializa con estrategia estacional."""
        super().__init__(AbsorcionSeasonalStrategy())

    def absorver_agua(
            self,
            cultivo: 'Cultivo',
            fecha: date = None,
            temperatura: float = 20.0,
            humedad: float = 50.0
    ) -> int:
        """
        Pino absorbe agua y crece.

        Args:
            cultivo: Pino que absorbe
            fecha: Fecha actual
            temperatura: Temperatura
            humedad: Humedad

        Returns:
            Agua absorbida
        """
        agua = super().absorver_agua(cultivo, fecha, temperatura, humedad)
        cultivo.set_altura(cultivo.get_altura() + CRECIMIENTO_PINO)
        return agua

    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """
        Muestra datos del Pino.

        Args:
            cultivo: Pino a mostrar
        """
        super().mostrar_datos(cultivo)
        print(f"Variedad: {cultivo.get_variedad()}")