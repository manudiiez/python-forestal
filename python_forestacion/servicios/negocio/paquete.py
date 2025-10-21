
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

