from python_forestacion.entidades.cultivos.cultivo import Cultivo

class Arbol(Cultivo):
    """
    Clase base para cultivos arboreos.

    Los arboles tienen una altura que crece con el tiempo.

    Atributos adicionales:
        altura: Altura del arbol en metros
    """

    def __init__(self, agua: int, superficie: float, altura: float):
        """
        Inicializa un arbol.

        Args:
            agua: Agua inicial en litros
            superficie: Superficie en metros cuadrados
            altura: Altura inicial en metros
        """
        super().__init__(agua, superficie)
        self._altura = altura

    def get_altura(self) -> float:
        """Obtiene la altura del arbol."""
        return self._altura

    def set_altura(self, altura: float) -> None:
        """Establece la altura del arbol."""
        self._altura = altura
