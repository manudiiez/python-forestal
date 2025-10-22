"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion
Fecha de generacion: 2025-10-21 21:39:45
Total de archivos integrados: 66
Total de directorios procesados: 21
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. __init__.py
#   2. constantes.py
#
# DIRECTORIO: entidades
#   3. __init__.py
#
# DIRECTORIO: entidades/cultivos
#   4. __init__.py
#   5. arbol.py
#   6. cultivo.py
#   7. hortaliza.py
#   8. lechuga.py
#   9. olivo.py
#   10. pino.py
#   11. tipo_aceituna.py
#   12. zanahoria.py
#
# DIRECTORIO: entidades/personal
#   13. __init__.py
#   14. apto_medico.py
#   15. herramienta.py
#   16. tarea.py
#   17. trabajador.py
#
# DIRECTORIO: entidades/terrenos
#   18. __init__.py
#   19. plantacion.py
#   20. registro_forestal.py
#   21. tierra.py
#
# DIRECTORIO: excepciones
#   22. __init__.py
#   23. agua_agotada_exception.py
#   24. forestacion_exception.py
#   25. mensajes_exception.py
#   26. persistencia_exception.py
#   27. superficie_insuficiente_exception.py
#
# DIRECTORIO: patrones
#   28. __init__.py
#
# DIRECTORIO: patrones/factory
#   29. __init__.py
#   30. cultivo_factory.py
#
# DIRECTORIO: patrones/observer
#   31. __init__.py
#   32. observable.py
#   33. observer.py
#
# DIRECTORIO: patrones/observer/eventos
#   34. __init__.py
#   35. evento_plantacion.py
#   36. evento_sensor.py
#
# DIRECTORIO: patrones/singleton
#   37. __init__.py
#
# DIRECTORIO: patrones/strategy
#   38. __init__.py
#   39. absorcion_agua_strategy.py
#
# DIRECTORIO: patrones/strategy/impl
#   40. __init__.py
#   41. absorcion_constante_strategy.py
#   42. absorcion_seasonal_strategy.py
#
# DIRECTORIO: riego
#   43. __init__.py
#
# DIRECTORIO: riego/control
#   44. __init__.py
#   45. control_riego_task.py
#
# DIRECTORIO: riego/sensores
#   46. __init__.py
#   47. humedad_reader_task.py
#   48. temperatura_reader_task.py
#
# DIRECTORIO: servicios
#   49. __init__.py
#
# DIRECTORIO: servicios/cultivos
#   50. __init__.py
#   51. arbol_service.py
#   52. cultivo_service.py
#   53. cultivo_service_registry.py
#   54. lechuga_service.py
#   55. olivo_service.py
#   56. pino_service.py
#   57. zanahoria_service.py
#
# DIRECTORIO: servicios/negocio
#   58. __init__.py
#   59. fincas_service.py
#   60. paquete.py
#
# DIRECTORIO: servicios/personal
#   61. __init__.py
#   62. trabajador_service.py
#
# DIRECTORIO: servicios/terrenos
#   63. __init__.py
#   64. plantacion_service.py
#   65. registro_forestal_service.py
#   66. tierra_service.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/66: __init__.py
# Directorio: .
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/__init__.py
# ==============================================================================

# =============================================================================
# python_forestacion/__init__.py
# =============================================================================
"""
Sistema de Gestion Forestal.

Sistema integral que implementa multiples patrones de diseno
para la gestion de fincas forestales y agricolas.
"""

__version__ = "1.0.0"
__author__ = "Sistema Forestal"

# ==============================================================================
# ARCHIVO 2/66: constantes.py
# Directorio: .
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/constantes.py
# ==============================================================================

"""
Constantes centralizadas del sistema PythonForestal.

Este modulo contiene todas las constantes utilizadas en el sistema,
evitando valores magicos hardcodeados en el codigo.
"""

# Standard library
from enum import Enum

# =============================================================================
# CONSTANTES DE AGUA
# =============================================================================

AGUA_MINIMA = 10
"""int: Cantidad minima de agua para riego (litros)"""

AGUA_INICIAL_PLANTACION = 500
"""int: Agua inicial de una plantacion (litros)"""

AGUA_CONSUMIDA_POR_RIEGO = 10
"""int: Agua consumida en cada ciclo de riego (litros)"""

# =============================================================================
# CONSTANTES DE RIEGO AUTOMATIZADO
# =============================================================================

TEMP_MIN_RIEGO = 8
"""int: Temperatura minima para activar riego (Celsius)"""

TEMP_MAX_RIEGO = 15
"""int: Temperatura maxima para activar riego (Celsius)"""

HUMEDAD_MAX_RIEGO = 50
"""int: Humedad maxima para activar riego (porcentaje)"""

INTERVALO_CONTROL_RIEGO = 2.5
"""float: Intervalo de evaluacion del control de riego (segundos)"""

# =============================================================================
# CONSTANTES DE SENSORES
# =============================================================================

INTERVALO_SENSOR_TEMPERATURA = 2.0
"""float: Intervalo de lectura del sensor de temperatura (segundos)"""

INTERVALO_SENSOR_HUMEDAD = 3.0
"""float: Intervalo de lectura del sensor de humedad (segundos)"""

SENSOR_TEMP_MIN = -25
"""int: Temperatura minima del sensor (Celsius)"""

SENSOR_TEMP_MAX = 50
"""int: Temperatura maxima del sensor (Celsius)"""

SENSOR_HUMEDAD_MIN = 0
"""int: Humedad minima del sensor (porcentaje)"""

SENSOR_HUMEDAD_MAX = 100
"""int: Humedad maxima del sensor (porcentaje)"""

# =============================================================================
# CONSTANTES DE THREADING
# =============================================================================

THREAD_JOIN_TIMEOUT = 2.0
"""float: Timeout para esperar finalizacion de threads (segundos)"""

# =============================================================================
# CONSTANTES DE CULTIVOS - PINO
# =============================================================================

SUPERFICIE_PINO = 2.0
"""float: Superficie requerida por pino (metros cuadrados)"""

AGUA_INICIAL_PINO = 2
"""int: Agua inicial de un pino (litros)"""

ALTURA_INICIAL_ARBOL = 1.0
"""float: Altura inicial de arboles (metros)"""

CRECIMIENTO_PINO = 0.10
"""float: Crecimiento del pino por riego (metros)"""

# =============================================================================
# CONSTANTES DE CULTIVOS - OLIVO
# =============================================================================

SUPERFICIE_OLIVO = 3.0
"""float: Superficie requerida por olivo (metros cuadrados)"""

AGUA_INICIAL_OLIVO = 5
"""int: Agua inicial de un olivo (litros)"""

CRECIMIENTO_OLIVO = 0.01
"""float: Crecimiento del olivo por riego (metros)"""

# =============================================================================
# CONSTANTES DE CULTIVOS - LECHUGA
# =============================================================================

SUPERFICIE_LECHUGA = 0.10
"""float: Superficie requerida por lechuga (metros cuadrados)"""

AGUA_INICIAL_LECHUGA = 1
"""int: Agua inicial de una lechuga (litros)"""

# =============================================================================
# CONSTANTES DE CULTIVOS - ZANAHORIA
# =============================================================================

SUPERFICIE_ZANAHORIA = 0.15
"""float: Superficie requerida por zanahoria (metros cuadrados)"""

AGUA_INICIAL_ZANAHORIA = 0
"""int: Agua inicial de una zanahoria (litros)"""

# =============================================================================
# CONSTANTES DE ESTRATEGIAS DE ABSORCION
# =============================================================================

ABSORCION_SEASONAL_VERANO = 5
"""int: Absorcion de agua en verano (litros)"""

ABSORCION_SEASONAL_INVIERNO = 2
"""int: Absorcion de agua en invierno (litros)"""

MES_INICIO_VERANO = 3
"""int: Mes de inicio del verano (marzo)"""

MES_FIN_VERANO = 8
"""int: Mes de fin del verano (agosto)"""

# =============================================================================
# CONSTANTES DE PERSISTENCIA
# =============================================================================

DIRECTORIO_DATA = "data"
"""str: Directorio para almacenar datos persistidos"""

EXTENSION_DATA = ".dat"
"""str: Extension de archivos de datos"""

# =============================================================================
# ENUMS
# =============================================================================

class TipoOperacionPersistencia(Enum):
    """Tipos de operaciones de persistencia."""
    ESCRITURA = "escritura"
    LECTURA = "lectura"


################################################################################
# DIRECTORIO: entidades
################################################################################

# ==============================================================================
# ARCHIVO 3/66: __init__.py
# Directorio: entidades
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/__init__.py
# ==============================================================================

# =============================================================================
# python_forestacion/entidades/__init__.py
# =============================================================================
"""Entidades del dominio forestal."""


################################################################################
# DIRECTORIO: entidades/cultivos
################################################################################

# ==============================================================================
# ARCHIVO 4/66: __init__.py
# Directorio: entidades/cultivos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/cultivos/__init__.py
# ==============================================================================

# =============================================================================
# python_forestacion/entidades/cultivos/__init__.py
# =============================================================================
"""Entidades de cultivos."""

from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna


__all__ = [
    'Cultivo',
    'Arbol',
    'Hortaliza',
    'Pino',
    'Olivo',
    'Lechuga',
    'Zanahoria',
    'TipoAceituna'
]

# ==============================================================================
# ARCHIVO 5/66: arbol.py
# Directorio: entidades/cultivos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/cultivos/arbol.py
# ==============================================================================

from python_forestacion.entidades.cultivos.cultivo import Cultivo

class Arbol(Cultivo):
    """
    Clase base para cultivos arboreos.

    Los arboles tienen una altura que crece con el tiempo.

    Atributos adicionales:
        altura: Altura del arbol en metros
    """

    def __init__(self, agua: int, superficie: float, altura: float):
        """
        Inicializa un arbol.

        Args:
            agua: Agua inicial en litros
            superficie: Superficie en metros cuadrados
            altura: Altura inicial en metros
        """
        super().__init__(agua, superficie)
        self._altura = altura

    def get_altura(self) -> float:
        """Obtiene la altura del arbol."""
        return self._altura

    def set_altura(self, altura: float) -> None:
        """Establece la altura del arbol."""
        self._altura = altura


# ==============================================================================
# ARCHIVO 6/66: cultivo.py
# Directorio: entidades/cultivos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/cultivos/cultivo.py
# ==============================================================================

from abc import ABC

class Cultivo(ABC):
    """
    Clase base abstracta para todos los cultivos.

    Atributos:
        agua: Cantidad de agua almacenada (litros)
        superficie: Superficie ocupada (metros cuadrados)
        id_cultivo: Identificador unico del cultivo
    """

    _contador_id = 0

    def __init__(self, agua: int, superficie: float):
        """
        Inicializa un cultivo.

        Args:
            agua: Agua inicial en litros
            superficie: Superficie en metros cuadrados
        """
        Cultivo._contador_id += 1
        self._id_cultivo = Cultivo._contador_id
        self._agua = agua
        self._superficie = superficie

    def get_id_cultivo(self) -> int:
        """Obtiene el ID del cultivo."""
        return self._id_cultivo

    def get_agua(self) -> int:
        """Obtiene el agua almacenada."""
        return self._agua

    def set_agua(self, agua: int) -> None:
        """Establece el agua almacenada."""
        self._agua = agua

    def get_superficie(self) -> float:
        """Obtiene la superficie ocupada."""
        return self._superficie

    def set_superficie(self, superficie: float) -> None:
        """Establece la superficie ocupada."""
        self._superficie = superficie




# ==============================================================================
# ARCHIVO 7/66: hortaliza.py
# Directorio: entidades/cultivos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/cultivos/hortaliza.py
# ==============================================================================

from python_forestacion.entidades.cultivos.cultivo import Cultivo


class Hortaliza(Cultivo):
    """
    Clase base para cultivos horticolas.

    Las hortalizas pueden cultivarse en invernadero.

    Atributos adicionales:
        invernadero: Indica si esta en invernadero
    """

    def __init__(self, agua: int, superficie: float, invernadero: bool):
        """
        Inicializa una hortaliza.

        Args:
            agua: Agua inicial en litros
            superficie: Superficie en metros cuadrados
            invernadero: True si esta en invernadero
        """
        super().__init__(agua, superficie)
        self._invernadero = invernadero

    def esta_en_invernadero(self) -> bool:
        """Verifica si esta en invernadero."""
        return self._invernadero

    def set_invernadero(self, invernadero: bool) -> None:
        """Establece si esta en invernadero."""
        self._invernadero = invernadero



# ==============================================================================
# ARCHIVO 8/66: lechuga.py
# Directorio: entidades/cultivos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/cultivos/lechuga.py
# ==============================================================================

from python_forestacion.constantes import AGUA_INICIAL_LECHUGA, SUPERFICIE_LECHUGA
from python_forestacion.entidades.cultivos.hortaliza import Hortaliza


class Lechuga(Hortaliza):
    """
    Cultivo: Lechuga.

    Hortaliza de hoja verde cultivada en invernadero.
    """

    def __init__(self, variedad: str):
        """
        Inicializa una lechuga.

        Args:
            variedad: Variedad de lechuga (Crespa, Mantecosa, etc.)
        """
        super().__init__(
            agua=AGUA_INICIAL_LECHUGA,
            superficie=SUPERFICIE_LECHUGA,
            invernadero=True
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        """Obtiene la variedad de lechuga."""
        return self._variedad

    def set_variedad(self, variedad: str) -> None:
        """Establece la variedad de lechuga."""
        self._variedad = variedad


# ==============================================================================
# ARCHIVO 9/66: olivo.py
# Directorio: entidades/cultivos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/cultivos/olivo.py
# ==============================================================================

from python_forestacion.constantes import AGUA_INICIAL_OLIVO, SUPERFICIE_OLIVO, ALTURA_INICIAL_ARBOL
from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna


class Olivo(Arbol):
    """
    Cultivo: Olivo.

    Arbol frutal con tipo de aceituna especifico.
    """

    def __init__(self, tipo_aceituna: TipoAceituna):
        """
        Inicializa un olivo.

        Args:
            tipo_aceituna: Tipo de aceituna del olivo
        """
        super().__init__(
            agua=AGUA_INICIAL_OLIVO,
            superficie=SUPERFICIE_OLIVO,
            altura=ALTURA_INICIAL_ARBOL
        )
        self._tipo_aceituna = tipo_aceituna

    def get_tipo_aceituna(self) -> TipoAceituna:
        """Obtiene el tipo de aceituna."""
        return self._tipo_aceituna

    def set_tipo_aceituna(self, tipo_aceituna: TipoAceituna) -> None:
        """Establece el tipo de aceituna."""
        self._tipo_aceituna = tipo_aceituna



# ==============================================================================
# ARCHIVO 10/66: pino.py
# Directorio: entidades/cultivos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/cultivos/pino.py
# ==============================================================================

# Local application
from python_forestacion.constantes import (
    SUPERFICIE_PINO,
    AGUA_INICIAL_PINO,
    ALTURA_INICIAL_ARBOL,
)
from python_forestacion.entidades.cultivos.arbol import Arbol


class Pino(Arbol):
    """
    Cultivo: Pino.

    Arbol forestal con variedad especifica.
    """

    def __init__(self, variedad: str):
        """
        Inicializa un pino.

        Args:
            variedad: Variedad del pino (Parana, Elliott, etc.)
        """
        super().__init__(
            agua=AGUA_INICIAL_PINO,
            superficie=SUPERFICIE_PINO,
            altura=ALTURA_INICIAL_ARBOL
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        """Obtiene la variedad del pino."""
        return self._variedad

    def set_variedad(self, variedad: str) -> None:
        """Establece la variedad del pino."""
        self._variedad = variedad

# ==============================================================================
# ARCHIVO 11/66: tipo_aceituna.py
# Directorio: entidades/cultivos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/cultivos/tipo_aceituna.py
# ==============================================================================

from enum import Enum

class TipoAceituna(Enum):
    """Tipos de aceituna para olivos."""
    ARBEQUINA = "Arbequina"
    PICUAL = "Picual"
    MANZANILLA = "Manzanilla"

# ==============================================================================
# ARCHIVO 12/66: zanahoria.py
# Directorio: entidades/cultivos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/cultivos/zanahoria.py
# ==============================================================================

from python_forestacion.constantes import AGUA_INICIAL_ZANAHORIA, SUPERFICIE_ZANAHORIA
from python_forestacion.entidades.cultivos.hortaliza import Hortaliza


class Zanahoria(Hortaliza):
    """
    Cultivo: Zanahoria.

    Hortaliza de raiz cultivada a campo abierto.
    """

    def __init__(self, es_baby_carrot: bool):
        """
        Inicializa una zanahoria.

        Args:
            es_baby_carrot: True si es baby carrot
        """
        super().__init__(
            agua=AGUA_INICIAL_ZANAHORIA,
            superficie=SUPERFICIE_ZANAHORIA,
            invernadero=False
        )
        self._es_baby_carrot = es_baby_carrot

    def is_baby_carrot(self) -> bool:
        """Verifica si es baby carrot."""
        return self._es_baby_carrot

    def set_baby_carrot(self, es_baby_carrot: bool) -> None:
        """Establece si es baby carrot."""
        self._es_baby_carrot = es_baby_carrot


################################################################################
# DIRECTORIO: entidades/personal
################################################################################

# ==============================================================================
# ARCHIVO 13/66: __init__.py
# Directorio: entidades/personal
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/personal/__init__.py
# ==============================================================================

"""Entidades de personal."""

from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.herramienta import Herramienta
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.personal.apto_medico import AptoMedico

__all__ = [
    'Trabajador',
    'Herramienta',
    'Tarea',
    'AptoMedico'
]


# ==============================================================================
# ARCHIVO 14/66: apto_medico.py
# Directorio: entidades/personal
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/personal/apto_medico.py
# ==============================================================================

from datetime import date

class AptoMedico:
    """
    Certificacion medica de un trabajador.

    Attributes:
        apto: Estado de aptitud
        fecha_emision: Fecha de emision del apto
        observaciones: Observaciones medicas
    """

    def __init__(self, apto: bool, fecha_emision: date, observaciones: str):
        """
        Inicializa un apto medico.

        Args:
            apto: True si esta apto
            fecha_emision: Fecha de emision
            observaciones: Observaciones medicas
        """
        self._apto = apto
        self._fecha_emision = fecha_emision
        self._observaciones = observaciones

    def esta_apto(self) -> bool:
        """Verifica si esta apto."""
        return self._apto

    def get_fecha_emision(self) -> date:
        """Obtiene la fecha de emision."""
        return self._fecha_emision

    def get_observaciones(self) -> str:
        """Obtiene las observaciones."""
        return self._observaciones


# ==============================================================================
# ARCHIVO 15/66: herramienta.py
# Directorio: entidades/personal
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/personal/herramienta.py
# ==============================================================================

class Herramienta:
    """
    Herramienta de trabajo.

    Attributes:
        id_herramienta: Identificador unico
        nombre: Nombre de la herramienta
        certificado_hys: Certificacion de higiene y seguridad
    """

    def __init__(self, id_herramienta: int, nombre: str, certificado_hys: bool):
        """
        Inicializa una herramienta.

        Args:
            id_herramienta: ID unico
            nombre: Nombre
            certificado_hys: Certificacion H&S
        """
        self._id_herramienta = id_herramienta
        self._nombre = nombre
        self._certificado_hys = certificado_hys

    def get_id_herramienta(self) -> int:
        """Obtiene el ID."""
        return self._id_herramienta

    def get_nombre(self) -> str:
        """Obtiene el nombre."""
        return self._nombre

    def tiene_certificado_hys(self) -> bool:
        """Verifica si tiene certificacion H&S."""
        return self._certificado_hys


# ==============================================================================
# ARCHIVO 16/66: tarea.py
# Directorio: entidades/personal
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/personal/tarea.py
# ==============================================================================

from datetime import date

class Tarea:
    """
    Tarea asignada a un trabajador.

    Attributes:
        id_tarea: Identificador unico
        fecha: Fecha programada
        descripcion: Descripcion de la tarea
    """

    def __init__(self, id_tarea: int, fecha: date, descripcion: str):
        """
        Inicializa una tarea.

        Args:
            id_tarea: ID unico
            fecha: Fecha programada
            descripcion: Descripcion
        """
        self._id_tarea = id_tarea
        self._fecha = fecha
        self._descripcion = descripcion

    def get_id_tarea(self) -> int:
        """Obtiene el ID de la tarea."""
        return self._id_tarea

    def get_fecha(self) -> date:
        """Obtiene la fecha."""
        return self._fecha

    def get_descripcion(self) -> str:
        """Obtiene la descripcion."""
        return self._descripcion


# ==============================================================================
# ARCHIVO 17/66: trabajador.py
# Directorio: entidades/personal
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/personal/trabajador.py
# ==============================================================================

from typing import List

from python_forestacion.entidades.personal.apto_medico import AptoMedico
from python_forestacion.entidades.personal.tarea import Tarea


class Trabajador:
    """
    Trabajador agricola.

    Attributes:
        dni: DNI del trabajador
        nombre: Nombre completo
        tareas: Lista de tareas asignadas
        apto_medico: Certificacion medica
    """

    def __init__(self, dni: int, nombre: str, tareas: List[Tarea]):
        """
        Inicializa un trabajador.

        Args:
            dni: DNI
            nombre: Nombre completo
            tareas: Lista de tareas
        """
        self._dni = dni
        self._nombre = nombre
        self._tareas = tareas.copy()
        self._apto_medico = None

    def get_dni(self) -> int:
        """Obtiene el DNI."""
        return self._dni

    def get_nombre(self) -> str:
        """Obtiene el nombre."""
        return self._nombre

    def get_tareas(self) -> List[Tarea]:
        """Obtiene las tareas (copia defensiva)."""
        return self._tareas.copy()

    def get_apto_medico(self) -> AptoMedico:
        """Obtiene el apto medico."""
        return self._apto_medico

    def set_apto_medico(self, apto_medico: AptoMedico) -> None:
        """Establece el apto medico."""
        self._apto_medico = apto_medico


################################################################################
# DIRECTORIO: entidades/terrenos
################################################################################

# ==============================================================================
# ARCHIVO 18/66: __init__.py
# Directorio: entidades/terrenos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/terrenos/__init__.py
# ==============================================================================

"""Entidades de terrenos."""

from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal

__all__ = [
    'Tierra',
    'Plantacion',
    'RegistroForestal'
]



# ==============================================================================
# ARCHIVO 19/66: plantacion.py
# Directorio: entidades/terrenos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/terrenos/plantacion.py
# ==============================================================================

# Standard library
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class Plantacion:
    """
    Representa una plantacion agricola.

    Attributes:
        nombre: Nombre de la plantacion
        superficie: Superficie total disponible
        agua_disponible: Agua disponible en litros
        cultivos: Lista de cultivos plantados
        trabajadores: Lista de trabajadores asignados
    """

    def __init__(self, nombre: str, superficie: float, agua: int):
        """
        Inicializa una plantacion.

        Args:
            nombre: Nombre identificatorio
            superficie: Superficie en m2
            agua: Agua inicial en litros

        Raises:
            ValueError: Si agua es negativa
        """
        if agua < 0:
            raise ValueError("El agua no puede ser negativa")

        self._nombre = nombre
        self._superficie = superficie
        self._agua_disponible = agua
        self._cultivos: List['Cultivo'] = []
        self._trabajadores = []

    def get_nombre(self) -> str:
        """Obtiene el nombre."""
        return self._nombre

    def get_superficie(self) -> float:
        """Obtiene la superficie total."""
        return self._superficie

    def get_agua_disponible(self) -> int:
        """Obtiene el agua disponible."""
        return self._agua_disponible

    def set_agua_disponible(self, agua: int) -> None:
        """
        Establece el agua disponible.

        Raises:
            ValueError: Si agua es negativa
        """
        if agua < 0:
            raise ValueError("El agua no puede ser negativa")
        self._agua_disponible = agua

    def get_cultivos(self) -> List['Cultivo']:
        """Obtiene la lista de cultivos (copia defensiva)."""
        return self._cultivos.copy()

    def agregar_cultivo(self, cultivo: 'Cultivo') -> None:
        """Agrega un cultivo a la plantacion."""
        self._cultivos.append(cultivo)

    def eliminar_cultivo(self, cultivo: 'Cultivo') -> None:
        """Elimina un cultivo de la plantacion."""
        if cultivo in self._cultivos:
            self._cultivos.remove(cultivo)

    def get_trabajadores(self):
        """Obtiene la lista de trabajadores (copia defensiva)."""
        return self._trabajadores.copy()

    def set_trabajadores(self, trabajadores) -> None:
        """Establece la lista de trabajadores."""
        self._trabajadores = trabajadores.copy()

# ==============================================================================
# ARCHIVO 20/66: registro_forestal.py
# Directorio: entidades/terrenos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/terrenos/registro_forestal.py
# ==============================================================================

from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.entidades.terrenos.tierra import Tierra


class RegistroForestal:
    """
    Registro forestal completo.

    Vincula tierra, plantacion, propietario y avaluo.
    """

    def __init__(
            self,
            id_padron: int,
            tierra: Tierra,
            plantacion: Plantacion,
            propietario: str,
            avaluo: float
    ):
        """
        Inicializa un registro forestal.

        Args:
            id_padron: ID de padron
            tierra: Terreno asociado
            plantacion: Plantacion asociada
            propietario: Nombre del propietario
            avaluo: Avaluo fiscal
        """
        self._id_padron = id_padron
        self._tierra = tierra
        self._plantacion = plantacion
        self._propietario = propietario
        self._avaluo = avaluo

    def get_id_padron(self) -> int:
        """Obtiene el ID de padron."""
        return self._id_padron

    def get_tierra(self) -> Tierra:
        """Obtiene la tierra."""
        return self._tierra

    def get_plantacion(self) -> Plantacion:
        """Obtiene la plantacion."""
        return self._plantacion

    def get_propietario(self) -> str:
        """Obtiene el propietario."""
        return self._propietario

    def get_avaluo(self) -> float:
        """Obtiene el avaluo."""
        return self._avaluo


# ==============================================================================
# ARCHIVO 21/66: tierra.py
# Directorio: entidades/terrenos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/terrenos/tierra.py
# ==============================================================================


class Tierra:
    """
    Representa un terreno catastral.

    Attributes:
        id_padron_catastral: Identificador catastral unico
        superficie: Superficie en metros cuadrados
        domicilio: Ubicacion del terreno
        finca: Plantacion asociada al terreno
    """

    def __init__(
            self,
            id_padron_catastral: int,
            superficie: float,
            domicilio: str
    ):
        """
        Inicializa un terreno.

        Args:
            id_padron_catastral: Padron catastral
            superficie: Superficie en m2
            domicilio: Domicilio del terreno

        Raises:
            ValueError: Si superficie es <= 0
        """
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")

        self._id_padron_catastral = id_padron_catastral
        self._superficie = superficie
        self._domicilio = domicilio
        self._finca = None

    def get_id_padron_catastral(self) -> int:
        """Obtiene el padron catastral."""
        return self._id_padron_catastral

    def get_superficie(self) -> float:
        """Obtiene la superficie."""
        return self._superficie

    def set_superficie(self, superficie: float) -> None:
        """
        Establece la superficie.

        Raises:
            ValueError: Si superficie es <= 0
        """
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")
        self._superficie = superficie

    def get_domicilio(self) -> str:
        """Obtiene el domicilio."""
        return self._domicilio

    def set_domicilio(self, domicilio: str) -> None:
        """Establece el domicilio."""
        self._domicilio = domicilio

    def get_finca(self):
        """Obtiene la plantacion asociada."""
        return self._finca

    def set_finca(self, finca) -> None:
        """Establece la plantacion asociada."""
        self._finca = finca


################################################################################
# DIRECTORIO: excepciones
################################################################################

# ==============================================================================
# ARCHIVO 22/66: __init__.py
# Directorio: excepciones
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/excepciones/__init__.py
# ==============================================================================

"""Excepciones personalizadas."""

from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.excepciones.persistencia_exception import PersistenciaException


__all__ = [
    'ForestacionException',
    'SuperficieInsuficienteException',
    'AguaAgotadaException',
    'PersistenciaException'
]

# ==============================================================================
# ARCHIVO 23/66: agua_agotada_exception.py
# Directorio: excepciones
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/excepciones/agua_agotada_exception.py
# ==============================================================================

"""
Excepcion para casos de agua agotada en plantaciones.

Se lanza cuando se intenta regar pero no hay suficiente agua
disponible en la plantacion.
"""

from python_forestacion.excepciones.forestacion_exception import ForestacionException


class AguaAgotadaException(ForestacionException):
    """
    Excepcion lanzada cuando no hay suficiente agua para regar.

    Args:
        agua_requerida: Cantidad de agua requerida
        agua_disponible: Cantidad de agua disponible
    """

    def __init__(self, agua_requerida: int, agua_disponible: int):
        self._agua_requerida = agua_requerida
        self._agua_disponible = agua_disponible

        mensaje_usuario = (
            f"Agua agotada. "
            f"Requerida: {agua_requerida} L, "
            f"Disponible: {agua_disponible} L"
        )

        mensaje_tecnico = (
            f"AguaAgotadaException: "
            f"agua_requerida={agua_requerida}, "
            f"agua_disponible={agua_disponible}"
        )

        super().__init__(mensaje_usuario, mensaje_tecnico)

    def get_agua_requerida(self) -> int:
        """Obtiene el agua requerida."""
        return self._agua_requerida

    def get_agua_disponible(self) -> int:
        """Obtiene el agua disponible."""
        return self._agua_disponibleble

# ==============================================================================
# ARCHIVO 24/66: forestacion_exception.py
# Directorio: excepciones
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/excepciones/forestacion_exception.py
# ==============================================================================


class ForestacionException(Exception):
    """
    Excepcion base para el sistema de gestion forestal.

    Proporciona mensajes separados para usuarios y tecnicos,
    permitiendo manejar errores de forma contextualizada.

    Args:
        mensaje_usuario: Mensaje legible para el usuario final
        mensaje_tecnico: Mensaje tecnico con detalles del error
        causa: Excepcion original que causo este error (opcional)
    """

    def __init__(
            self,
            mensaje_usuario: str,
            mensaje_tecnico: str,
            causa: Exception = None
    ):
        self._mensaje_usuario = mensaje_usuario
        self._mensaje_tecnico = mensaje_tecnico
        self._causa = causa
        super().__init__(mensaje_tecnico)

    def get_user_message(self) -> str:
        """
        Obtiene el mensaje para el usuario final.

        Returns:
            Mensaje legible para usuarios no tecnicos
        """
        return self._mensaje_usuario

    def get_technical_message(self) -> str:
        """
        Obtiene el mensaje tecnico detallado.

        Returns:
            Mensaje con detalles tecnicos del error
        """
        return self._mensaje_tecnico

    def get_causa(self) -> Exception:
        """
        Obtiene la excepcion original que causo este error.

        Returns:
            Excepcion original o None si no hay causa
        """
        return self._causa

    def get_full_message(self) -> str:
        """
        Obtiene el mensaje completo combinando ambos mensajes.

        Returns:
            Mensaje completo con informacion de usuario y tecnica
        """
        mensaje = f"[USUARIO] {self._mensaje_usuario}\n"
        mensaje += f"[TECNICO] {self._mensaje_tecnico}"
        if self._causa:
            mensaje += f"\n[CAUSA] {str(self._causa)}"
        return mensaje

# ==============================================================================
# ARCHIVO 25/66: mensajes_exception.py
# Directorio: excepciones
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/excepciones/mensajes_exception.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 26/66: persistencia_exception.py
# Directorio: excepciones
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/excepciones/persistencia_exception.py
# ==============================================================================

"""
Excepcion para errores de persistencia de datos.

Se lanza cuando ocurren problemas al guardar o leer registros
forestales desde disco.
"""

from enum import Enum

from python_forestacion.constantes import TipoOperacionPersistencia
from python_forestacion.excepciones.forestacion_exception import ForestacionException

class PersistenciaException(ForestacionException):
    """
    Excepcion lanzada cuando ocurre un error de persistencia.

    Args:
        nombre_archivo: Nombre del archivo involucrado
        tipo_operacion: Tipo de operacion (lectura/escritura)
        causa: Excepcion original
    """

    def __init__(
            self,
            nombre_archivo: str,
            tipo_operacion: TipoOperacionPersistencia,
            causa: Exception
    ):
        self._nombre_archivo = nombre_archivo
        self._tipo_operacion = tipo_operacion

        mensaje_usuario = (
            f"Error al {tipo_operacion.value} el archivo {nombre_archivo}"
        )

        mensaje_tecnico = (
            f"PersistenciaException: "
            f"archivo={nombre_archivo}, "
            f"operacion={tipo_operacion.value}, "
            f"causa={type(causa).__name__}"
        )

        super().__init__(mensaje_usuario, mensaje_tecnico, causa)

    def get_nombre_archivo(self) -> str:
        """Obtiene el nombre del archivo."""
        return self._nombre_archivo

    def get_tipo_operacion(self) -> TipoOperacionPersistencia:
        """Obtiene el tipo de operacion."""
        return self._tipo_operacionTipoOperacionPersistencia.ESCRITURA

# ==============================================================================
# ARCHIVO 27/66: superficie_insuficiente_exception.py
# Directorio: excepciones
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/excepciones/superficie_insuficiente_exception.py
# ==============================================================================

"""
Excepcion para casos de superficie insuficiente en plantaciones.

Se lanza cuando se intenta plantar cultivos pero no hay suficiente
superficie disponible en la plantacion.
"""

from python_forestacion.excepciones.forestacion_exception import ForestacionException

class SuperficieInsuficienteException(ForestacionException):
    """
    Excepcion lanzada cuando no hay suficiente superficie para plantar.

    Args:
        superficie_requerida: Superficie total requerida
        superficie_disponible: Superficie actualmente disponible
    """

    def __init__(self, superficie_requerida: float, superficie_disponible: float):
        self._superficie_requerida = superficie_requerida
        self._superficie_disponible = superficie_disponible

        mensaje_usuario = (
            f"No hay suficiente superficie disponible. "
            f"Requerida: {superficie_requerida} m2, "
            f"Disponible: {superficie_disponible} m2"
        )

        mensaje_tecnico = (
            f"SuperficieInsuficienteException: "
            f"superficie_requerida={superficie_requerida}, "
            f"superficie_disponible={superficie_disponible}"
        )

        super().__init__(mensaje_usuario, mensaje_tecnico)

    def get_superficie_requerida(self) -> float:
        """Obtiene la superficie requerida."""
        return self._superficie_requerida

    def get_superficie_disponible(self) -> float:
        """Obtiene la superficie disponible."""
        return self._superficie_disponible




################################################################################
# DIRECTORIO: patrones
################################################################################

# ==============================================================================
# ARCHIVO 28/66: __init__.py
# Directorio: patrones
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/__init__.py
# ==============================================================================

"""Implementaciones de patrones de diseno."""



################################################################################
# DIRECTORIO: patrones/factory
################################################################################

# ==============================================================================
# ARCHIVO 29/66: __init__.py
# Directorio: patrones/factory
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/factory/__init__.py
# ==============================================================================

"""Patron Factory Method."""

from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory

__all__ = ['CultivoFactory']

# ==============================================================================
# ARCHIVO 30/66: cultivo_factory.py
# Directorio: patrones/factory
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/factory/cultivo_factory.py
# ==============================================================================


# Local application
from python_forestacion.entidades.cultivos import Cultivo, Pino, Olivo, Lechuga, Zanahoria, TipoAceituna


class CultivoFactory:
    """
    Factory para crear cultivos.

    Proporciona un punto centralizado para la creacion
    de todos los tipos de cultivos del sistema.
    """

    @staticmethod
    def crear_cultivo(especie: str) -> Cultivo:
        """
        Crea un cultivo segun la especie especificada.

        Args:
            especie: Nombre de la especie (Pino, Olivo, Lechuga, Zanahoria)

        Returns:
            Instancia del cultivo creado

        Raises:
            ValueError: Si la especie es desconocida
        """
        factories = {
            "Pino": CultivoFactory._crear_pino,
            "Olivo": CultivoFactory._crear_olivo,
            "Lechuga": CultivoFactory._crear_lechuga,
            "Zanahoria": CultivoFactory._crear_zanahoria
        }

        if especie not in factories:
            raise ValueError(f"Especie desconocida: {especie}")

        return factories[especie]()

    @staticmethod
    def _crear_pino() -> Cultivo:
        """
        Crea un Pino con valores por defecto.

        Returns:
            Instancia de Pino
        """
        return Pino(variedad="Parana")

    @staticmethod
    def _crear_olivo() -> Cultivo:
        """
        Crea un Olivo con valores por defecto.

        Returns:
            Instancia de Olivo
        """
        return Olivo(tipo_aceituna=TipoAceituna.ARBEQUINA)

    @staticmethod
    def _crear_lechuga() -> Cultivo:
        """
        Crea una Lechuga con valores por defecto.

        Returns:
            Instancia de Lechuga
        """
        return Lechuga(variedad="Crespa")

    @staticmethod
    def _crear_zanahoria() -> Cultivo:
        """
        Crea una Zanahoria con valores por defecto.

        Returns:
            Instancia de Zanahoria
        """
        return Zanahoria(es_baby_carrot=False)


################################################################################
# DIRECTORIO: patrones/observer
################################################################################

# ==============================================================================
# ARCHIVO 31/66: __init__.py
# Directorio: patrones/observer
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/observer/__init__.py
# ==============================================================================

"""Patron Observer."""

from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.patrones.observer.observer import Observer

__all__ = ['Observable', 'Observer']


# ==============================================================================
# ARCHIVO 32/66: observable.py
# Directorio: patrones/observer
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/observer/observable.py
# ==============================================================================

from python_forestacion.patrones.observer.observer import Observer
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List

T = TypeVar('T')

class Observable(Generic[T], ABC):
    """
    Clase Observable generica.

    Los objetos observables mantienen una lista de observadores
    y los notifican cuando ocurren eventos.

    Type Parameters:
        T: Tipo de evento que el observable puede emitir
    """

    def __init__(self):
        """Inicializa la lista de observadores."""
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        """
        Agrega un observador a la lista.

        Args:
            observador: Observador a agregar
        """
        if observador not in self._observadores:
            self._observadores.append(observador)

    def eliminar_observador(self, observador: Observer[T]) -> None:
        """
        Elimina un observador de la lista.

        Args:
            observador: Observador a eliminar
        """
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notificar_observadores(self, evento: T) -> None:
        """
        Notifica a todos los observadores sobre un evento.

        Args:
            evento: Evento a notificar
        """
        for observador in self._observadores:
            observador.actualizar(evento)

# ==============================================================================
# ARCHIVO 33/66: observer.py
# Directorio: patrones/observer
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/observer/observer.py
# ==============================================================================

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List

T = TypeVar('T')


class Observer(Generic[T], ABC):
    """
    Interfaz Observer generica.

    Los observadores deben implementar el metodo actualizar()
    para recibir notificaciones de eventos.

    Type Parameters:
        T: Tipo de evento que el observador puede manejar
    """

    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """
        Metodo llamado cuando ocurre un evento observable.

        Args:
            evento: Evento que ocurrio
        """
        pass




################################################################################
# DIRECTORIO: patrones/observer/eventos
################################################################################

# ==============================================================================
# ARCHIVO 34/66: __init__.py
# Directorio: patrones/observer/eventos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/observer/eventos/__init__.py
# ==============================================================================

from python_forestacion.patrones.observer.eventos.evento_plantacion import (
    EventoPlantacion,
    TipoEventoPlantacion
)

# ==============================================================================
# ARCHIVO 35/66: evento_plantacion.py
# Directorio: patrones/observer/eventos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/observer/eventos/evento_plantacion.py
# ==============================================================================



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

# ==============================================================================
# ARCHIVO 36/66: evento_sensor.py
# Directorio: patrones/observer/eventos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/observer/eventos/evento_sensor.py
# ==============================================================================


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


################################################################################
# DIRECTORIO: patrones/singleton
################################################################################

# ==============================================================================
# ARCHIVO 37/66: __init__.py
# Directorio: patrones/singleton
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/singleton/__init__.py
# ==============================================================================

"""
============================================================================
PATRÓN SINGLETON - Package
============================================================================

Este paquete reexporta el patrón Singleton aplicado al CultivoServiceRegistry.

El patrón Singleton garantiza que una clase tenga solo una instancia única
y proporciona un punto de acceso global a ella.

La implementación real está en servicios/cultivos/cultivo_service_registry.py
Este paquete solo sirve para demostrar el patrón educativamente.

Uso:
    from python_forestacion.patrones.singleton import CultivoServiceRegistry

    # Primera instancia
    registry1 = CultivoServiceRegistry()

    # Segunda instancia (reutiliza la primera)
    registry2 = CultivoServiceRegistry()

    # Son la misma instancia
    assert registry1 is registry2  # True
"""

# Reexportar desde la implementación de producción
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry

__all__ = ['CultivoServiceRegistry']


################################################################################
# DIRECTORIO: patrones/strategy
################################################################################

# ==============================================================================
# ARCHIVO 38/66: __init__.py
# Directorio: patrones/strategy
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/strategy/__init__.py
# ==============================================================================

"""Patron Strategy."""

from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from python_forestacion.patrones.strategy.impl import AbsorcionSeasonalStrategy, AbsorcionConstanteStrategy

__all__ = [
    'AbsorcionAguaStrategy', 'AbsorcionSeasonalStrategy', 'AbsorcionConstanteStrategy'
]


# ==============================================================================
# ARCHIVO 39/66: absorcion_agua_strategy.py
# Directorio: patrones/strategy
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/strategy/absorcion_agua_strategy.py
# ==============================================================================



# Standard library
from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionAguaStrategy(ABC):
    """
    Interfaz Strategy para algoritmos de absorcion de agua.

    Define el contrato que deben cumplir todas las estrategias
    de absorcion de agua.
    """

    @abstractmethod
    def calcular_absorcion(
            self,
            fecha: date,
            temperatura: float,
            humedad: float,
            cultivo: 'Cultivo'
    ) -> int:
        """
        Calcula la cantidad de agua que absorbe un cultivo.

        Args:
            fecha: Fecha actual
            temperatura: Temperatura ambiente
            humedad: Humedad ambiente
            cultivo: Cultivo que absorbe agua

        Returns:
            Cantidad de agua absorbida en litros
        """
        pass





################################################################################
# DIRECTORIO: patrones/strategy/impl
################################################################################

# ==============================================================================
# ARCHIVO 40/66: __init__.py
# Directorio: patrones/strategy/impl
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/strategy/impl/__init__.py
# ==============================================================================

from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy

__all__ = ["AbsorcionConstanteStrategy", "AbsorcionSeasonalStrategy"]

# ==============================================================================
# ARCHIVO 41/66: absorcion_constante_strategy.py
# Directorio: patrones/strategy/impl
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/strategy/impl/absorcion_constante_strategy.py
# ==============================================================================

from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
# Standard library
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo



class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """
    Estrategia de absorcion constante.

    La cantidad de agua absorbida es siempre la misma,
    independientemente de las condiciones ambientales.
    """

    def __init__(self, cantidad_constante: int):
        """
        Inicializa la estrategia con una cantidad fija.

        Args:
            cantidad_constante: Litros de agua a absorber siempre
        """
        self._cantidad_constante = cantidad_constante

    def calcular_absorcion(
            self,
            fecha: date,
            temperatura: float,
            humedad: float,
            cultivo: 'Cultivo'
    ) -> int:
        """
        Retorna cantidad constante.

        Args:
            fecha: No utilizado en esta estrategia
            temperatura: No utilizado en esta estrategia
            humedad: No utilizado en esta estrategia
            cultivo: No utilizado en esta estrategia

        Returns:
            Cantidad constante configurada
        """
        return self._cantidad_constante

# ==============================================================================
# ARCHIVO 42/66: absorcion_seasonal_strategy.py
# Directorio: patrones/strategy/impl
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/strategy/impl/absorcion_seasonal_strategy.py
# ==============================================================================


from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
# Local application
from python_forestacion.constantes import (
    ABSORCION_SEASONAL_VERANO,
    ABSORCION_SEASONAL_INVIERNO,
    MES_INICIO_VERANO,
    MES_FIN_VERANO
)
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """
    Estrategia de absorcion estacional.

    La cantidad de agua absorbida depende de la temporada del ano:
    - Verano: Mayor absorcion
    - Invierno: Menor absorcion
    """

    def calcular_absorcion(
            self,
            fecha: date,
            temperatura: float,
            humedad: float,
            cultivo: 'Cultivo'
    ) -> int:
        """
        Calcula absorcion segun temporada.

        Args:
            fecha: Fecha actual (usado para determinar temporada)
            temperatura: No utilizado en esta estrategia
            humedad: No utilizado en esta estrategia
            cultivo: No utilizado en esta estrategia

        Returns:
            Absorcion en litros (5L verano, 2L invierno)
        """
        mes = fecha.month
        if MES_INICIO_VERANO <= mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO
        else:
            return ABSORCION_SEASONAL_INVIERNO



################################################################################
# DIRECTORIO: riego
################################################################################

# ==============================================================================
# ARCHIVO 43/66: __init__.py
# Directorio: riego
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/riego/__init__.py
# ==============================================================================

"""Sistema de riego automatizado."""



################################################################################
# DIRECTORIO: riego/control
################################################################################

# ==============================================================================
# ARCHIVO 44/66: __init__.py
# Directorio: riego/control
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/riego/control/__init__.py
# ==============================================================================

"""Control de riego."""

from python_forestacion.riego.control.control_riego_task import ControlRiegoTask

__all__ = ['ControlRiegoTask']

# ==============================================================================
# ARCHIVO 45/66: control_riego_task.py
# Directorio: riego/control
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/riego/control/control_riego_task.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: riego/sensores
################################################################################

# ==============================================================================
# ARCHIVO 46/66: __init__.py
# Directorio: riego/sensores
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/riego/sensores/__init__.py
# ==============================================================================

"""Sensores ambientales."""

from python_forestacion.riego.sensores.temperatura_reader_task import (
    TemperaturaReaderTask
)
from python_forestacion.riego.sensores.humedad_reader_task import (
    HumedadReaderTask
)

__all__ = ['TemperaturaReaderTask', 'HumedadReaderTask']


# ==============================================================================
# ARCHIVO 47/66: humedad_reader_task.py
# Directorio: riego/sensores
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/riego/sensores/humedad_reader_task.py
# ==============================================================================


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


# ==============================================================================
# ARCHIVO 48/66: temperatura_reader_task.py
# Directorio: riego/sensores
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/riego/sensores/temperatura_reader_task.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: servicios
################################################################################

# ==============================================================================
# ARCHIVO 49/66: __init__.py
# Directorio: servicios
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/__init__.py
# ==============================================================================

"""Servicios de negocio."""



################################################################################
# DIRECTORIO: servicios/cultivos
################################################################################

# ==============================================================================
# ARCHIVO 50/66: __init__.py
# Directorio: servicios/cultivos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/cultivos/__init__.py
# ==============================================================================

"""Servicios de cultivos."""

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.servicios.cultivos.pino_service import PinoService
from python_forestacion.servicios.cultivos.olivo_service import OlivoService
from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
from python_forestacion.servicios.cultivos.zanahoria_service import ZanahoriaService
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry

__all__ = [
    'CultivoService',
    'ArbolService',
    'PinoService',
    'OlivoService',
    'LechugaService',
    'ZanahoriaService',
    'CultivoServiceRegistry'
]

# ==============================================================================
# ARCHIVO 51/66: arbol_service.py
# Directorio: servicios/cultivos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/cultivos/arbol_service.py
# ==============================================================================


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




# ==============================================================================
# ARCHIVO 52/66: cultivo_service.py
# Directorio: servicios/cultivos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/cultivos/cultivo_service.py
# ==============================================================================

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



# ==============================================================================
# ARCHIVO 53/66: cultivo_service_registry.py
# Directorio: servicios/cultivos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/cultivos/cultivo_service_registry.py
# ==============================================================================


# Standard library
from threading import Lock
from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos import LechugaService, OlivoService, PinoService, ZanahoriaService
from python_forestacion.entidades.cultivos import Lechuga, Zanahoria, Olivo, Pino


if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class CultivoServiceRegistry:
    """
    Registro Singleton de servicios de cultivos.

    Implementa patron Singleton thread-safe con double-checked locking
    y patron Registry para dispatch polimorfico.
    """

    _instance = None
    _lock = Lock()

    def __new__(cls):
        """
        Controla la creacion de instancias (Singleton).

        Returns:
            La unica instancia del registry
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._inicializar_servicios()
        return cls._instance

    def _inicializar_servicios(self) -> None:
        """Inicializa los servicios y registros de handlers."""

        self._pino_service = PinoService()
        self._olivo_service = OlivoService()
        self._lechuga_service = LechugaService()
        self._zanahoria_service = ZanahoriaService()

        self._absorber_agua_handlers = {
            Pino: self._absorber_agua_pino,
            Olivo: self._absorber_agua_olivo,
            Lechuga: self._absorber_agua_lechuga,
            Zanahoria: self._absorber_agua_zanahoria
        }

        self._mostrar_datos_handlers = {
            Pino: self._mostrar_datos_pino,
            Olivo: self._mostrar_datos_olivo,
            Lechuga: self._mostrar_datos_lechuga,
            Zanahoria: self._mostrar_datos_zanahoria
        }

        # aca hice el cambio

    @classmethod
    def get_instance(cls):
        """
        Obtiene la instancia Singleton.

        Returns:
            La unica instancia del registry
        """
        if cls._instance is None:
            cls()
        return cls._instance

    def absorber_agua(self, cultivo: 'Cultivo') -> int:
        """
        Despacha absorcion de agua al servicio correcto.

        Args:
            cultivo: Cultivo que absorbe agua

        Returns:
            Cantidad de agua absorbida

        Raises:
            ValueError: Si el tipo de cultivo no esta registrado
        """
        tipo = type(cultivo)
        if tipo not in self._absorber_agua_handlers:
            raise ValueError(f"Tipo de cultivo no registrado: {tipo}")
        return self._absorber_agua_handlers[tipo](cultivo)

    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """
        Despacha mostracion de datos al servicio correcto.

        Args:
            cultivo: Cultivo a mostrar

        Raises:
            ValueError: Si el tipo de cultivo no esta registrado
        """
        tipo = type(cultivo)
        if tipo not in self._mostrar_datos_handlers:
            raise ValueError(f"Tipo de cultivo no registrado: {tipo}")
        self._mostrar_datos_handlers[tipo](cultivo)

    def _absorber_agua_pino(self, cultivo):
        """Handler para absorcion de Pino."""
        return self._pino_service.absorver_agua(cultivo)

    def _absorber_agua_olivo(self, cultivo):
        """Handler para absorcion de Olivo."""
        return self._olivo_service.absorver_agua(cultivo)

    def _absorber_agua_lechuga(self, cultivo):
        """Handler para absorcion de Lechuga."""
        return self._lechuga_service.absorver_agua(cultivo)

    def _absorber_agua_zanahoria(self, cultivo):
        """Handler para absorcion de Zanahoria."""
        return self._zanahoria_service.absorver_agua(cultivo)

    def _mostrar_datos_pino(self, cultivo):
        """Handler para mostracion de Pino."""
        self._pino_service.mostrar_datos(cultivo)

    def _mostrar_datos_olivo(self, cultivo):
        """Handler para mostracion de Olivo."""
        self._olivo_service.mostrar_datos(cultivo)

    def _mostrar_datos_lechuga(self, cultivo):
        """Handler para mostracion de Lechuga."""
        self._lechuga_service.mostrar_datos(cultivo)

    def _mostrar_datos_zanahoria(self, cultivo):
        """Handler para mostracion de Zanahoria."""
        self._zanahoria_service.mostrar_datos(cultivo)

# ==============================================================================
# ARCHIVO 54/66: lechuga_service.py
# Directorio: servicios/cultivos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/cultivos/lechuga_service.py
# ==============================================================================

from python_forestacion.patrones.strategy import AbsorcionConstanteStrategy
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class LechugaService(CultivoService):
    """Servicio para Lechugas."""

    def __init__(self):
        """Inicializa con estrategia constante."""
        super().__init__(AbsorcionConstanteStrategy(1))

    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """
        Muestra datos de la Lechuga.

        Args:
            cultivo: Lechuga a mostrar
        """
        super().mostrar_datos(cultivo)
        print(f"Variedad: {cultivo.get_variedad()}")
        print(f"Invernadero: {cultivo.esta_en_invernadero()}")


# ==============================================================================
# ARCHIVO 55/66: olivo_service.py
# Directorio: servicios/cultivos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/cultivos/olivo_service.py
# ==============================================================================

from python_forestacion.constantes import CRECIMIENTO_OLIVO
from python_forestacion.patrones.strategy import AbsorcionSeasonalStrategy
from datetime import date

from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos import ArbolService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class OlivoService(ArbolService):
    """Servicio para Olivos."""

    def __init__(self):
        """Inicializa con estrategia estacional."""
        super().__init__(AbsorcionSeasonalStrategy())

    def absorver_agua(
            self,
            cultivo: 'Cultivo',
            fecha: date = None,
            temperatura: float = 20.0,
            humedad: float = 50.0
    ) -> int:
        """
        Olivo absorbe agua y crece.

        Args:
            cultivo: Olivo que absorbe
            fecha: Fecha actual
            temperatura: Temperatura
            humedad: Humedad

        Returns:
            Agua absorbida
        """
        agua = super().absorver_agua(cultivo, fecha, temperatura, humedad)
        cultivo.set_altura(cultivo.get_altura() + CRECIMIENTO_OLIVO)
        return agua

    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """
        Muestra datos del Olivo.

        Args:
            cultivo: Olivo a mostrar
        """
        super().mostrar_datos(cultivo)
        print(f"Tipo de aceituna: {cultivo.get_tipo_aceituna().value}")


# ==============================================================================
# ARCHIVO 56/66: pino_service.py
# Directorio: servicios/cultivos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/cultivos/pino_service.py
# ==============================================================================


from datetime import date


from python_forestacion.constantes import CRECIMIENTO_PINO
from python_forestacion.patrones.strategy import AbsorcionSeasonalStrategy
from python_forestacion.servicios.cultivos.arbol_service import ArbolService


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class PinoService(ArbolService):
    """Servicio para Pinos."""

    def __init__(self):
        """Inicializa con estrategia estacional."""
        super().__init__(AbsorcionSeasonalStrategy())

    def absorver_agua(
            self,
            cultivo: 'Cultivo',
            fecha: date = None,
            temperatura: float = 20.0,
            humedad: float = 50.0
    ) -> int:
        """
        Pino absorbe agua y crece.

        Args:
            cultivo: Pino que absorbe
            fecha: Fecha actual
            temperatura: Temperatura
            humedad: Humedad

        Returns:
            Agua absorbida
        """
        agua = super().absorver_agua(cultivo, fecha, temperatura, humedad)
        cultivo.set_altura(cultivo.get_altura() + CRECIMIENTO_PINO)
        return agua

    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """
        Muestra datos del Pino.

        Args:
            cultivo: Pino a mostrar
        """
        super().mostrar_datos(cultivo)
        print(f"Variedad: {cultivo.get_variedad()}")

# ==============================================================================
# ARCHIVO 57/66: zanahoria_service.py
# Directorio: servicios/cultivos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/cultivos/zanahoria_service.py
# ==============================================================================

from python_forestacion.patrones.strategy import AbsorcionConstanteStrategy
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class ZanahoriaService(CultivoService):
    """Servicio para Zanahorias."""

    def __init__(self):
        """Inicializa con estrategia constante."""
        super().__init__(AbsorcionConstanteStrategy(2))

    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """
        Muestra datos de la Zanahoria.

        Args:
            cultivo: Zanahoria a mostrar
        """
        super().mostrar_datos(cultivo)
        print(f"Es baby carrot: {cultivo.is_baby_carrot()}")


################################################################################
# DIRECTORIO: servicios/negocio
################################################################################

# ==============================================================================
# ARCHIVO 58/66: __init__.py
# Directorio: servicios/negocio
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/negocio/__init__.py
# ==============================================================================

"""Servicios de alto nivel."""

from python_forestacion.servicios.negocio.fincas_service import FincasService
from python_forestacion.servicios.negocio.paquete import Paquete

__all__ = ['FincasService', 'Paquete']

# ==============================================================================
# ARCHIVO 59/66: fincas_service.py
# Directorio: servicios/negocio
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/negocio/fincas_service.py
# ==============================================================================


# Standard library
from typing import Dict, Type, TypeVar

# Local application
from python_forestacion.entidades.terrenos import RegistroForestal
from python_forestacion.entidades.cultivos import Cultivo
from python_forestacion.servicios.negocio.paquete import Paquete
from python_forestacion.servicios.terrenos import PlantacionService


T = TypeVar('T', bound=Cultivo)

class FincasService:
    """Servicio para operaciones de alto nivel sobre fincas."""

    def __init__(self):
        """Inicializa el servicio."""
        self._fincas: Dict[int, RegistroForestal] = {}
        self._plantacion_service = PlantacionService()

    def add_finca(self, registro: RegistroForestal) -> None:
        """
        Agrega una finca al servicio.

        Args:
            registro: Registro forestal a agregar
        """
        id_padron = registro.get_id_padron()
        self._fincas[id_padron] = registro

    def buscar_finca(self, id_padron: int) -> RegistroForestal:
        """
        Busca una finca por ID de padron.

        Args:
            id_padron: ID de padron a buscar

        Returns:
            Registro forestal encontrado o None
        """
        return self._fincas.get(id_padron)

    def fumigar(self, id_padron: int, plaguicida: str) -> None:
        """
        Fumiga una finca especifica.

        Args:
            id_padron: ID de la finca
            plaguicida: Tipo de plaguicida
        """
        registro = self.buscar_finca(id_padron)
        if registro:
            plantacion = registro.get_plantacion()
            self._plantacion_service.fumigar(plantacion, plaguicida)

    def cosechar_yempaquetar(self, tipo_cultivo: Type[T]) -> Paquete[T]:
        """
        Cosecha y empaqueta cultivos de un tipo especifico.

        Args:
            tipo_cultivo: Tipo de cultivo a cosechar

        Returns:
            Paquete con los cultivos cosechados
        """
        paquete = Paquete(tipo_cultivo)
        total_cosechados = 0

        for registro in self._fincas.values():
            plantacion = registro.get_plantacion()
            cosechados = self._plantacion_service.cosechar(
                plantacion,
                tipo_cultivo
            )
            for cultivo in cosechados:
                paquete.agregar_cultivo(cultivo)
                total_cosechados += 1

        print(f"\nCOSECHANDO {total_cosechados} unidades de {tipo_cultivo}")

        return paquete

# ==============================================================================
# ARCHIVO 60/66: paquete.py
# Directorio: servicios/negocio
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/negocio/paquete.py
# ==============================================================================


# Standard library
from typing import Type, Generic, TypeVar, List

# Local application
from python_forestacion.entidades.cultivos import Cultivo


T = TypeVar('T', bound=Cultivo)


class Paquete(Generic[T]):
    """
    Paquete generico tipo-seguro para empaquetado de cultivos.

    Type Parameters:
        T: Tipo de cultivo contenido en el paquete
    """

    _contador_id = 0

    def __init__(self, tipo_cultivo: Type[T]):
        """
        Inicializa un paquete vacio.

        Args:
            tipo_cultivo: Tipo de cultivo a empaquetar
        """
        Paquete._contador_id += 1
        self._id_paquete = Paquete._contador_id
        self._tipo_cultivo = tipo_cultivo
        self._cultivos: List[T] = []

    def agregar_cultivo(self, cultivo: T) -> None:
        """
        Agrega un cultivo al paquete.

        Args:
            cultivo: Cultivo a agregar
        """
        self._cultivos.append(cultivo)

    def get_cultivos(self) -> List[T]:
        """
        Obtiene los cultivos del paquete.

        Returns:
            Lista de cultivos
        """
        return self._cultivos.copy()

    def get_cantidad(self) -> int:
        """
        Obtiene la cantidad de cultivos.

        Returns:
            Cantidad de cultivos en el paquete
        """
        return len(self._cultivos)

    def mostrar_contenido_caja(self) -> None:
        """Muestra el contenido del paquete."""
        print("\nContenido de la caja:")
        print(f"  Tipo: {self._tipo_cultivo.__name__}")
        print(f"  Cantidad: {self.get_cantidad()}")
        print(f"  ID Paquete: {self._id_paquete}")




################################################################################
# DIRECTORIO: servicios/personal
################################################################################

# ==============================================================================
# ARCHIVO 61/66: __init__.py
# Directorio: servicios/personal
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/personal/__init__.py
# ==============================================================================

"""Servicios de personal."""

from python_forestacion.servicios.personal.trabajador_service import TrabajadorService

__all__ = ['TrabajadorService']

# ==============================================================================
# ARCHIVO 62/66: trabajador_service.py
# Directorio: servicios/personal
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/personal/trabajador_service.py
# ==============================================================================

# Standard library
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.personal.trabajador import Trabajador
    from python_forestacion.entidades.personal.herramienta import Herramienta

# Local application
from python_forestacion.entidades.personal import AptoMedico


class TrabajadorService:
    """Servicio para operaciones sobre trabajadores."""

    def asignar_apto_medico(
            self,
            trabajador: 'Trabajador',
            apto: bool,
            fecha_emision: date,
            observaciones: str
    ) -> None:
        """
        Asigna un apto medico a un trabajador.

        Args:
            trabajador: Trabajador a certificar
            apto: Estado de aptitud
            fecha_emision: Fecha de emision
            observaciones: Observaciones medicas
        """
        apto_medico = AptoMedico(apto, fecha_emision, observaciones)
        trabajador.set_apto_medico(apto_medico)

    def trabajar(
            self,
            trabajador: 'Trabajador',
            fecha: date,
            util: 'Herramienta'
    ) -> bool:
        """
        Ejecuta las tareas asignadas a un trabajador.

        Args:
            trabajador: Trabajador que ejecuta tareas
            fecha: Fecha de las tareas a ejecutar
            util: Herramienta a utilizar

        Returns:
            True si ejecuto tareas, False si no tiene apto medico
        """
        apto_medico = trabajador.get_apto_medico()

        if apto_medico is None or not apto_medico.esta_apto():
            return False

        tareas = trabajador.get_tareas()
        tareas_del_dia = [t for t in tareas if t.get_fecha() == fecha]

        tareas_ordenadas = sorted(
            tareas_del_dia,
            key=self._obtener_id_tarea,
            reverse=True
        )

        for tarea in tareas_ordenadas:
            print(
                f"El trabajador {trabajador.get_nombre()} "
                f"realizo la tarea {tarea.get_id_tarea()} "
                f"{tarea.get_descripcion()} "
                f"con herramienta: {util.get_nombre()}"
            )

        return True

    @staticmethod
    def _obtener_id_tarea(tarea):
        """
        Funcion auxiliar para ordenamiento.

        Args:
            tarea: Tarea a extraer ID

        Returns:
            ID de la tarea
        """
        return tarea.get_id_tarea()


################################################################################
# DIRECTORIO: servicios/terrenos
################################################################################

# ==============================================================================
# ARCHIVO 63/66: __init__.py
# Directorio: servicios/terrenos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/terrenos/__init__.py
# ==============================================================================

"""Servicios de terrenos."""

from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.terrenos.registro_forestal_service import (
    RegistroForestalService
)

__all__ = [
    'TierraService',
    'PlantacionService',
    'RegistroForestalService'
]


# ==============================================================================
# ARCHIVO 64/66: plantacion_service.py
# Directorio: servicios/terrenos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/terrenos/plantacion_service.py
# ==============================================================================


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



# ==============================================================================
# ARCHIVO 65/66: registro_forestal_service.py
# Directorio: servicios/terrenos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/terrenos/registro_forestal_service.py
# ==============================================================================


# Standard library
import os
import pickle

from python_forestacion.entidades.terrenos import RegistroForestal
from python_forestacion.excepciones import PersistenciaException
from python_forestacion.servicios.cultivos import CultivoServiceRegistry
from python_forestacion.constantes import (
    DIRECTORIO_DATA,
    EXTENSION_DATA,
    TipoOperacionPersistencia
)

class RegistroForestalService:
    """Servicio para operaciones sobre registros forestales."""

    def mostrar_datos(self, registro: RegistroForestal) -> None:
        """
        Muestra los datos completos de un registro.

        Args:
            registro: Registro a mostrar
        """
        print("\nREGISTRO FORESTAL")
        print("=================")
        print(f"Padron:      {registro.get_id_padron()}")
        print(f"Propietario: {registro.get_propietario()}")
        print(f"Avaluo:      {registro.get_avaluo()}")

        tierra = registro.get_tierra()
        print(f"Domicilio:   {tierra.get_domicilio()}")
        print(f"Superficie: {tierra.get_superficie()}")

        plantacion = registro.get_plantacion()
        cultivos = plantacion.get_cultivos()
        print(f"Cantidad de cultivos plantados: {len(cultivos)}")

        if cultivos:
            print("Listado de Cultivos plantados")
            print("____________________________\n")
            registry = CultivoServiceRegistry.get_instance()
            for cultivo in cultivos:
                registry.mostrar_datos(cultivo)
            print()

    def persistir(self, registro: RegistroForestal) -> None:
        """
        Persiste un registro en disco usando Pickle.

        Args:
            registro: Registro a persistir

        Raises:
            PersistenciaException: Si ocurre error al escribir
        """
        propietario = registro.get_propietario()
        nombre_archivo = f"{propietario}{EXTENSION_DATA}"
        ruta_completa = os.path.join(DIRECTORIO_DATA, nombre_archivo)

        os.makedirs(DIRECTORIO_DATA, exist_ok=True)

        archivo = None
        try:
            archivo = open(ruta_completa, 'wb')
            pickle.dump(registro, archivo)
            print(f"Registro de {propietario} persistido exitosamente en {ruta_completa}")
        except Exception as e:
            raise PersistenciaException(
                nombre_archivo,
                TipoOperacionPersistencia.ESCRITURA,
                e
            )
        finally:
            if archivo is not None:
                archivo.close()

    @staticmethod
    def leer_registro(propietario: str) -> RegistroForestal:
        """
        Lee un registro desde disco.

        Args:
            propietario: Nombre del propietario

        Returns:
            Registro leido

        Raises:
            ValueError: Si propietario es vacio
            PersistenciaException: Si ocurre error al leer
        """
        if not propietario or propietario.strip() == "":
            raise ValueError("El nombre del propietario no puede ser nulo o vacio")

        nombre_archivo = f"{propietario}{EXTENSION_DATA}"
        ruta_completa = os.path.join(DIRECTORIO_DATA, nombre_archivo)

        archivo = None
        try:
            archivo = open(ruta_completa, 'rb')
            registro = pickle.load(archivo)
            print(f"Registro de {propietario} recuperado exitosamente desde {ruta_completa}")
            return registro
        except FileNotFoundError as e:
            raise PersistenciaException(
                nombre_archivo,
                TipoOperacionPersistencia.LECTURA,
                e
            )
        except Exception as e:
            raise PersistenciaException(
                nombre_archivo,
                TipoOperacionPersistencia.LECTURA,
                e
            )
        finally:
            if archivo is not None:
                archivo.close()

# ==============================================================================
# ARCHIVO 66/66: tierra_service.py
# Directorio: servicios/terrenos
# Ruta completa: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/terrenos/tierra_service.py
# ==============================================================================


from python_forestacion.entidades.terrenos import Tierra, Plantacion
from python_forestacion.constantes import (
    AGUA_INICIAL_PLANTACION
)

class TierraService:
    """Servicio para operaciones sobre terrenos."""

    def crear_tierra_con_plantacion(
            self,
            id_padron_catastral: int,
            superficie: float,
            domicilio: str,
            nombre_plantacion: str
    ) -> Tierra:
        """
        Crea un terreno con su plantacion asociada.

        Args:
            id_padron_catastral: Padron catastral
            superficie: Superficie en m2
            domicilio: Domicilio del terreno
            nombre_plantacion: Nombre de la plantacion

        Returns:
            Terreno creado con plantacion asociada
        """
        tierra = Tierra(id_padron_catastral, superficie, domicilio)

        plantacion = Plantacion(
            nombre=nombre_plantacion,
            superficie=superficie,
            agua=AGUA_INICIAL_PLANTACION
        )

        tierra.set_finca(plantacion)
        return tierra




################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 66
# Generado: 2025-10-21 21:39:45
################################################################################



# Standard library
import time
from datetime import date

# Local application
from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService
from python_forestacion.servicios.personal.trabajador_service import TrabajadorService
from python_forestacion.servicios.negocio.fincas_service import FincasService
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.herramienta import Herramienta
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask
from python_forestacion.constantes import THREAD_JOIN_TIMEOUT


def main():
    """Funcion principal que demuestra todo el sistema."""

    print("=" * 70)
    print("         SISTEMA DE GESTION FORESTAL - PATRONES DE DISENO")
    print("=" * 70)
    print()

    # =========================================================================
    # PATRON SINGLETON: Verificar instancia unica
    # =========================================================================
    print("-" * 70)
    print("  PATRON SINGLETON: Inicializando servicios")
    print("-" * 70)

    registry1 = CultivoServiceRegistry.get_instance()
    registry2 = CultivoServiceRegistry()
    registry3 = CultivoServiceRegistry.get_instance()

    if registry1 is registry2 is registry3:
        print("[OK] Todos los servicios comparten la misma instancia del Registry")
    else:
        print("[ERROR] Las instancias no son iguales")

    print()

    # =========================================================================
    # CREACION DE TERRENO Y PLANTACION
    # =========================================================================
    print("1. Creando tierra con plantacion...")
    tierra_service = TierraService()
    terreno = tierra_service.crear_tierra_con_plantacion(
        id_padron_catastral=1,
        superficie=10000.0,
        domicilio="Agrelo, Mendoza",
        nombre_plantacion="Finca del Madero"
    )
    plantacion = terreno.get_finca()
    print(f"   Terreno creado: Padron {terreno.get_id_padron_catastral()}")
    print(f"   Plantacion: {plantacion.get_nombre()}")
    print(f"   Superficie disponible: {plantacion.get_superficie()} m2")
    print()

    # =========================================================================
    # PATRON FACTORY: Plantar cultivos
    # =========================================================================
    print("-" * 70)
    print("  PATRON FACTORY: Plantando cultivos")
    print("-" * 70)

    plantacion_service = PlantacionService()

    print("2. Plantando 5 Pinos (usa Factory Method)...")
    plantacion_service.plantar(plantacion, "Pino", 5)
    print("   [OK] 5 Pinos plantados")

    print("3. Plantando 5 Olivos (usa Factory Method)...")
    plantacion_service.plantar(plantacion, "Olivo", 5)
    print("   [OK] 5 Olivos plantados")

    print("4. Plantando 5 Lechugas (usa Factory Method)...")
    plantacion_service.plantar(plantacion, "Lechuga", 5)
    print("   [OK] 5 Lechugas plantadas")

    print("5. Plantando 5 Zanahorias (usa Factory Method)...")
    plantacion_service.plantar(plantacion, "Zanahoria", 5)
    print("   [OK] 5 Zanahorias plantadas")

    print(f"\n   Total cultivos plantados: {len(plantacion.get_cultivos())}")
    print()

    # =========================================================================
    # PATRON OBSERVER: Sistema de riego automatizado
    # =========================================================================
    print("-" * 70)
    print("  PATRON OBSERVER: Sistema de riego automatizado")
    print("-" * 70)

    print("6. Iniciando sensores y control de riego...")

    tarea_temp = TemperaturaReaderTask()
    tarea_hum = HumedadReaderTask()

    tarea_control = ControlRiegoTask(
        tarea_temp,
        tarea_hum,
        plantacion,
        plantacion_service
    )

    tarea_temp.start()
    tarea_hum.start()
    tarea_control.start()

    print("   [OK] Sensores iniciados (threads daemon)")
    print("   [OK] Control de riego activo")
    print("   Dejando funcionar el sistema por 20 segundos...")
    print()

    time.sleep(20)

    print("\n7. Deteniendo sistema de riego...")
    tarea_temp.detener()
    tarea_hum.detener()
    tarea_control.detener()

    tarea_temp.join(timeout=THREAD_JOIN_TIMEOUT)
    tarea_hum.join(timeout=THREAD_JOIN_TIMEOUT)
    tarea_control.join(timeout=THREAD_JOIN_TIMEOUT)

    print("   [OK] Sistema detenido correctamente")
    print()

    # =========================================================================
    # GESTION DE TRABAJADORES
    # =========================================================================
    print("-" * 70)
    print("  GESTION DE PERSONAL")
    print("-" * 70)

    print("8. Creando trabajador con tareas...")
    tareas = [
        Tarea(1, date.today(), "Desmalezar"),
        Tarea(2, date.today(), "Abonar"),
        Tarea(3, date.today(), "Marcar surcos")
    ]

    trabajador = Trabajador(43888734, "Juan Perez", tareas)
    plantacion.set_trabajadores([trabajador])
    print(f"   Trabajador: {trabajador.get_nombre()}")
    print(f"   Tareas asignadas: {len(trabajador.get_tareas())}")
    print()

    print("9. Asignando apto medico...")
    trabajador_service = TrabajadorService()
    trabajador_service.asignar_apto_medico(
        trabajador,
        apto=True,
        fecha_emision=date.today(),
        observaciones="Estado de salud: excelente"
    )
    print("   [OK] Apto medico asignado")
    print()

    print("10. Ejecutando tareas del trabajador...")
    herramienta = Herramienta(1, "Pala", True)
    resultado = trabajador_service.trabajar(trabajador, date.today(), herramienta)

    if resultado:
        print("   [OK] Tareas ejecutadas exitosamente")
    else:
        print("   [ERROR] No pudo trabajar")
    print()

    # =========================================================================
    # OPERACIONES DE NEGOCIO
    # =========================================================================
    print("-" * 70)
    print("  OPERACIONES DE NEGOCIO")
    print("-" * 70)

    print("11. Creando registro forestal...")
    registro = RegistroForestal(
        id_padron=1,
        tierra=terreno,
        plantacion=plantacion,
        propietario="Juan Perez",
        avaluo=50309233.55
    )
    print("   [OK] Registro creado")
    print()

    print("12. Agregando finca al servicio de gestion...")
    fincas_service = FincasService()
    fincas_service.add_finca(registro)
    print("   [OK] Finca agregada")
    print()

    print("13. Fumigando plantacion...")
    fincas_service.fumigar(1, "insecto organico")
    print()

    print("14. Cosechando y empaquetando cultivos...")
    print("\n   Cosechando Lechugas:")
    caja_lechugas = fincas_service.cosechar_yempaquetar(Lechuga)
    caja_lechugas.mostrar_contenido_caja()

    print("\n   Cosechando Pinos:")
    caja_pinos = fincas_service.cosechar_yempaquetar(Pino)
    caja_pinos.mostrar_contenido_caja()
    print()

    # =========================================================================
    # PERSISTENCIA
    # =========================================================================
    print("-" * 70)
    print("  PERSISTENCIA DE DATOS")
    print("-" * 70)

    print("15. Persistiendo registro forestal...")
    registro_service = RegistroForestalService()
    registro_service.persistir(registro)
    print()

    print("16. Recuperando registro desde disco...")
    registro_leido = RegistroForestalService.leer_registro("Juan Perez")
    print()

    print("17. Mostrando datos del registro recuperado...")
    registro_service.mostrar_datos(registro_leido)
    print()

    # =========================================================================
    # RESUMEN FINAL
    # =========================================================================
    print("=" * 70)
    print("              EJEMPLO COMPLETADO EXITOSAMENTE")
    print("=" * 70)
    print("  [OK] SINGLETON   - CultivoServiceRegistry (instancia unica)")
    print("  [OK] FACTORY     - Creacion de cultivos")
    print("  [OK] OBSERVER    - Sistema de sensores y eventos")
    print("  [OK] STRATEGY    - Algoritmos de absorcion de agua")
    print("=" * 70)


if __name__ == "__main__":
    main()