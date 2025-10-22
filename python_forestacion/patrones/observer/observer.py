"""
Patron Observer con soporte para Generics.

Este modulo implementa el patron Observer de forma tipo-segura
utilizando Generic[T] de Python.
"""

# Standard library
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List

T = TypeVar('T')

class Observer(Generic[T], ABC):
    """
    Interfaz Observer generica.

    Los observadores deben implementar el metodo actualizar()
    para recibir notificaciones de eventos.

    Type Parameters:
        T: Tipo de evento que el observador puede manejar
    """

    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """
        Metodo llamado cuando ocurre un evento observable.

        Args:
            evento: Evento que ocurrio
        """
        pass

