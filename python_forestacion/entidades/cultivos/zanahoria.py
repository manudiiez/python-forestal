# Local application
from python_forestacion.constantes import AGUA_INICIAL_ZANAHORIA, SUPERFICIE_ZANAHORIA
from python_forestacion.entidades.cultivos.hortaliza import Hortaliza


class Zanahoria(Hortaliza):
    """
    Cultivo: Zanahoria.

    Hortaliza de raiz cultivada a campo abierto.
    """

    def __init__(self, es_baby_carrot: bool):
        """
        Inicializa una zanahoria.

        Args:
            es_baby_carrot: True si es baby carrot
        """
        super().__init__(
            agua=AGUA_INICIAL_ZANAHORIA,
            superficie=SUPERFICIE_ZANAHORIA,
            invernadero=False
        )
        self._es_baby_carrot = es_baby_carrot

    def is_baby_carrot(self) -> bool:
        """Verifica si es baby carrot."""
        return self._es_baby_carrot

    def set_baby_carrot(self, es_baby_carrot: bool) -> None:
        """Establece si es baby carrot."""
        self._es_baby_carrot = es_baby_carrot