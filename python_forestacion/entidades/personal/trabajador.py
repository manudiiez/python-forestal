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