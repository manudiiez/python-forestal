"""
Archivo integrador generado automaticamente
Directorio: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/cultivos
Fecha: 2025-10-22 10:13:59
Total de archivos integrados: 9
"""

# ================================================================================
# ARCHIVO 1/9: __init__.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/cultivos/__init__.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 2/9: arbol.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/cultivos/arbol.py
# ================================================================================

"""
Entidades de cultivos del sistema forestal.
"""
# Local application
from python_forestacion.entidades.cultivos.cultivo import Cultivo

# =============================================================================
# CLASE BASE: ARBOL
# =============================================================================


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


# ================================================================================
# ARCHIVO 3/9: cultivo.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/cultivos/cultivo.py
# ================================================================================

"""
Entidades de cultivos del sistema forestal.
"""

# Standard library
from abc import ABC


# =============================================================================
# CLASE BASE: CULTIVO
# =============================================================================

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




# ================================================================================
# ARCHIVO 4/9: hortaliza.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/cultivos/hortaliza.py
# ================================================================================

# Local application
from python_forestacion.entidades.cultivos.cultivo import Cultivo

# =============================================================================
# SUBCLASE: HORTALIZA
# =============================================================================

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



# ================================================================================
# ARCHIVO 5/9: lechuga.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/cultivos/lechuga.py
# ================================================================================

# Local application
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


# ================================================================================
# ARCHIVO 6/9: olivo.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/cultivos/olivo.py
# ================================================================================

# Local application
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



# ================================================================================
# ARCHIVO 7/9: pino.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/cultivos/pino.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 8/9: tipo_aceituna.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/cultivos/tipo_aceituna.py
# ================================================================================

# Standard library
from enum import Enum

class TipoAceituna(Enum):
    """Tipos de aceituna para olivos."""
    ARBEQUINA = "Arbequina"
    PICUAL = "Picual"
    MANZANILLA = "Manzanilla"

# ================================================================================
# ARCHIVO 9/9: zanahoria.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/entidades/cultivos/zanahoria.py
# ================================================================================

# Local application
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

