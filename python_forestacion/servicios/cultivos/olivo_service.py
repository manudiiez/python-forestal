from python_forestacion.constantes import CRECIMIENTO_OLIVO
from python_forestacion.patrones.strategy import AbsorcionSeasonalStrategy
from datetime import date

from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos import ArbolService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class OlivoService(ArbolService):
    """Servicio para Olivos."""

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
        Olivo absorbe agua y crece.

        Args:
            cultivo: Olivo que absorbe
            fecha: Fecha actual
            temperatura: Temperatura
            humedad: Humedad

        Returns:
            Agua absorbida
        """
        agua = super().absorver_agua(cultivo, fecha, temperatura, humedad)
        cultivo.set_altura(cultivo.get_altura() + CRECIMIENTO_OLIVO)
        return agua

    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """
        Muestra datos del Olivo.

        Args:
            cultivo: Olivo a mostrar
        """
        super().mostrar_datos(cultivo)
        print(f"Tipo de aceituna: {cultivo.get_tipo_aceituna().value}")
