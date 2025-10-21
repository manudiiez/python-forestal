
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
# Local application
from python_forestacion.constantes import (
    ABSORCION_SEASONAL_VERANO,
    ABSORCION_SEASONAL_INVIERNO,
    MES_INICIO_VERANO,
    MES_FIN_VERANO
)
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """
    Estrategia de absorcion estacional.

    La cantidad de agua absorbida depende de la temporada del ano:
    - Verano: Mayor absorcion
    - Invierno: Menor absorcion
    """

    def calcular_absorcion(
            self,
            fecha: date,
            temperatura: float,
            humedad: float,
            cultivo: 'Cultivo'
    ) -> int:
        """
        Calcula absorcion segun temporada.

        Args:
            fecha: Fecha actual (usado para determinar temporada)
            temperatura: No utilizado en esta estrategia
            humedad: No utilizado en esta estrategia
            cultivo: No utilizado en esta estrategia

        Returns:
            Absorcion en litros (5L verano, 2L invierno)
        """
        mes = fecha.month
        if MES_INICIO_VERANO <= mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO
        else:
            return ABSORCION_SEASONAL_INVIERNO
