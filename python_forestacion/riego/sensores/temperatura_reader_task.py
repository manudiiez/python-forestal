"""
Sistema de riego automatizado con sensores y control.
"""

# Standard library
import threading
import time
import random

# Local application
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_TEMPERATURA,
    SENSOR_TEMP_MIN,
    SENSOR_TEMP_MAX
)



class TemperaturaReaderTask(threading.Thread, Observable[float]):
    """
    Sensor de temperatura que ejecuta en thread daemon.

    Lee temperatura cada INTERVALO_SENSOR_TEMPERATURA segundos
    y notifica a observadores.
    """

    def __init__(self):
        """Inicializa el sensor."""
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def run(self) -> None:
        """Ejecuta el loop de lectura de temperatura."""
        while not self._detenido.is_set():
            temperatura = self._leer_temperatura()
            self.notificar_observadores(temperatura)
            time.sleep(INTERVALO_SENSOR_TEMPERATURA)

    def _leer_temperatura(self) -> float:
        """
        Simula lectura de sensor de temperatura.

        Returns:
            Temperatura en Celsius
        """
        return random.uniform(SENSOR_TEMP_MIN, SENSOR_TEMP_MAX)

    def detener(self) -> None:
        """Detiene el sensor de forma controlada."""
        self._detenido.set()
