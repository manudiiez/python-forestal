"""
Archivo integrador generado automaticamente
Directorio: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/observer
Fecha: 2025-10-21 21:39:45
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/observer/__init__.py
# ================================================================================

"""Patron Observer."""

from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.patrones.observer.observer import Observer

__all__ = ['Observable', 'Observer']


# ================================================================================
# ARCHIVO 2/3: observable.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/observer/observable.py
# ================================================================================

from python_forestacion.patrones.observer.observer import Observer
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

# ================================================================================
# ARCHIVO 3/3: observer.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/observer/observer.py
# ================================================================================

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



