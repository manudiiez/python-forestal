"""
Archivo integrador generado automaticamente
Directorio: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/strategy
Fecha: 2025-10-21 21:39:45
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/strategy/__init__.py
# ================================================================================

"""Patron Strategy."""

from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from python_forestacion.patrones.strategy.impl import AbsorcionSeasonalStrategy, AbsorcionConstanteStrategy

__all__ = [
    'AbsorcionAguaStrategy', 'AbsorcionSeasonalStrategy', 'AbsorcionConstanteStrategy'
]


# ================================================================================
# ARCHIVO 2/2: absorcion_agua_strategy.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/strategy/absorcion_agua_strategy.py
# ================================================================================



# Standard library
from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionAguaStrategy(ABC):
    """
    Interfaz Strategy para algoritmos de absorcion de agua.

    Define el contrato que deben cumplir todas las estrategias
    de absorcion de agua.
    """

    @abstractmethod
    def calcular_absorcion(
            self,
            fecha: date,
            temperatura: float,
            humedad: float,
            cultivo: 'Cultivo'
    ) -> int:
        """
        Calcula la cantidad de agua que absorbe un cultivo.

        Args:
            fecha: Fecha actual
            temperatura: Temperatura ambiente
            humedad: Humedad ambiente
            cultivo: Cultivo que absorbe agua

        Returns:
            Cantidad de agua absorbida en litros
        """
        pass




