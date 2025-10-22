"""
Archivo integrador generado automaticamente
Directorio: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/personal
Fecha: 2025-10-22 10:13:59
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/personal/__init__.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 2/5: apto_medico.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/personal/apto_medico.py
# ================================================================================

# Standard library
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


# ================================================================================
# ARCHIVO 3/5: herramienta.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/personal/herramienta.py
# ================================================================================


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


# ================================================================================
# ARCHIVO 4/5: tarea.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/personal/tarea.py
# ================================================================================

# Standard library
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


# ================================================================================
# ARCHIVO 5/5: trabajador.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/personal/trabajador.py
# ================================================================================

# Standard library
from typing import List

# Local application
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

