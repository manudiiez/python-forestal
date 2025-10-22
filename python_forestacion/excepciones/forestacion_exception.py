"""
Excepcion base del sistema de gestion forestal.

Todas las excepciones especificas del dominio heredan de esta clase.
"""


class ForestacionException(Exception):
    """
    Excepcion base para el sistema de gestion forestal.

    Proporciona mensajes separados para usuarios y tecnicos,
    permitiendo manejar errores de forma contextualizada.

    Args:
        mensaje_usuario: Mensaje legible para el usuario final
        mensaje_tecnico: Mensaje tecnico con detalles del error
        causa: Excepcion original que causo este error (opcional)
    """

    def __init__(
            self,
            mensaje_usuario: str,
            mensaje_tecnico: str,
            causa: Exception = None
    ):
        self._mensaje_usuario = mensaje_usuario
        self._mensaje_tecnico = mensaje_tecnico
        self._causa = causa
        super().__init__(mensaje_tecnico)

    def get_user_message(self) -> str:
        """
        Obtiene el mensaje para el usuario final.

        Returns:
            Mensaje legible para usuarios no tecnicos
        """
        return self._mensaje_usuario

    def get_technical_message(self) -> str:
        """
        Obtiene el mensaje tecnico detallado.

        Returns:
            Mensaje con detalles tecnicos del error
        """
        return self._mensaje_tecnico

    def get_causa(self) -> Exception:
        """
        Obtiene la excepcion original que causo este error.

        Returns:
            Excepcion original o None si no hay causa
        """
        return self._causa

    def get_full_message(self) -> str:
        """
        Obtiene el mensaje completo combinando ambos mensajes.

        Returns:
            Mensaje completo con informacion de usuario y tecnica
        """
        mensaje = f"[USUARIO] {self._mensaje_usuario}\n"
        mensaje += f"[TECNICO] {self._mensaje_tecnico}"
        if self._causa:
            mensaje += f"\n[CAUSA] {str(self._causa)}"
        return mensaje