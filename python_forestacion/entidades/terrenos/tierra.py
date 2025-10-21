
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