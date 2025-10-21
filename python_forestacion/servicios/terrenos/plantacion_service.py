
from typing import List, Type

# Local application
from python_forestacion.entidades.terrenos import Plantacion
from python_forestacion.entidades.cultivos import Cultivo
from python_forestacion.excepciones import SuperficieInsuficienteException, AguaAgotadaException
from python_forestacion.patrones.factory import CultivoFactory
from python_forestacion.servicios.cultivos import CultivoServiceRegistry

from python_forestacion.constantes import (
    AGUA_CONSUMIDA_POR_RIEGO,
    AGUA_MINIMA
)


class PlantacionService:
    """Servicio para operaciones sobre plantaciones."""

    def __init__(self):
        """Inicializa el servicio."""
        self._registry = CultivoServiceRegistry.get_instance()

    def plantar(
            self,
            plantacion: Plantacion,
            especie: str,
            cantidad: int
    ) -> None:
        """
        Planta cultivos en una plantacion.

        Args:
            plantacion: Plantacion donde plantar
            especie: Especie a plantar
            cantidad: Cantidad de cultivos

        Raises:
            SuperficieInsuficienteException: Si no hay superficie
        """
        cultivo_muestra = CultivoFactory.crear_cultivo(especie)
        superficie_requerida = cultivo_muestra.get_superficie() * cantidad

        superficie_ocupada = sum(
            c.get_superficie() for c in plantacion.get_cultivos()
        )
        superficie_disponible = plantacion.get_superficie() - superficie_ocupada

        if superficie_requerida > superficie_disponible:
            raise SuperficieInsuficienteException(
                superficie_requerida,
                superficie_disponible
            )

        for i in range(cantidad):
            cultivo = CultivoFactory.crear_cultivo(especie)
            plantacion.agregar_cultivo(cultivo)

    def regar(self, plantacion: Plantacion) -> None:
        """
        Riega todos los cultivos de la plantacion.

        Args:
            plantacion: Plantacion a regar

        Raises:
            AguaAgotadaException: Si no hay agua suficiente
        """
        agua_disponible = plantacion.get_agua_disponible()

        if agua_disponible < AGUA_MINIMA:
            raise AguaAgotadaException(AGUA_MINIMA, agua_disponible)

        plantacion.set_agua_disponible(
            agua_disponible - AGUA_CONSUMIDA_POR_RIEGO
        )

        for cultivo in plantacion.get_cultivos():
            self._registry.absorber_agua(cultivo)

    def fumigar(self, plantacion: Plantacion, plaguicida: str) -> None:
        """
        Fumiga la plantacion.

        Args:
            plantacion: Plantacion a fumigar
            plaguicida: Tipo de plaguicida
        """
        print(f"Fumigando plantacion con: {plaguicida}")

    def cosechar(
            self,
            plantacion: Plantacion,
            tipo_cultivo: Type[Cultivo]
    ) -> List[Cultivo]:
        """
        Cosecha cultivos de un tipo especifico.

        Args:
            plantacion: Plantacion donde cosechar
            tipo_cultivo: Tipo de cultivo a cosechar

        Returns:
            Lista de cultivos cosechados
        """
        cosechados = []
        cultivos = plantacion.get_cultivos()

        for cultivo in cultivos:
            if isinstance(cultivo, tipo_cultivo):
                cosechados.append(cultivo)
                plantacion.eliminar_cultivo(cultivo)

        return cosechados

