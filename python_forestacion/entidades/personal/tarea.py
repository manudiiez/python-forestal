from datetime import date

class Tarea:
    """
    Tarea asignada a un trabajador.

    Attributes:
        id_tarea: Identificador unico
        fecha: Fecha programada
        descripcion: Descripcion de la tarea
    """

    def __init__(self, id_tarea: int, fecha: date, descripcion: str):
        """
        Inicializa una tarea.

        Args:
            id_tarea: ID unico
            fecha: Fecha programada
            descripcion: Descripcion
        """
        self._id_tarea = id_tarea
        self._fecha = fecha
        self._descripcion = descripcion

    def get_id_tarea(self) -> int:
        """Obtiene el ID de la tarea."""
        return self._id_tarea

    def get_fecha(self) -> date:
        """Obtiene la fecha."""
        return self._fecha

    def get_descripcion(self) -> str:
        """Obtiene la descripcion."""
        return self._descripcion
