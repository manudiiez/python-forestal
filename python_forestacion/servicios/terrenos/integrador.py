"""
Archivo integrador generado automaticamente
Directorio: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/terrenos
Fecha: 2025-10-22 10:13:59
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/terrenos/__init__.py
# ================================================================================

"""Servicios de terrenos."""

from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.terrenos.registro_forestal_service import (
    RegistroForestalService
)

__all__ = [
    'TierraService',
    'PlantacionService',
    'RegistroForestalService'
]


# ================================================================================
# ARCHIVO 2/4: plantacion_service.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/terrenos/plantacion_service.py
# ================================================================================

# Standard library
from typing import List, Type

# Local application
from python_forestacion.entidades.terrenos import Plantacion
from python_forestacion.entidades.cultivos import Cultivo
from python_forestacion.excepciones import SuperficieInsuficienteException, AguaAgotadaException
from python_forestacion.patrones.factory import CultivoFactory
from python_forestacion.servicios.cultivos import CultivoServiceRegistry

from python_forestacion.constantes import (
    AGUA_CONSUMIDA_POR_RIEGO,
    AGUA_MINIMA
)


class PlantacionService:
    """Servicio para operaciones sobre plantaciones."""

    def __init__(self):
        """Inicializa el servicio."""
        self._registry = CultivoServiceRegistry.get_instance()

    def plantar(
            self,
            plantacion: Plantacion,
            especie: str,
            cantidad: int
    ) -> None:
        """
        Planta cultivos en una plantacion.

        Args:
            plantacion: Plantacion donde plantar
            especie: Especie a plantar
            cantidad: Cantidad de cultivos

        Raises:
            SuperficieInsuficienteException: Si no hay superficie
        """
        cultivo_muestra = CultivoFactory.crear_cultivo(especie)
        superficie_requerida = cultivo_muestra.get_superficie() * cantidad

        superficie_ocupada = sum(
            c.get_superficie() for c in plantacion.get_cultivos()
        )
        superficie_disponible = plantacion.get_superficie() - superficie_ocupada

        if superficie_requerida > superficie_disponible:
            raise SuperficieInsuficienteException(
                superficie_requerida,
                superficie_disponible
            )

        for i in range(cantidad):
            cultivo = CultivoFactory.crear_cultivo(especie)
            plantacion.agregar_cultivo(cultivo)

    def regar(self, plantacion: Plantacion) -> None:
        """
        Riega todos los cultivos de la plantacion.

        Args:
            plantacion: Plantacion a regar

        Raises:
            AguaAgotadaException: Si no hay agua suficiente
        """
        agua_disponible = plantacion.get_agua_disponible()

        if agua_disponible < AGUA_MINIMA:
            raise AguaAgotadaException(AGUA_MINIMA, agua_disponible)

        plantacion.set_agua_disponible(
            agua_disponible - AGUA_CONSUMIDA_POR_RIEGO
        )

        for cultivo in plantacion.get_cultivos():
            self._registry.absorber_agua(cultivo)

    def fumigar(self, plantacion: Plantacion, plaguicida: str) -> None:
        """
        Fumiga la plantacion.

        Args:
            plantacion: Plantacion a fumigar
            plaguicida: Tipo de plaguicida
        """
        print(f"Fumigando plantacion con: {plaguicida}")

    def cosechar(
            self,
            plantacion: Plantacion,
            tipo_cultivo: Type[Cultivo]
    ) -> List[Cultivo]:
        """
        Cosecha cultivos de un tipo especifico.

        Args:
            plantacion: Plantacion donde cosechar
            tipo_cultivo: Tipo de cultivo a cosechar

        Returns:
            Lista de cultivos cosechados
        """
        cosechados = []
        cultivos = plantacion.get_cultivos()

        for cultivo in cultivos:
            if isinstance(cultivo, tipo_cultivo):
                cosechados.append(cultivo)
                plantacion.eliminar_cultivo(cultivo)

        return cosechados



# ================================================================================
# ARCHIVO 3/4: registro_forestal_service.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/terrenos/registro_forestal_service.py
# ================================================================================


# Standard library
import os
import pickle

# Local application
from python_forestacion.entidades.terrenos import RegistroForestal
from python_forestacion.excepciones import PersistenciaException
from python_forestacion.servicios.cultivos import CultivoServiceRegistry
from python_forestacion.constantes import (
    DIRECTORIO_DATA,
    EXTENSION_DATA,
    TipoOperacionPersistencia
)

class RegistroForestalService:
    """Servicio para operaciones sobre registros forestales."""

    def mostrar_datos(self, registro: RegistroForestal) -> None:
        """
        Muestra los datos completos de un registro.

        Args:
            registro: Registro a mostrar
        """
        print("\nREGISTRO FORESTAL")
        print("=================")
        print(f"Padron:      {registro.get_id_padron()}")
        print(f"Propietario: {registro.get_propietario()}")
        print(f"Avaluo:      {registro.get_avaluo()}")

        tierra = registro.get_tierra()
        print(f"Domicilio:   {tierra.get_domicilio()}")
        print(f"Superficie: {tierra.get_superficie()}")

        plantacion = registro.get_plantacion()
        cultivos = plantacion.get_cultivos()
        print(f"Cantidad de cultivos plantados: {len(cultivos)}")

        if cultivos:
            print("Listado de Cultivos plantados")
            print("____________________________\n")
            registry = CultivoServiceRegistry.get_instance()
            for cultivo in cultivos:
                registry.mostrar_datos(cultivo)
            print()

    def persistir(self, registro: RegistroForestal) -> None:
        """
        Persiste un registro en disco usando Pickle.

        Args:
            registro: Registro a persistir

        Raises:
            PersistenciaException: Si ocurre error al escribir
        """
        propietario = registro.get_propietario()
        nombre_archivo = f"{propietario}{EXTENSION_DATA}"
        ruta_completa = os.path.join(DIRECTORIO_DATA, nombre_archivo)

        os.makedirs(DIRECTORIO_DATA, exist_ok=True)

        archivo = None
        try:
            archivo = open(ruta_completa, 'wb')
            pickle.dump(registro, archivo)
            print(f"Registro de {propietario} persistido exitosamente en {ruta_completa}")
        except Exception as e:
            raise PersistenciaException(
                nombre_archivo,
                TipoOperacionPersistencia.ESCRITURA,
                e
            )
        finally:
            if archivo is not None:
                archivo.close()

    @staticmethod
    def leer_registro(propietario: str) -> RegistroForestal:
        """
        Lee un registro desde disco.

        Args:
            propietario: Nombre del propietario

        Returns:
            Registro leido

        Raises:
            ValueError: Si propietario es vacio
            PersistenciaException: Si ocurre error al leer
        """
        if not propietario or propietario.strip() == "":
            raise ValueError("El nombre del propietario no puede ser nulo o vacio")

        nombre_archivo = f"{propietario}{EXTENSION_DATA}"
        ruta_completa = os.path.join(DIRECTORIO_DATA, nombre_archivo)

        archivo = None
        try:
            archivo = open(ruta_completa, 'rb')
            registro = pickle.load(archivo)
            print(f"Registro de {propietario} recuperado exitosamente desde {ruta_completa}")
            return registro
        except FileNotFoundError as e:
            raise PersistenciaException(
                nombre_archivo,
                TipoOperacionPersistencia.LECTURA,
                e
            )
        except Exception as e:
            raise PersistenciaException(
                nombre_archivo,
                TipoOperacionPersistencia.LECTURA,
                e
            )
        finally:
            if archivo is not None:
                archivo.close()

# ================================================================================
# ARCHIVO 4/4: tierra_service.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/servicios/terrenos/tierra_service.py
# ================================================================================

# Local application
from python_forestacion.entidades.terrenos import Tierra, Plantacion
from python_forestacion.constantes import (
    AGUA_INICIAL_PLANTACION
)

class TierraService:
    """Servicio para operaciones sobre terrenos."""

    def crear_tierra_con_plantacion(
            self,
            id_padron_catastral: int,
            superficie: float,
            domicilio: str,
            nombre_plantacion: str
    ) -> Tierra:
        """
        Crea un terreno con su plantacion asociada.

        Args:
            id_padron_catastral: Padron catastral
            superficie: Superficie en m2
            domicilio: Domicilio del terreno
            nombre_plantacion: Nombre de la plantacion

        Returns:
            Terreno creado con plantacion asociada
        """
        tierra = Tierra(id_padron_catastral, superficie, domicilio)

        plantacion = Plantacion(
            nombre=nombre_plantacion,
            superficie=superficie,
            agua=AGUA_INICIAL_PLANTACION
        )

        tierra.set_finca(plantacion)
        return tierra



