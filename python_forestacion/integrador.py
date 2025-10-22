"""
Archivo integrador generado automaticamente
Directorio: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion
Fecha: 2025-10-22 10:13:59
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/__init__.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 2/2: constantes.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/constantes.py
# ================================================================================

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

