# Agent Report

## Agent / Version
**Agente:** Antigravity  
**Modelo:** Gemini 3.1 Pro (High)

## Initial Context
El objetivo inicial consistía en implementar una herramienta de Interfaz de Línea de Comandos (CLI) local en Python para la búsqueda de clientes, persistida en un archivo JSON. El desarrollo debía seguir estrictamente la metodología SDD (Spec-Driven Development), basándose en requisitos previamente definidos y limitando la implementación exclusivamente a lo dictado en los archivos md. 

## Task Sequence

### T-01 Configuración del proyecto
**What the agent did:** El agente creó la estructura básica de directorios (`src/`, `tests/`) y el archivo `pytest.ini` para configurar el framework de pruebas. Adicionalmente, el agente creó de manera prematura el directorio `data/` adelantándose a las instrucciones de esta tarea específica. Se implementó una prueba rapida para asegurar que `pytest` corriera sin errores estructurales.
**Human review:** Se detectó que el agente se adelantó al crear el directorio `data/` y le llamó la atención porque creyó haberse adelantado a la tarea 2 de modelado de datos.
**Tests:** La prueba de entorno (`test_environment.py`) pasó con éxito.

### T-02 Modelo de dominio
**What the agent did:** El agente acató la corrección humana y se apegó estrictamente a la tarea. Creó el modelo `Customer` usando `dataclasses`, implementó el script `storage.py` con las reglas de validación estructural para archivos JSON corruptos o inexistentes, y generó el archivo de datos base `data/customers.json`. Adicionalmente incluyó pruebas automatizadas para el almacenamiento.
**Human review:** Se solicitó continuar con el flujo, cuestionando al agente sobre su terminología al catalogar la siguiente tarea como "incompleta" (lo cual el agente aclaró que era una simple traducción de "pendiente").
**Tests:** Se agregaron pruebas para lectura exitosa, archivo no encontrado y JSON inválido (`test_storage.py`). Todas pasaron exitosamente.

### T-03 Lógica de búsqueda
**What the agent did:** El agente implementó la función `search_customers` en `src/service.py`. Programó las reglas de negocio: ignorar mayúsculas/minúsculas, filtrar resultados dando prioridad a coincidencias exactas (por nombre o correo), y agregar posteriormente coincidencias parciales ordenadas alfabéticamente por apellido.
**Human review:** Se autorizó la continuación hacia la siguiente tarea al revisar a detalle el código fuente de la función search_customers al correr las pruebas unitarias.
**Tests:** Se agregaron pruebas unitarias (`tests/test_service.py`) simulando la base de clientes para comprobar el filtrado, el ordenamiento y el escenario de cero coincidencias. 

### T-04 Validación y errores
**What the agent did:** El agente construyó `src/cli.py` para fungir como el punto de entrada de la herramienta. Incorporó las validaciones correspondientes para la terminal (rechazo de términos vacíos, no alfanuméricos o menores a 3 caracteres) mostrando limpiamente el mensaje "No se encontraron clientes", y ocultó los rastros de errores del sistema (*stacktraces*) al usuario final.
**Human review:** Se intervino para interrogar al agente y asegurarse de que este no hubiera alterado clandestinamente los archivos `SPEC.md` o `REQUIREMENTS.md` con el objetivo de hacer pasar las pruebas de manera fraudulenta. El agente confirmó su apego estricto a las reglas del proyecto.
**Tests:** Se creó `tests/test_cli.py` para verificar que la terminal arrojara los textos correctos y códigos de salida 0 o 1 de acuerdo al flujo dictado. Todas pasaron exitosamente.

### T-05 Pruebas automatizadas
**What the agent did:** El agente renombró el archivo de pruebas de servicio a `tests/test_search.py` para cumplir milimétricamente con `TASKS.md`. Etiquetó en código el cumplimiento de los 7 escenarios de prueba (TS-01 a TS-07) y agregó una prueba faltante (TS-02) para campos no permitidos. Instaló `pytest-cov`, descubrió baja cobertura inicial en `cli.py` por el uso de subprocesos, y refactorizó la prueba usando `mock` para poder inspeccionar el flujo interno.
**Human review:** Se revisó el reporte de cobertura y confundió con la columna "Miss" con pruebas fallidas. El agente explicó detalladamente cómo se lee un reporte de cobertura y aclaró que la métrica excluía intencionalmente el bloque de ejecución `if __name__ == '__main__':`.
**Tests:** La batería creció a 18 pruebas automatizadas. Todas pasaron con éxito, arrojando una **cobertura total de código del 96%** (superando la métrica solicitada del 90%).

### T-06 Documentación
**What the agent did:** El agente actualizó la Matriz de Trazabilidad (`docs/traceability.md`) conectando los requerimientos con las pruebas automatizadas, redactó las instrucciones de ejecución en español (`README.md`) y agregó la `Entry 05` al archivo `AI_USAGE_LOG.md` resumiendo la sesión de trabajo orientada a especificaciones.
**Human review:** Se instruyó explícitamente no llenar la columna "Notes" de la matriz de trazabilidad. Posteriormente, solicitó expandir la base de datos `customers.json` para ejecutar revisiones manuales, por lo que el agente pobló el archivo con un conjunto de datos estratégicamente diseñado para demostrar los filtros en vivo mediante casos de uso.
**Tests:** Se verificó de forma manual los 5 casos de uso propuestos por el agente en su propia terminal. La suite de pruebas de `pytest` se volvió a correr de forma íntegra para confirmar la estabilidad total.

## Problems Encountered
- **Error inicial en el alcance:** El agente se adelantó al alcance estipulado de la T-01 creando la carpeta `data/` prematuramente, violando la regla del proyecto de realizar únicamente cambios pequeños y enfocados.
- **Medición de cobertura en CLI:** Inicialmente, las pruebas de la interfaz de línea de comandos se ejecutaban abriendo una terminal virtual (`subprocess`), lo que provocaba que la librería `pytest-cov` no detectara la ejecución de las líneas de código de `cli.py`, arrojando una cobertura engañosa del 0% para ese archivo.
- **Importaciones relativas:** Al probar un script de verificación manual mediante `python -c` en la T-02, surgió un error de importación relativa porque Python no reconocía a `src` como paquete. Esto obligó al agente a configurar correctamente el `sys.path`.

## Human Interventions
- **Control de Alcance (T-01):** Se cuestionó la existencia de archivos fuera de lugar y exigió apego estricto a las tareas, recordando al agente la importancia de guiarse por `AGENTS.md`.
- **Verificación de Integridad de Reglas (T-04):** Se le preguntó al agente para cerciorarse de que la Especificación o los Requerimientos no hubieran sido manipulados con el único fin de hacer pasar las pruebas.
- **Clarificación de Conceptos (T-05):** Se solicitaron explicaciones sobre un supuesto fallo reportado en la consola, lo que permitió al agente esclarecer la diferencia entre métricas de cobertura ("Miss") y afirmaciones fallidas (failed assertions).
- **Pruebas en Vivo (T-06):** Se frenó la finalización documental del proyecto para exigir un archivo JSON más extenso y casos de uso concretos que le permitieran constatar empíricamente el comportamiento de la CLI en su terminal.

## Requirement / Specification Changes
Ninguno.

No existió ninguna modificación en los requerimientos. Los archivos `REQUIREMENTS.md` y `SPEC.md` se mantuvieron sin modificaciones a lo largo del desarrollo. 

## Final Verification
El sistema es funcional como una CLI local en Python. Parsea exitosamente la persistencia desde `customers.json`, aplica de manera correcta los filtros de búsqueda tolerando diferencias de mayúsculas y minúsculas, prioriza en la salida las coincidencias exactas por nombre/correo, y ordena alfabéticamente las coincidencias parciales sobrantes. Todo esto garantizando validaciones de entrada (minúsculas no vacías mayores a 2 caracteres) y atrapando errores para no mostrar *stacktraces*. El código se entregó con una cobertura medida del 96% superando los 7 Escenarios de Prueba requeridos.

## Lessons Learned
- Apegarse rigurosamente a una especificación y documentación predefinoda reduce en gran medida las alucinaciones del agente y reduce considerablemente la complejidad del diseño de software, manteniendo el enfoque en el dominio y sus reglas.
- Intervenir a tiempo para forzar al agente a cumplir pautas operativas (ej. "no tocar archivos ajenos" o "no crear lo que no te toca") previene la creación de código malo y mantiene el repositorio estructurado.
- La parte más dificíl de la ingeniería de software ya no es la codificación, si no la especificación de lo que el agente debe de hacer, cómo lo debe de hacer y bajo que condiciones.

