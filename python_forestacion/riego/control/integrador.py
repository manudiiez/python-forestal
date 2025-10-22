"""
Archivo integrador generado automaticamente
Directorio: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/riego/control
Fecha: 2025-10-21 21:39:45
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/riego/control/__init__.py
# ================================================================================

"""Control de riego."""

from python_forestacion.riego.control.control_riego_task import ControlRiegoTask

__all__ = ['ControlRiegoTask']

# ================================================================================
# ARCHIVO 2/2: control_riego_task.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/riego/control/control_riego_task.py
# ================================================================================

"""
Sistema de riego automatizado con sensores y control.
"""

# Standard library
import threading
import time

# Local application
from python_forestacion.patrones.observer.observable import Observer
from python_forestacion.constantes import (

    INTERVALO_CONTROL_RIEGO,
    TEMP_MIN_RIEGO,
    TEMP_MAX_RIEGO,
    HUMEDAD_MAX_RIEGO
)
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.riego.sensores import TemperaturaReaderTask, HumedadReaderTask

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion
    from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService

# =============================================================================
# CONTROL DE RIEGO
# =============================================================================

class ControlRiegoTask(threading.Thread, Observer[float]):
    """
    Controlador de riego automatico.

    Observa sensores de temperatura y humedad, y riega
    cuando se cumplen las condiciones.
    """

    def __init__(
            self,
            sensor_temperatura: TemperaturaReaderTask,
            sensor_humedad: HumedadReaderTask,
            plantacion: 'Plantacion',
            plantacion_service: 'PlantacionService'
    ):
        """
        Inicializa el controlador.

        Args:
            sensor_temperatura: Sensor de temperatura
            sensor_humedad: Sensor de humedad
            plantacion: Plantacion a regar
            plantacion_service: Servicio de plantacion
        """
        threading.Thread.__init__(self, daemon=True)
        self._sensor_temperatura = sensor_temperatura
        self._sensor_humedad = sensor_humedad
        self._plantacion = plantacion
        self._plantacion_service = plantacion_service

        self._ultima_temperatura = 20.0
        self._ultima_humedad = 50.0

        self._detenido = threading.Event()

        sensor_temperatura.agregar_observador(self)
        sensor_humedad.agregar_observador(self)

    def actualizar(self, evento: float) -> None:
        """
        Recibe notificaciones de sensores.

        Args:
            evento: Valor del sensor (temperatura o humedad)
        """
        pass

    def run(self) -> None:
        """Ejecuta el loop de control de riego."""
        while not self._detenido.is_set():
            temperatura = self._sensor_temperatura._leer_temperatura()
            humedad = self._sensor_humedad._leer_humedad()

            self._ultima_temperatura = temperatura
            self._ultima_humedad = humedad

            if self._debe_regar(temperatura, humedad):
                try:
                    self._plantacion_service.regar(self._plantacion)
                    print(f"[RIEGO] T={temperatura:.1f}C H={humedad:.1f}% - Regando...")
                except AguaAgotadaException:
                    print("[RIEGO] Agua agotada - No se puede regar")

            time.sleep(INTERVALO_CONTROL_RIEGO)

    def _debe_regar(self, temperatura: float, humedad: float) -> bool:
        """
        Determina si se debe regar segun condiciones.

        Args:
            temperatura: Temperatura actual
            humedad: Humedad actual

        Returns:
            True si se debe regar
        """
        return (
                TEMP_MIN_RIEGO <= temperatura <= TEMP_MAX_RIEGO and
                humedad < HUMEDAD_MAX_RIEGO
        )

    def detener(self) -> None:
        """Detiene el controlador de forma controlada."""
        self._detenido.set()

