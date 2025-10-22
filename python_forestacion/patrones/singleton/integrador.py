"""
Archivo integrador generado automaticamente
Directorio: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/singleton
Fecha: 2025-10-21 21:39:45
Total de archivos integrados: 1
"""

# ================================================================================
# ARCHIVO 1/1: __init__.py
# Ruta: /Users/manudiiez/Desktop/Mis Carpetas/Facultad/Diseño de sistemas/ParcialForestal/python-forestal/python_forestacion/patrones/singleton/__init__.py
# ================================================================================

"""
============================================================================
PATRÓN SINGLETON - Package
============================================================================

Este paquete reexporta el patrón Singleton aplicado al CultivoServiceRegistry.

El patrón Singleton garantiza que una clase tenga solo una instancia única
y proporciona un punto de acceso global a ella.

La implementación real está en servicios/cultivos/cultivo_service_registry.py
Este paquete solo sirve para demostrar el patrón educativamente.

Uso:
    from python_forestacion.patrones.singleton import CultivoServiceRegistry

    # Primera instancia
    registry1 = CultivoServiceRegistry()

    # Segunda instancia (reutiliza la primera)
    registry2 = CultivoServiceRegistry()

    # Son la misma instancia
    assert registry1 is registry2  # True
"""

# Reexportar desde la implementación de producción
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry

__all__ = ['CultivoServiceRegistry']

