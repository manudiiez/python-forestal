"""
Archivo integrador generado automaticamente
Directorio: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/negocio
Fecha: 2025-10-22 10:13:59
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/negocio/__init__.py
# ================================================================================

"""Servicios de alto nivel."""

from python_forestacion.servicios.negocio.fincas_service import FincasService
from python_forestacion.servicios.negocio.paquete import Paquete

__all__ = ['FincasService', 'Paquete']

# ================================================================================
# ARCHIVO 2/3: fincas_service.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/negocio/fincas_service.py
# ================================================================================


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

# ================================================================================
# ARCHIVO 3/3: paquete.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/negocio/paquete.py
# ================================================================================


# Standard library
from typing import Type, Generic, TypeVar, List

# Local application
from python_forestacion.entidades.cultivos import Cultivo


T = TypeVar('T', bound=Cultivo)


class Paquete(Generic[T]):
    """
    Paquete generico tipo-seguro para empaquetado de cultivos.

    Type Parameters:
        T: Tipo de cultivo contenido en el paquete
    """

    _contador_id = 0

    def __init__(self, tipo_cultivo: Type[T]):
        """
        Inicializa un paquete vacio.

        Args:
            tipo_cultivo: Tipo de cultivo a empaquetar
        """
        Paquete._contador_id += 1
        self._id_paquete = Paquete._contador_id
        self._tipo_cultivo = tipo_cultivo
        self._cultivos: List[T] = []

    def agregar_cultivo(self, cultivo: T) -> None:
        """
        Agrega un cultivo al paquete.

        Args:
            cultivo: Cultivo a agregar
        """
        self._cultivos.append(cultivo)

    def get_cultivos(self) -> List[T]:
        """
        Obtiene los cultivos del paquete.

        Returns:
            Lista de cultivos
        """
        return self._cultivos.copy()

    def get_cantidad(self) -> int:
        """
        Obtiene la cantidad de cultivos.

        Returns:
            Cantidad de cultivos en el paquete
        """
        return len(self._cultivos)

    def mostrar_contenido_caja(self) -> None:
        """Muestra el contenido del paquete."""
        print("\nContenido de la caja:")
        print(f"  Tipo: {self._tipo_cultivo.__name__}")
        print(f"  Cantidad: {self.get_cantidad()}")
        print(f"  ID Paquete: {self._id_paquete}")



