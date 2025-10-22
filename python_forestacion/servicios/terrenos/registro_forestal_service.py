
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