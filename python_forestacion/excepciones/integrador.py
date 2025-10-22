"""
Archivo integrador generado automaticamente
Directorio: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/excepciones
Fecha: 2025-10-22 10:13:59
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/excepciones/__init__.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 2/6: agua_agotada_exception.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/excepciones/agua_agotada_exception.py
# ================================================================================

"""
Excepcion para casos de agua agotada en plantaciones.

Se lanza cuando se intenta regar pero no hay suficiente agua
disponible en la plantacion.
"""
# Local application
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

# ================================================================================
# ARCHIVO 3/6: forestacion_exception.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/excepciones/forestacion_exception.py
# ================================================================================

"""
Excepcion base del sistema de gestion forestal.

Todas las excepciones especificas del dominio heredan de esta clase.
"""


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

# ================================================================================
# ARCHIVO 4/6: mensajes_exception.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/excepciones/mensajes_exception.py
# ================================================================================



# ================================================================================
# ARCHIVO 5/6: persistencia_exception.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/excepciones/persistencia_exception.py
# ================================================================================

"""
Excepcion para errores de persistencia de datos.

Se lanza cuando ocurren problemas al guardar o leer registros
forestales desde disco.
"""
# Local application
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

# ================================================================================
# ARCHIVO 6/6: superficie_insuficiente_exception.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/excepciones/superficie_insuficiente_exception.py
# ================================================================================

"""
Excepciones especificas del dominio forestal.
"""

# Local application
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



