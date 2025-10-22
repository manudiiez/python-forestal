# Local application
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
# Standard library
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo



class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """
    Estrategia de absorcion constante.

    La cantidad de agua absorbida es siempre la misma,
    independientemente de las condiciones ambientales.
    """

    def __init__(self, cantidad_constante: int):
        """
        Inicializa la estrategia con una cantidad fija.

        Args:
            cantidad_constante: Litros de agua a absorber siempre
        """
        self._cantidad_constante = cantidad_constante

    def calcular_absorcion(
            self,
            fecha: date,
            temperatura: float,
            humedad: float,
            cultivo: 'Cultivo'
    ) -> int:
        """
        Retorna cantidad constante.

        Args:
            fecha: No utilizado en esta estrategia
            temperatura: No utilizado en esta estrategia
            humedad: No utilizado en esta estrategia
            cultivo: No utilizado en esta estrategia

        Returns:
            Cantidad constante configurada
        """
        return self._cantidad_constante