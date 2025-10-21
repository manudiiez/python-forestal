"""Sensores ambientales."""

from python_forestacion.riego.sensores.temperatura_reader_task import (
    TemperaturaReaderTask
)
from python_forestacion.riego.sensores.humedad_reader_task import (
    HumedadReaderTask
)

__all__ = ['TemperaturaReaderTask', 'HumedadReaderTask']
