"""
Archivo integrador generado automaticamente
Directorio: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/riego/sensores
Fecha: 2025-10-21 21:39:45
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/riego/sensores/__init__.py
# ================================================================================

"""Sensores ambientales."""

from python_forestacion.riego.sensores.temperatura_reader_task import (
    TemperaturaReaderTask
)
from python_forestacion.riego.sensores.humedad_reader_task import (
    HumedadReaderTask
)

__all__ = ['TemperaturaReaderTask', 'HumedadReaderTask']


# ================================================================================
# ARCHIVO 2/3: humedad_reader_task.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/riego/sensores/humedad_reader_task.py
# ================================================================================


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


# ================================================================================
# ARCHIVO 3/3: temperatura_reader_task.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/riego/sensores/temperatura_reader_task.py
# ================================================================================

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


