# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

PythonForestal is a forestry management system built with Python 3.13 that demonstrates multiple design patterns. The system manages crops, workers, irrigation, and land records with an educational focus on software architecture patterns.

## Development Environment

- **Python Version**: 3.13
- **Virtual Environment**: Located in `.venv/` directory
- **IDE**: PyCharm/IntelliJ IDEA configuration present
- **Package Name**: `python_forestacion`

## Running the Application

Activate the virtual environment first:
- Windows: `.venv\Scripts\activate`
- Unix/MacOS: `source .venv/bin/activate`

Run the main demonstration:
```bash
python main.py
```

The main.py file orchestrates a complete demonstration of all design patterns and system features including crop creation, automated irrigation, worker management, and data persistence.

## Architecture Overview

### Core Design Patterns

The codebase demonstrates four major design patterns:

1. **SINGLETON** - `CultivoServiceRegistry` ensures a single registry instance managing all crop services
    - **Implementation**: `python_forestacion/servicios/cultivos/cultivo_service_registry.py`
    - **Educational reference**: `python_forestacion/patrones/singleton/` (reexports the production version)
    - Thread-safe implementation using `__new__` with double-checked locking
    - Registry pattern eliminates isinstance chains
    - **IMPORTANT**: Always access via `CultivoServiceRegistry.get_instance()` or direct instantiation
    - DO NOT store the singleton as an instance variable to avoid multiple references

2. **FACTORY METHOD** - `CultivoFactory` creates different crop types
    - **Location**: `python_forestacion/patrones/factory/cultivo_factory.py`
    - Centralized factory for all crop creation (Pino, Olivo, Lechuga, Zanahoria)
    - **IMPORTANT**: Use `CultivoFactory.crear_cultivo(especie)` instead of direct instantiation
    - Services like `PlantacionService` delegate to this factory
    - Supports both standard and customized crop creation

3. **OBSERVER** - Sensor and irrigation monitoring system
    - Location: `python_forestacion/patrones/observer/`
    - Base classes: `Observable[T]` and `Observer[T]` with Generic type parameters
    - **IMPLEMENTED**: `TemperaturaReaderTask` and `HumedadReaderTask` inherit from `Observable[float]`
    - Sensors emit events by calling `notificar_observadores()` after each reading
    - `ControlRiegoTask` can observe sensors and trigger irrigation automatically
    - Uses Generic types for type-safe event handling
    - Multiple inheritance pattern: `class SensorTask(threading.Thread, Observable[float])`

4. **STRATEGY** - Interchangeable water absorption algorithms
    - Location: `python_forestacion/patrones/strategy/`
    - `AbsorcionSeasonalStrategy` - Trees (Pino, Olivo) with seasonal variation (uses constants from constantes.py)
    - `AbsorcionConstanteStrategy` - Vegetables (Lechuga, Zanahoria) with constant absorption
    - **IMPLEMENTED**: Strategies are properly injected into crop services via constructor
    - Each service (PinoService, OlivoService, LechugaService, ZanahoriaService) initializes its strategy in `__init__()`
    - All `absorver_agua()` methods delegate to `strategy.calcular_absorcion()`

### Package Structure

```
python_forestacion/
├── entidades/          # Domain entities
│   ├── cultivos/       # Crops (Pino, Olivo, Lechuga, Zanahoria)
│   ├── terrenos/       # Land (Tierra, Plantacion, RegistroForestal)
│   └── personal/       # Workers, tools, tasks
├── servicios/          # Business logic layer
│   ├── cultivos/       # Crop-specific services
│   ├── terrenos/       # Land management services
│   ├── personal/       # Worker management services
│   └── negocio/        # High-level business services (FincasService)
├── patrones/           # Design pattern implementations
│   ├── singleton/      # Singleton metaclass
│   ├── factory/        # Factory method
│   ├── observer/       # Observer pattern with events
│   └── strategy/       # Strategy implementations
├── riego/              # Irrigation system
│   ├── sensores/       # Temperature and humidity reader tasks
│   └── control/        # Automated irrigation control
├── excepciones/        # Custom exceptions hierarchy
└── data/               # Persistence directory
```

### Key Architectural Decisions

1. **Service Layer Pattern**: Business logic is separated from entities in dedicated service classes
    - Entities are pure data containers (DTOs) with getters/setters
    - Services contain all business logic and orchestration
    - Example: `PlantacionService` manages planting, irrigation, and harvesting

2. **Thread-based Sensors**: Irrigation system uses daemon threads for real-time monitoring
    - Sensors run as daemon threads (automatically terminated when main exits)
    - Thread-safe with `threading.Event` for graceful shutdown
    - Dependency injection: `ControlRiegoTask` receives sensor tasks and services

3. **Type Safety**: Uses TYPE_CHECKING guards and Generic types for better IDE support
    - `TYPE_CHECKING` avoids circular imports while preserving type hints
    - Generic types used in Observer pattern and Paquete class
    - Forward references with string literals for type annotations

4. **Centralized Constants**: All system constants in `python_forestacion/constantes.py`
    - UPPER_CASE naming convention for all constants
    - Grouped by domain (AGUA, RIEGO, SENSORES, CULTIVOS, etc.)
    - **IMPORTANT**: Never hardcode magic numbers - always use constants

5. **Custom Exception Hierarchy**: Domain-specific exceptions extending `ForestacionException`
    - Structured exception messages with user/technical separation
    - Context-specific exceptions (SuperficieInsuficienteException, AguaAgotadaException)
    - Proper exception handling demonstrated in main.py

6. **Encoding Considerations** (CRITICAL for Windows):
    - **NO emojis in print statements** (Windows charmap encoding issues)
    - **NO Unicode box-drawing characters** (`├─`, `└─`, `│`, etc.) - causes UnicodeEncodeError
    - Use ASCII characters only: `[OK]`, `[!]`, `[INFO]`, `[+]` instead of Unicode symbols
    - Windows console uses cp1252/charmap by default which doesn't support extended Unicode
    - Spanish characters with tildes (á, é, í, ó, ú, ñ) in strings should be avoided in print statements when possible
    - **TESTED**: The system runs successfully on Windows with ASCII-only console output

### Constants Configuration

All system constants are centralized in `constantes.py`:
- Water thresholds (AGUA_MINIMA, AGUA_INICIAL_PLANTACION)
- Irrigation triggers (TEMP_MIN_RIEGO, TEMP_MAX_RIEGO, HUMEDAD_MAX_RIEGO)
- Sensor intervals (INTERVALO_SENSOR_TEMPERATURA, INTERVALO_SENSOR_HUMEDAD)
- Crop-specific values (surface area, initial water, absorption rates)
- **Strategy pattern constants**: ABSORCION_SEASONAL_VERANO, ABSORCION_SEASONAL_INVIERNO, MES_INICIO_VERANO, MES_FIN_VERANO, ABSORCION_CONSTANTE_DEFAULT
- Persistence configuration (DIRECTORIO_DATA, EXTENSION_DATA)

### Exception Handling

The system uses a three-tier exception hierarchy:
- `ForestacionException` - Base exception with user/technical messages
- `SuperficieInsuficienteException` - Insufficient land area
- `AguaAgotadaException` - Water depleted
- `PersistenciaException` - Data persistence errors

Main.py demonstrates proper exception handling for each type.

### Threading Model

The irrigation system runs three daemon threads:
- `TemperaturaReaderTask` - Reads temperature every 2 seconds
- `HumedadReaderTask` - Reads humidity every 3 seconds
- `ControlRiegoTask` - Observes sensors and triggers irrigation every 2.5 seconds

All threads support graceful shutdown with configurable timeout (THREAD_JOIN_TIMEOUT).

## Design Pattern Best Practices

### When Adding New Crop Types

1. **Add constants first** in `constantes.py`:
   ```python
   # Add to appropriate section
   SUPERFICIE_NUEVO_CULTIVO = 1.5
   AGUA_INICIAL_NUEVO_CULTIVO = 3
   ```

2. **Create the entity class** in `python_forestacion/entidades/cultivos/`:
   ```python
   from python_forestacion.entidades.cultivos.arbol import Arbol  # or Hortaliza
   from python_forestacion.constantes import (
       AGUA_INICIAL_NUEVO_CULTIVO,
       ALTURA_INICIAL_ARBOL,  # if tree
       SUPERFICIE_NUEVO_CULTIVO
   )

   class NuevoCultivo(Arbol):  # or Hortaliza
       """
       Entidad NuevoCultivo - solo contiene datos/estado.
       La lógica de comportamiento está en NuevoCultivoService.
       """

       def __init__(self, atributo_especifico: str):
           super().__init__(
               agua=AGUA_INICIAL_NUEVO_CULTIVO,
               altura=ALTURA_INICIAL_ARBOL,  # if tree
               superficie=SUPERFICIE_NUEVO_CULTIVO
           )
           self._atributo_especifico = atributo_especifico

       def get_atributo_especifico(self) -> str:
           return self._atributo_especifico

       def set_atributo_especifico(self, valor: str) -> None:
           """
           Establece el atributo específico.

           Args:
               valor: Nuevo valor del atributo
           """
           self._atributo_especifico = valor
   ```

3. **Create the service class** in `python_forestacion/servicios/cultivos/`:
   ```python
   from python_forestacion.servicios.cultivos.arbol_service import ArbolService  # or CultivoService
   from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy

   class NuevoCultivoService(ArbolService):  # or CultivoService
       """
       Servicio para operaciones específicas de NuevoCultivo.
       """

       def __init__(self):
           # Trees: AbsorcionSeasonalStrategy()
           # Vegetables: AbsorcionConstanteStrategy(cantidad_constante=X)
           super().__init__(AbsorcionSeasonalStrategy())

       def consumir_agua(self, cultivo: 'NuevoCultivo') -> int:
           """Implementar lógica específica"""
           pass

       def mostrar_datos(self, cultivo: 'NuevoCultivo') -> None:
           """Implementar visualización específica"""
           pass
   ```

4. **Register in CultivoServiceRegistry** (`servicios/cultivos/cultivo_service_registry.py`):
    - Add service instantiation in `__init__`:
      ```python
      self._nuevo_cultivo_service = NuevoCultivoService()
      ```
    - Add handler methods:
      ```python
      def _absorber_agua_nuevo_cultivo(self, cultivo):
          return self._nuevo_cultivo_service.absorver_agua(cultivo)
 
      def _mostrar_datos_nuevo_cultivo(self, cultivo):
          return self._nuevo_cultivo_service.mostrar_datos(cultivo)
      ```
    - Register in dictionaries:
      ```python
      from python_forestacion.entidades.cultivos.nuevo_cultivo import NuevoCultivo
      self._absorber_agua_handlers[NuevoCultivo] = self._absorber_agua_nuevo_cultivo
      self._mostrar_datos_handlers[NuevoCultivo] = self._mostrar_datos_nuevo_cultivo
      ```

5. **Register in CultivoFactory** (`patrones/factory/cultivo_factory.py`):
    - Add static factory method:
      ```python
      @staticmethod
      def _crear_nuevo_cultivo() -> NuevoCultivo:
          from python_forestacion.entidades.cultivos.nuevo_cultivo import NuevoCultivo
          return NuevoCultivo(atributo_especifico="valor_default")
      ```
    - Add to factories dictionary:
      ```python
      factories["NuevoCultivo"] = CultivoFactory._crear_nuevo_cultivo
      ```

### When Modifying Services

- **DO**: Access Singleton via `CultivoServiceRegistry.get_instance()` when needed
- **DON'T**: Store singleton as instance variable (`self._registry`)
- **DO**: Use dependency injection for service collaborators
- **DON'T**: Create services inside business logic - inject them via constructor
- **DO**: Keep services stateless (except for registries and configuration)
- **DON'T**: Mix business logic with data (entities should be pure DTOs)

### When Working with Threads

- Always use daemon threads for background tasks (`daemon=True`)
- Implement graceful shutdown with `threading.Event`
- Use configurable timeouts from `constantes.py`
- Join threads with timeout: `thread.join(timeout=THREAD_JOIN_TIMEOUT)`

### Code Quality Guidelines

- No emojis in print statements (encoding issues on Windows)
- All constants must be UPPER_CASE in `constantes.py`
- Use TYPE_CHECKING for import type hints to avoid circular dependencies
- Prefer composition over inheritance
- Follow Single Responsibility Principle (one service = one domain concept)
- **NO lambda functions**: Always use named methods or functions instead of lambda
    - For sort keys: create static methods (e.g., `_obtener_id_tarea`)
    - For factory patterns: create dedicated methods (e.g., `_crear_pino`)
    - For handlers/callbacks: create instance methods (e.g., `_absorber_agua_pino`)
    - Exception: Simple built-in operations like `map()` or `filter()` with trivial lambdas MAY be acceptable

## Service Class Hierarchy

The codebase uses inheritance to eliminate code duplication in services:

### Base Classes
- **`CultivoService`** (`python_forestacion/servicios/cultivos/cultivo_service.py`)
    - Abstract base class for all crop services
    - Provides common `absorver_agua()` method that delegates to injected Strategy
    - Constructor accepts `AbsorcionAguaStrategy` for dependency injection
    - All crop services inherit from this base

- **`ArbolService`** (extends `CultivoService`)
    - Intermediate class for tree-specific services (Pino, Olivo)
    - Adds tree-specific method `crecer(arbol, incremento)`
    - Constructor passes strategy to parent `CultivoService.__init__()`

### Inheritance Chain
```
CultivoService (ABC)
    ├── ArbolService
    │   ├── PinoService
    │   └── OlivoService
    └── LechugaService / ZanahoriaService (direct inheritance)
```

**IMPORTANT**: When creating new crop services:
- Inherit from `CultivoService` (vegetables) or `ArbolService` (trees)
- DO NOT override `absorver_agua()` - it's handled by the base class
- Inject the appropriate Strategy in `__init__()` via `super().__init__(strategy)`

## Code Style Standards (PEP 8 Compliance)

This codebase adheres strictly to PEP 8. When contributing:

### Naming Conventions
- **Parameters**: Use descriptive full names, NOT abbreviations
    - ✅ `def __init__(self, agua: int, altura: float, superficie: float)`
    - ❌ `def __init__(self, agua: int, alt: float, sup: float)`
- **Constants**: UPPER_CASE in `constantes.py`
- **Private attributes**: Prefix with underscore `_nombre`
- **Methods**: snake_case

### Docstring Format
- **REQUIRED**: Use Google Style docstrings (NOT JavaDoc @param/@return)
  ```python
  def method(self, param: str) -> int:
      """
      Brief description.

      Args:
          param: Description of parameter

      Returns:
          Description of return value

      Raises:
          ValueError: When validation fails
      """
  ```

### Import Organization (PEP 8)
Group imports in this order with blank lines between groups:
```python
# Standard library
import os
from datetime import datetime
from typing import TYPE_CHECKING

# Third-party
# (none currently)

# Local application
from python_forestacion.constantes import AGUA_MINIMA
```

### Entity Constructor Pattern
All entity constructors MUST use constants from `constantes.py`:
```python
# CORRECT
from python_forestacion.constantes import (
    AGUA_INICIAL_PINO,
    ALTURA_INICIAL_ARBOL,
    SUPERFICIE_PINO
)

def __init__(self, variedad: str):
    super().__init__(
        agua=AGUA_INICIAL_PINO,
        altura=ALTURA_INICIAL_ARBOL,
        superficie=SUPERFICIE_PINO
    )
```

```python
# INCORRECT - Hardcoded values
def __init__(self, variedad: str):
    super().__init__(agua=2, altura=1.0, superficie=2.0)  # ❌ NO
```

### Getter/Setter Consistency
All entities MUST provide both getters AND setters for mutable attributes:
```python
class Cultivo:
    def get_variedad(self) -> str:
        return self._variedad

    def set_variedad(self, variedad: str) -> None:
        """
        Establece la variedad del cultivo.

        Args:
            variedad: Nueva variedad
        """
        self._variedad = variedad
```

## Recent Refactorings (October 2025)

The following improvements have been completed:

1. **Strategy Pattern Implementation**: All crop services now properly inject and use Strategy objects
    - `PinoService` and `OlivoService` use `AbsorcionSeasonalStrategy`
    - `LechugaService` uses `AbsorcionConstanteStrategy(1)`
    - `ZanahoriaService` uses `AbsorcionConstanteStrategy(2)`
    - All services delegate to `_estrategia_absorcion.calcular_absorcion()` in `absorver_agua()`

2. **Service Inheritance Hierarchy**: Created base classes to eliminate code duplication
    - `CultivoService` base class with common `absorver_agua()` implementation
    - `ArbolService` intermediate class for tree-specific logic (`crecer()` method)
    - Eliminated ~70 lines of duplicated code across 4 service classes
    - All services now inherit shared behavior while maintaining specific implementations
    - **IMPORTANT**: New crop services MUST inherit from appropriate base class

3. **Magic Numbers Eliminated**: All hardcoded values moved to `constantes.py`
    - ALL entity constructors now use constants (AGUA_INICIAL_*, SUPERFICIE_*, ALTURA_INICIAL_*)
    - Seasonal absorption values (5L summer, 2L winter)
    - Month ranges for seasons (3-8 for summer)
    - Growth increments (INCREMENTO_ALTURA_PINO, INCREMENTO_ALTURA_OLIVO)
    - **Zero tolerance for magic numbers** - 100% constants usage

4. **PEP 8 Compliance Achieved**: Complete code style standardization
    - All parameter names expanded (no abbreviations: `altura` not `alt`, `superficie` not `sup`)
    - All docstrings converted to Google Style (removed JavaDoc @param/@return)
    - All imports organized according to PEP 8 (Standard → Third-party → Local)
    - All entities have complete getter/setter pairs
    - 100% PEP 8 compliance verified

5. **Observer Pattern Completion**: Sensors now properly implement Observable
    - `TemperaturaReaderTask(threading.Thread, Observable[float])`
    - `HumedadReaderTask(threading.Thread, Observable[float])`
    - Both sensors call `notificar_observadores()` after each reading
    - Multiple inheritance initialization: explicit `threading.Thread.__init__()` and `Observable.__init__()`

6. **ID Generation**: Kept in entity classes (Arbol) as it's lifecycle management, not business logic
    - Thread-safe with Lock
    - Acceptable pattern for entities managing their own identifiers

7. **Lambda Functions Eliminated**: All lambda functions replaced with named methods/functions
    - `trabajador_service.py`: Lambda in sort() replaced with static method `_obtener_id_tarea()`
    - `cultivo_factory.py`: Complex lambdas replaced with dedicated static methods (`_crear_pino()`, `_crear_olivo()`, etc.)
    - `cultivo_service_registry.py`: Handler lambdas replaced with instance methods (`_absorber_agua_pino()`, `_mostrar_datos_pino()`, etc.)
    - **Benefits**: Better debugging, clearer stack traces, improved testability, and self-documenting code
    - **IMPORTANT**: Do NOT use lambda functions in this codebase - always create named functions/methods

8. **Code Quality Improvements**: Multiple consistency fixes
    - Removed unused strategy base classes (ConsumoAguaStrategy, DecisionRiegoStrategy)
    - Normalized field access modifiers (all private with getters: `_id`, `_dni`)
    - Added input validation to all setters (negative checks, zero checks)
    - Fixed type hints (`Optional[int]` for nullable fields)
    - **110 lines of dead code removed**

9. **Syntax Error Prevention** (October 2025):
    - Fixed: Stray `/` character at end of `observable.py` caused SyntaxError during imports
    - Fixed: Unicode box-drawing characters in `cultivo_factory.py` prints caused UnicodeEncodeError
    - **Validation**: Always test imports and print statements on Windows before committing
    - **Best Practice**: Use ASCII-only characters in all console output (see Encoding Considerations above)

## Common Issues and Solutions

### Import Errors
- **Symptom**: `SyntaxError: invalid syntax` on module import
- **Cause**: Stray characters at end of Python files (e.g., `/`, `\`, incomplete statements)
- **Solution**: Check file endings - ensure they end cleanly after last statement

### UnicodeEncodeError on Windows
- **Symptom**: `'charmap' codec can't encode characters` when running on Windows
- **Cause**: Unicode characters in print/output statements incompatible with Windows console (cp1252)
- **Solution**: Replace with ASCII equivalents:
    - ✅ `[+]`, `[OK]`, `[!]`, `[INFO]`
    - ❌ `├─`, `└─`, `│`, emojis, extended Unicode
- **Quick Test**: `python -c "print('├─ Test')"`  will fail on Windows

### Threading Issues
- **Symptom**: Program doesn't exit cleanly or hangs
- **Cause**: Non-daemon threads or missing Event-based shutdown
- **Solution**:
    - Set `daemon=True` on all background threads
    - Use `threading.Event()` for graceful shutdown
    - Always call `thread.join(timeout=THREAD_JOIN_TIMEOUT)`