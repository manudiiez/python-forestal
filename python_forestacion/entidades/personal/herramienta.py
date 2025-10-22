
class Herramienta:
    """
    Herramienta de trabajo.

    Attributes:
        id_herramienta: Identificador unico
        nombre: Nombre de la herramienta
        certificado_hys: Certificacion de higiene y seguridad
    """

    def __init__(self, id_herramienta: int, nombre: str, certificado_hys: bool):
        """
        Inicializa una herramienta.

        Args:
            id_herramienta: ID unico
            nombre: Nombre
            certificado_hys: Certificacion H&S
        """
        self._id_herramienta = id_herramienta
        self._nombre = nombre
        self._certificado_hys = certificado_hys

    def get_id_herramienta(self) -> int:
        """Obtiene el ID."""
        return self._id_herramienta

    def get_nombre(self) -> str:
        """Obtiene el nombre."""
        return self._nombre

    def tiene_certificado_hys(self) -> bool:
        """Verifica si tiene certificacion H&S."""
        return self._certificado_hys
