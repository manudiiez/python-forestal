
from datetime import datetime
from typing import Optional


class EventoSensor:
    """
    Evento generado por un sensor ambiental.

    Encapsula la informacion de una lectura de sensor con timestamp
    y metadata adicional.

    Attributes:
        _valor: Valor leido por el sensor
        _timestamp: Momento de la lectura
        _tipo_sensor: Tipo de sensor que genero el evento
        _unidad: Unidad de medida del valor
    """

    def __init__(
            self,
            valor: float,
            tipo_sensor: str,
            unidad: str,
            timestamp: Optional[datetime] = None
    ):
        """
        Inicializa un evento de sensor.

        Args:
            valor: Valor leido por el sensor
            tipo_sensor: Tipo de sensor (temperatura, humedad, etc.)
            unidad: Unidad de medida (C, %, etc.)
            timestamp: Momento de la lectura (None usa datetime.now())
        """
        self._valor = valor
        self._tipo_sensor = tipo_sensor
        self._unidad = unidad
        self._timestamp = timestamp if timestamp else datetime.now()

    def get_valor(self) -> float:
        """
        Obtiene el valor leido por el sensor.

        Returns:
            Valor de la lectura
        """
        return self._valor

    def get_tipo_sensor(self) -> str:
        """
        Obtiene el tipo de sensor que genero el evento.

        Returns:
            Tipo de sensor (temperatura, humedad, etc.)
        """
        return self._tipo_sensor

    def get_unidad(self) -> str:
        """
        Obtiene la unidad de medida del valor.

        Returns:
            Unidad de medida (C, %, etc.)
        """
        return self._unidad

    def get_timestamp(self) -> datetime:
        """
        Obtiene el momento en que se genero la lectura.

        Returns:
            Timestamp de la lectura
        """
        return self._timestamp

    def __str__(self) -> str:
        """
        Representacion en texto del evento.

        Returns:
            String formateado con informacion del evento
        """
        return (
            f"EventoSensor("
            f"tipo={self._tipo_sensor}, "
            f"valor={self._valor}{self._unidad}, "
            f"timestamp={self._timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
            f")"
        )

    def __repr__(self) -> str:
        """
        Representacion tecnica del evento.

        Returns:
            String para debugging
        """
        return self.__str__()