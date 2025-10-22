"""
Archivo integrador generado automaticamente
Directorio: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/cultivos
Fecha: 2025-10-21 21:39:45
Total de archivos integrados: 8
"""

# ================================================================================
# ARCHIVO 1/8: __init__.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/cultivos/__init__.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 2/8: arbol_service.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/cultivos/arbol_service.py
# ================================================================================


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




# ================================================================================
# ARCHIVO 3/8: cultivo_service.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/cultivos/cultivo_service.py
# ================================================================================

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



# ================================================================================
# ARCHIVO 4/8: cultivo_service_registry.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/cultivos/cultivo_service_registry.py
# ================================================================================


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

# ================================================================================
# ARCHIVO 5/8: lechuga_service.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/cultivos/lechuga_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 6/8: olivo_service.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/cultivos/olivo_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 7/8: pino_service.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/cultivos/pino_service.py
# ================================================================================


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

# ================================================================================
# ARCHIVO 8/8: zanahoria_service.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/cultivos/zanahoria_service.py
# ================================================================================

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

