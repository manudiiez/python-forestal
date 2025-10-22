# Local application
from python_forestacion.patrones.observer.observer import Observer

# Standard library
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List

T = TypeVar('T')

class Observable(Generic[T], ABC):
    """
    Clase Observable generica.

    Los objetos observables mantienen una lista de observadores
    y los notifican cuando ocurren eventos.

    Type Parameters:
        T: Tipo de evento que el observable puede emitir
    """

    def __init__(self):
        """Inicializa la lista de observadores."""
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        """
        Agrega un observador a la lista.

        Args:
            observador: Observador a agregar
        """
        if observador not in self._observadores:
            self._observadores.append(observador)

    def eliminar_observador(self, observador: Observer[T]) -> None:
        """
        Elimina un observador de la lista.

        Args:
            observador: Observador a eliminar
        """
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notificar_observadores(self, evento: T) -> None:
        """
        Notifica a todos los observadores sobre un evento.

        Args:
            evento: Evento a notificar
        """
        for observador in self._observadores:
            observador.actualizar(evento)