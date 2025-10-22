
# Standard library
from threading import Lock
from typing import TYPE_CHECKING

# Local application
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