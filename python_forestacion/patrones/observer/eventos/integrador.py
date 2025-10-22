"""
Archivo integrador generado automaticamente
Directorio: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/observer/eventos
Fecha: 2025-10-22 10:13:59
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/observer/eventos/__init__.py
# ================================================================================

from python_forestacion.patrones.observer.eventos.evento_plantacion import (
    EventoPlantacion,
    TipoEventoPlantacion
)

# ================================================================================
# ARCHIVO 2/3: evento_plantacion.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/observer/eventos/evento_plantacion.py
# ================================================================================



from datetime import datetime
from enum import Enum
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class TipoEventoPlantacion(Enum):
    """
    Tipos de eventos que pueden ocurrir en una plantacion.

    Attributes:
        RIEGO: Evento de riego de cultivos
        COSECHA: Evento de cosecha de cultivos
        PLANTACION: Evento de plantacion de nuevos cultivos
        FUMIGACION: Evento de aplicacion de plaguicida
        ABSORCION: Evento de absorcion de agua por cultivos
    """
    RIEGO = "riego"
    COSECHA = "cosecha"
    PLANTACION = "plantacion"
    FUMIGACION = "fumigacion"
    ABSORCION = "absorcion"


class EventoPlantacion:
    """
    Evento generado por una operacion en una plantacion.

    Encapsula informacion sobre operaciones realizadas en plantaciones
    para notificar a observadores interesados.

    Attributes:
        _tipo_evento: Tipo de operacion realizada
        _plantacion: Plantacion donde ocurrio el evento
        _descripcion: Descripcion detallada del evento
        _timestamp: Momento en que ocurrio el evento
        _datos_adicionales: Diccionario con datos extra (opcional)
    """

    def __init__(
            self,
            tipo_evento: TipoEventoPlantacion,
            plantacion: 'Plantacion',
            descripcion: str,
            timestamp: Optional[datetime] = None,
            datos_adicionales: Optional[dict] = None
    ):
        """
        Inicializa un evento de plantacion.

        Args:
            tipo_evento: Tipo de operacion realizada
            plantacion: Plantacion donde ocurrio el evento
            descripcion: Descripcion del evento
            timestamp: Momento del evento (None usa datetime.now())
            datos_adicionales: Informacion adicional del evento (opcional)
        """
        self._tipo_evento = tipo_evento
        self._plantacion = plantacion
        self._descripcion = descripcion
        self._timestamp = timestamp if timestamp else datetime.now()
        self._datos_adicionales = datos_adicionales if datos_adicionales else {}

    def get_tipo_evento(self) -> TipoEventoPlantacion:
        """
        Obtiene el tipo de evento.

        Returns:
            Tipo de operacion realizada
        """
        return self._tipo_evento

    def get_plantacion(self) -> 'Plantacion':
        """
        Obtiene la plantacion donde ocurrio el evento.

        Returns:
            Plantacion involucrada
        """
        return self._plantacion

    def get_descripcion(self) -> str:
        """
        Obtiene la descripcion del evento.

        Returns:
            Descripcion detallada
        """
        return self._descripcion

    def get_timestamp(self) -> datetime:
        """
        Obtiene el momento en que ocurrio el evento.

        Returns:
            Timestamp del evento
        """
        return self._timestamp

    def get_datos_adicionales(self) -> dict:
        """
        Obtiene datos adicionales del evento.

        Returns:
            Diccionario con informacion extra
        """
        return self._datos_adicionales.copy()

    def get_dato_adicional(self, clave: str, default=None):
        """
        Obtiene un dato adicional especifico.

        Args:
            clave: Clave del dato a buscar
            default: Valor por defecto si no existe

        Returns:
            Valor del dato o default
        """
        return self._datos_adicionales.get(clave, default)

    def agregar_dato_adicional(self, clave: str, valor) -> None:
        """
        Agrega un dato adicional al evento.

        Args:
            clave: Clave del dato
            valor: Valor a almacenar
        """
        self._datos_adicionales[clave] = valor

    def __str__(self) -> str:
        """
        Representacion en texto del evento.

        Returns:
            String formateado con informacion del evento
        """
        return (
            f"EventoPlantacion("
            f"tipo={self._tipo_evento.value}, "
            f"plantacion={self._plantacion.get_nombre()}, "
            f"descripcion='{self._descripcion}', "
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

# ================================================================================
# ARCHIVO 3/3: evento_sensor.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/observer/eventos/evento_sensor.py
# ================================================================================


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

