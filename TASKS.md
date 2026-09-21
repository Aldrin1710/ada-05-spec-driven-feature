# Tasks

## T-01 Configuración del proyecto
- Goal: Crear la estructura básica de directorios del proyecto y configurar el framework de pruebas.
- Files: `src/`, `tests/`, `docs/`
- Acceptance: El entorno está listo y pytest puede ejecutarse sin mostrar errores estructurales.
- Verification: `pytest -v`

## T-02 Modelo de dominio
- Goal: Implementar el modelo de dominio Customer y la lógica de almacenamiento (Storage) para leer desde JSON.
- Files: `src/model.py`, `src/storage.py`, `data/customers.json`
- Acceptance: El archivo JSON se parsea correctamente y se convierte en una lista de objetos nativos de Python.
- Verification: Script simple en Python para imprimir los clientes cargados sin que el programa colapse.

## T-03 Lógica de búsqueda
- Goal: Implementar CustomerService con el filtrado (insensible a mayúsculas, coincidencia parcial) y reglas de ordenamiento.
- Files: `src/service.py`
- Acceptance: Se cumplen los criterios AC-02, AC-03 y AC-04 exclusivamente a nivel lógica de servicio.
- Verification: Invocar la función `search_customers()` manualmente en consola Python para verificar que retorna los subconjuntos correctos.

## T-04 Validación y errores
- Goal: Implementar la CLI, las validaciones de entrada (VR-01, VR-02) y el manejo de errores (EH-01, EH-02).
- Files: `src/cli.py`
- Acceptance: Se cumplen los criterios AC-01, AC-05, AC-06 y AC-07. La CLI intercepta errores y no expone el código interno (stacktrace) al usuario.
- Verification: Ejecutar comandos manuales en la terminal, ej., `python src/cli.py ""`, `python src/cli.py "al"`.

## T-05 Pruebas automatizadas
- Goal: Implementar pruebas automatizadas para todos los Escenarios de Prueba definidos en SPEC.md.
- Files: `tests/test_search.py`, `tests/test_cli.py`
- Acceptance: La cobertura de código  alcanza al menos el 90%, y las pruebas del TS-01 al TS-07 son exitosas.
- Verification: `pytest -v`

## T-06 Documentación
- Goal: Actualizar la matriz de trazabilidad, las instrucciones de ejecución y el log de IA.
- Files: `docs/traceability.md`, `README.md`, `AI_USAGE_LOG.md`
- Acceptance: La trazabilidad conecta claramente Requisito -> AC -> Tarea -> Código -> Prueba. Se cumple la definición de "Hecho" (DoD).
- Verification: Revisión humana de los archivos Markdown generados.
