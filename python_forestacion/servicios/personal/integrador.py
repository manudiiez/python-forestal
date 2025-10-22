"""
Archivo integrador generado automaticamente
Directorio: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/personal
Fecha: 2025-10-21 21:39:45
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/personal/__init__.py
# ================================================================================

"""Servicios de personal."""

from python_forestacion.servicios.personal.trabajador_service import TrabajadorService

__all__ = ['TrabajadorService']

# ================================================================================
# ARCHIVO 2/2: trabajador_service.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/personal/trabajador_service.py
# ================================================================================

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

