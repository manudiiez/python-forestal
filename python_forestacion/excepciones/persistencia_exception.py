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