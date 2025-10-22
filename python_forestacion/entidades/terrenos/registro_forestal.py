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
