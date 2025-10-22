"""
Archivo integrador generado automaticamente
Directorio: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/strategy/impl
Fecha: 2025-10-21 21:39:45
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/strategy/impl/__init__.py
# ================================================================================

from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy

__all__ = ["AbsorcionConstanteStrategy", "AbsorcionSeasonalStrategy"]

# ================================================================================
# ARCHIVO 2/3: absorcion_constante_strategy.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/strategy/impl/absorcion_constante_strategy.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/3: absorcion_seasonal_strategy.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/strategy/impl/absorcion_seasonal_strategy.py
# ================================================================================


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


