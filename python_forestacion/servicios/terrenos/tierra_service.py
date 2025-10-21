
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

