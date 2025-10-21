from abc import ABC
from datetime import date
from python_forestacion.patrones.strategy import AbsorcionAguaStrategy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class CultivoService(ABC):
    """
    Servicio base para operaciones sobre cultivos.

    Utiliza Strategy Pattern para absorcion de agua.
    """

    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        """
        Inicializa el servicio con una estrategia de absorcion.

        Args:
            estrategia_absorcion: Estrategia de absorcion a usar
        """
        self._estrategia_absorcion = estrategia_absorcion

    def absorver_agua(
            self,
            cultivo: 'Cultivo',
            fecha: date = None,
            temperatura: float = 20.0,
            humedad: float = 50.0
    ) -> int:
        """
        Hace que el cultivo absorba agua segun su estrategia.

        Args:
            cultivo: Cultivo que absorbe agua
            fecha: Fecha actual (default: hoy)
            temperatura: Temperatura ambiente
            humedad: Humedad ambiente

        Returns:
            Cantidad de agua absorbida en litros
        """
        if fecha is None:
            fecha = date.today()

        agua_absorvida = self._estrategia_absorcion.calcular_absorcion(
            fecha, temperatura, humedad, cultivo
        )

        cultivo.set_agua(cultivo.get_agua() + agua_absorvida)
        return agua_absorvida

    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """
        Muestra datos basicos del cultivo.

        Args:
            cultivo: Cultivo a mostrar
        """
        print(f"Cultivo: {type(cultivo).__name__}")
        print(f"Superficie: {cultivo.get_superficie()} m2")
        print(f"Agua almacenada: {cultivo.get_agua()} L")

