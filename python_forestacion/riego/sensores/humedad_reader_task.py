
# Standard library
import threading
import time
import random

# Local application
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_HUMEDAD,
    SENSOR_HUMEDAD_MIN,
    SENSOR_HUMEDAD_MAX,
)


class HumedadReaderTask(threading.Thread, Observable[float]):
    """
    Sensor de humedad que ejecuta en thread daemon.

    Lee humedad cada INTERVALO_SENSOR_HUMEDAD segundos
    y notifica a observadores.
    """

    def __init__(self):
        """Inicializa el sensor."""
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def run(self) -> None:
        """Ejecuta el loop de lectura de humedad."""
        while not self._detenido.is_set():
            humedad = self._leer_humedad()
            self.notificar_observadores(humedad)
            time.sleep(INTERVALO_SENSOR_HUMEDAD)

    def _leer_humedad(self) -> float:
        """
        Simula lectura de sensor de humedad.

        Returns:
            Humedad en porcentaje
        """
        return random.uniform(SENSOR_HUMEDAD_MIN, SENSOR_HUMEDAD_MAX)

    def detener(self) -> None:
        """Detiene el sensor de forma controlada."""
        self._detenido.set()
