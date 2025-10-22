"""
Archivo integrador generado automaticamente
Directorio: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/factory
Fecha: 2025-10-22 10:13:59
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/factory/__init__.py
# ================================================================================

"""Patron Factory Method."""

from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory

__all__ = ['CultivoFactory']

# ================================================================================
# ARCHIVO 2/2: cultivo_factory.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/factory/cultivo_factory.py
# ================================================================================


# Local application
from python_forestacion.entidades.cultivos import Cultivo, Pino, Olivo, Lechuga, Zanahoria, TipoAceituna


class CultivoFactory:
    """
    Factory para crear cultivos.

    Proporciona un punto centralizado para la creacion
    de todos los tipos de cultivos del sistema.
    """

    @staticmethod
    def crear_cultivo(especie: str) -> Cultivo:
        """
        Crea un cultivo segun la especie especificada.

        Args:
            especie: Nombre de la especie (Pino, Olivo, Lechuga, Zanahoria)

        Returns:
            Instancia del cultivo creado

        Raises:
            ValueError: Si la especie es desconocida
        """
        factories = {
            "Pino": CultivoFactory._crear_pino,
            "Olivo": CultivoFactory._crear_olivo,
            "Lechuga": CultivoFactory._crear_lechuga,
            "Zanahoria": CultivoFactory._crear_zanahoria
        }

        if especie not in factories:
            raise ValueError(f"Especie desconocida: {especie}")

        return factories[especie]()

    @staticmethod
    def _crear_pino() -> Cultivo:
        """
        Crea un Pino con valores por defecto.

        Returns:
            Instancia de Pino
        """
        return Pino(variedad="Parana")

    @staticmethod
    def _crear_olivo() -> Cultivo:
        """
        Crea un Olivo con valores por defecto.

        Returns:
            Instancia de Olivo
        """
        return Olivo(tipo_aceituna=TipoAceituna.ARBEQUINA)

    @staticmethod
    def _crear_lechuga() -> Cultivo:
        """
        Crea una Lechuga con valores por defecto.

        Returns:
            Instancia de Lechuga
        """
        return Lechuga(variedad="Crespa")

    @staticmethod
    def _crear_zanahoria() -> Cultivo:
        """
        Crea una Zanahoria con valores por defecto.

        Returns:
            Instancia de Zanahoria
        """
        return Zanahoria(es_baby_carrot=False)

