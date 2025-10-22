"""
Archivo integrador generado automaticamente
Directorio: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/terrenos
Fecha: 2025-10-22 10:13:59
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/terrenos/__init__.py
# ================================================================================

"""Entidades de terrenos."""

from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal

__all__ = [
    'Tierra',
    'Plantacion',
    'RegistroForestal'
]



# ================================================================================
# ARCHIVO 2/4: plantacion.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/terrenos/plantacion.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/4: registro_forestal.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/terrenos/registro_forestal.py
# ================================================================================

# Local application
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


# ================================================================================
# ARCHIVO 4/4: tierra.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/terrenos/tierra.py
# ================================================================================


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

