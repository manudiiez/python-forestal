
# Standard library
import time
from datetime import date

# Local application
from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService
from python_forestacion.servicios.personal.trabajador_service import TrabajadorService
from python_forestacion.servicios.negocio.fincas_service import FincasService
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.herramienta import Herramienta
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask
from python_forestacion.constantes import THREAD_JOIN_TIMEOUT


def main():
    """Funcion principal que demuestra todo el sistema."""

    print("=" * 70)
    print("         SISTEMA DE GESTION FORESTAL - PATRONES DE DISENO")
    print("=" * 70)
    print()

    # =========================================================================
    # PATRON SINGLETON: Verificar instancia unica
    # =========================================================================
    print("-" * 70)
    print("  PATRON SINGLETON: Inicializando servicios")
    print("-" * 70)

    registry1 = CultivoServiceRegistry.get_instance()
    registry2 = CultivoServiceRegistry()
    registry3 = CultivoServiceRegistry.get_instance()

    if registry1 is registry2 is registry3:
        print("[OK] Todos los servicios comparten la misma instancia del Registry")
    else:
        print("[ERROR] Las instancias no son iguales")

    print()

    # =========================================================================
    # CREACION DE TERRENO Y PLANTACION
    # =========================================================================
    print("1. Creando tierra con plantacion...")
    tierra_service = TierraService()
    terreno = tierra_service.crear_tierra_con_plantacion(
        id_padron_catastral=1,
        superficie=10000.0,
        domicilio="Agrelo, Mendoza",
        nombre_plantacion="Finca del Madero"
    )
    plantacion = terreno.get_finca()
    print(f"   Terreno creado: Padron {terreno.get_id_padron_catastral()}")
    print(f"   Plantacion: {plantacion.get_nombre()}")
    print(f"   Superficie disponible: {plantacion.get_superficie()} m2")
    print()

    # =========================================================================
    # PATRON FACTORY: Plantar cultivos
    # =========================================================================
    print("-" * 70)
    print("  PATRON FACTORY: Plantando cultivos")
    print("-" * 70)

    plantacion_service = PlantacionService()

    print("2. Plantando 5 Pinos (usa Factory Method)...")
    plantacion_service.plantar(plantacion, "Pino", 5)
    print("   [OK] 5 Pinos plantados")

    print("3. Plantando 5 Olivos (usa Factory Method)...")
    plantacion_service.plantar(plantacion, "Olivo", 5)
    print("   [OK] 5 Olivos plantados")

    print("4. Plantando 5 Lechugas (usa Factory Method)...")
    plantacion_service.plantar(plantacion, "Lechuga", 5)
    print("   [OK] 5 Lechugas plantadas")

    print("5. Plantando 5 Zanahorias (usa Factory Method)...")
    plantacion_service.plantar(plantacion, "Zanahoria", 5)
    print("   [OK] 5 Zanahorias plantadas")

    print(f"\n   Total cultivos plantados: {len(plantacion.get_cultivos())}")
    print()

    # =========================================================================
    # PATRON OBSERVER: Sistema de riego automatizado
    # =========================================================================
    print("-" * 70)
    print("  PATRON OBSERVER: Sistema de riego automatizado")
    print("-" * 70)

    print("6. Iniciando sensores y control de riego...")

    tarea_temp = TemperaturaReaderTask()
    tarea_hum = HumedadReaderTask()

    tarea_control = ControlRiegoTask(
        tarea_temp,
        tarea_hum,
        plantacion,
        plantacion_service
    )

    tarea_temp.start()
    tarea_hum.start()
    tarea_control.start()

    print("   [OK] Sensores iniciados (threads daemon)")
    print("   [OK] Control de riego activo")
    print("   Dejando funcionar el sistema por 20 segundos...")
    print()

    time.sleep(20)

    print("\n7. Deteniendo sistema de riego...")
    tarea_temp.detener()
    tarea_hum.detener()
    tarea_control.detener()

    tarea_temp.join(timeout=THREAD_JOIN_TIMEOUT)
    tarea_hum.join(timeout=THREAD_JOIN_TIMEOUT)
    tarea_control.join(timeout=THREAD_JOIN_TIMEOUT)

    print("   [OK] Sistema detenido correctamente")
    print()

    # =========================================================================
    # GESTION DE TRABAJADORES
    # =========================================================================
    print("-" * 70)
    print("  GESTION DE PERSONAL")
    print("-" * 70)

    print("8. Creando trabajador con tareas...")
    tareas = [
        Tarea(1, date.today(), "Desmalezar"),
        Tarea(2, date.today(), "Abonar"),
        Tarea(3, date.today(), "Marcar surcos")
    ]

    trabajador = Trabajador(43888734, "Juan Perez", tareas)
    plantacion.set_trabajadores([trabajador])
    print(f"   Trabajador: {trabajador.get_nombre()}")
    print(f"   Tareas asignadas: {len(trabajador.get_tareas())}")
    print()

    print("9. Asignando apto medico...")
    trabajador_service = TrabajadorService()
    trabajador_service.asignar_apto_medico(
        trabajador,
        apto=True,
        fecha_emision=date.today(),
        observaciones="Estado de salud: excelente"
    )
    print("   [OK] Apto medico asignado")
    print()

    print("10. Ejecutando tareas del trabajador...")
    herramienta = Herramienta(1, "Pala", True)
    resultado = trabajador_service.trabajar(trabajador, date.today(), herramienta)

    if resultado:
        print("   [OK] Tareas ejecutadas exitosamente")
    else:
        print("   [ERROR] No pudo trabajar")
    print()

    # =========================================================================
    # OPERACIONES DE NEGOCIO
    # =========================================================================
    print("-" * 70)
    print("  OPERACIONES DE NEGOCIO")
    print("-" * 70)

    print("11. Creando registro forestal...")
    registro = RegistroForestal(
        id_padron=1,
        tierra=terreno,
        plantacion=plantacion,
        propietario="Juan Perez",
        avaluo=50309233.55
    )
    print("   [OK] Registro creado")
    print()

    print("12. Agregando finca al servicio de gestion...")
    fincas_service = FincasService()
    fincas_service.add_finca(registro)
    print("   [OK] Finca agregada")
    print()

    print("13. Fumigando plantacion...")
    fincas_service.fumigar(1, "insecto organico")
    print()

    print("14. Cosechando y empaquetando cultivos...")
    print("\n   Cosechando Lechugas:")
    caja_lechugas = fincas_service.cosechar_yempaquetar(Lechuga)
    caja_lechugas.mostrar_contenido_caja()

    print("\n   Cosechando Pinos:")
    caja_pinos = fincas_service.cosechar_yempaquetar(Pino)
    caja_pinos.mostrar_contenido_caja()
    print()

    # =========================================================================
    # PERSISTENCIA
    # =========================================================================
    print("-" * 70)
    print("  PERSISTENCIA DE DATOS")
    print("-" * 70)

    print("15. Persistiendo registro forestal...")
    registro_service = RegistroForestalService()
    registro_service.persistir(registro)
    print()

    print("16. Recuperando registro desde disco...")
    registro_leido = RegistroForestalService.leer_registro("Juan Perez")
    print()

    print("17. Mostrando datos del registro recuperado...")
    registro_service.mostrar_datos(registro_leido)
    print()

    # =========================================================================
    # RESUMEN FINAL
    # =========================================================================
    print("=" * 70)
    print("              EJEMPLO COMPLETADO EXITOSAMENTE")
    print("=" * 70)
    print("  [OK] SINGLETON   - CultivoServiceRegistry (instancia unica)")
    print("  [OK] FACTORY     - Creacion de cultivos")
    print("  [OK] OBSERVER    - Sistema de sensores y eventos")
    print("  [OK] STRATEGY    - Algoritmos de absorcion de agua")
    print("=" * 70)


if __name__ == "__main__":
    main()