"""Patron Strategy."""

from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from python_forestacion.patrones.strategy.impl import AbsorcionSeasonalStrategy, AbsorcionConstanteStrategy

__all__ = [
    'AbsorcionAguaStrategy', 'AbsorcionSeasonalStrategy', 'AbsorcionConstanteStrategy'
]
