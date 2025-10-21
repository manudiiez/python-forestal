
# Standard library
from typing import Dict, Type, TypeVar

# Local application
from python_forestacion.entidades.terrenos import RegistroForestal
from python_forestacion.entidades.cultivos import Cultivo
from python_forestacion.servicios.negocio.paquete import Paquete
from python_forestacion.servicios.terrenos import PlantacionService


T = TypeVar('T', bound=Cultivo)

class FincasService:
    """Servicio para operaciones de alto nivel sobre fincas."""

    def __init__(self):
        """Inicializa el servicio."""
        self._fincas: Dict[int, RegistroForestal] = {}
        self._plantacion_service = PlantacionService()

    def add_finca(self, registro: RegistroForestal) -> None:
        """
        Agrega una finca al servicio.

        Args:
            registro: Registro forestal a agregar
        """
        id_padron = registro.get_id_padron()
        self._fincas[id_padron] = registro

    def buscar_finca(self, id_padron: int) -> RegistroForestal:
        """
        Busca una finca por ID de padron.

        Args:
            id_padron: ID de padron a buscar

        Returns:
            Registro forestal encontrado o None
        """
        return self._fincas.get(id_padron)

    def fumigar(self, id_padron: int, plaguicida: str) -> None:
        """
        Fumiga una finca especifica.

        Args:
            id_padron: ID de la finca
            plaguicida: Tipo de plaguicida
        """
        registro = self.buscar_finca(id_padron)
        if registro:
            plantacion = registro.get_plantacion()
            self._plantacion_service.fumigar(plantacion, plaguicida)

    def cosechar_yempaquetar(self, tipo_cultivo: Type[T]) -> Paquete[T]:
        """
        Cosecha y empaqueta cultivos de un tipo especifico.

        Args:
            tipo_cultivo: Tipo de cultivo a cosechar

        Returns:
            Paquete con los cultivos cosechados
        """
        paquete = Paquete(tipo_cultivo)
        total_cosechados = 0

        for registro in self._fincas.values():
            plantacion = registro.get_plantacion()
            cosechados = self._plantacion_service.cosechar(
                plantacion,
                tipo_cultivo
            )
            for cultivo in cosechados:
                paquete.agregar_cultivo(cultivo)
                total_cosechados += 1

        print(f"\nCOSECHANDO {total_cosechados} unidades de {tipo_cultivo}")

        return paquete