
from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.arbol import Arbol

# Local application
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class ArbolService(CultivoService):
    """
    Servicio especializado para arboles.

    Agrega funcionalidad de crecimiento.
    """

    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        """
        Inicializa el servicio de arboles.

        Args:
            estrategia_absorcion: Estrategia de absorcion
        """
        super().__init__(estrategia_absorcion)

    def mostrar_datos(self, arbol: 'Arbol') -> None:
        """
        Muestra datos del arbol incluyendo altura.

        Args:
            arbol: Arbol a mostrar
        """
        super().mostrar_datos(arbol)
        print(f"ID: {arbol.get_id_cultivo()}")
        print(f"Altura: {arbol.get_altura()} m")


