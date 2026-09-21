# Customer Search Feature

## Goal
Proveer una herramienta CLI para buscar clientes por nombre o correo.

## Requirements Covered
- FR-01
- FR-02
- FR-03
- FR-04
- FR-05
- FR-06
- NFR-01
- NFR-02
- NFR-03
- C-01
- C-02
- A-01

## Scope
Búsqueda parcial y completa, recuperación de datos, ordenamiento de clientes.

## Out of Scope
La creación, eliminación y actualización de datos de los clientes está fuera del alcance.

## Domain Model
Client:
- id: int
- name: str
- last_name: str
- email: str

## Search Rules
- El sistema debe identificar una coincidencia parcial cuando el término de búsqueda ingresado forme parte del inicio (prefijo) o del interior (subcadena) de cualquiera de los campos permitidos del cliente.
- Además, el sistema debe ordenar los resultados retornando primero los clientes que tengan una coincidencia exacta con el término de búsqueda (sea por nombre o correo), seguidos por aquellos con coincidencias parciales ordenados alfabéticamente por apellido.
- La búsqueda debe ignorar por completo las diferencias entre mayúsculas y minúsculas.

## Validation Rules
VR-01 [FR-01]: El término de búsqueda no podrá ser vacío.
VR-02: El término de búsqueda debe contener al menos 3 caracteres de longitud.

## Error Handling
EH-01 [FR-06]: Un término de búsqueda inválido o sin ninguna coincidencia deberá mostrar un mensaje claro de error indicando que no se encontraron clientes.
EH-02 [NFR-02]: Si el archivo JSON de origen no existe o está corrupto, el sistema debe abortar mostrando el mensaje "Error: No se pudo cargar la base de datos de clientes" y retornar un código de salida de error (exit code 1).

## Acceptance Criteria
AC-01 [FR-01]: Una búsqueda vacía o con caracteres que no sean alfanuméricos no podrá llevarse a cabo y será rechazada.
AC-02 [FR-02]: Una búsqueda que coincida únicamente con campos no permitidos (ej. teléfono o dirección física) no devolverá resultados del cliente.
AC-03 [FR-03, FR-04]: Un término de búsqueda parcial ("ale") ingresado en minúsculas debe devolver exitosamente a un cliente guardado en mayúsculas ("ALEJANDRO").
AC-04 [FR-05]: Una lista de resultados debe mostrar siempre primero a los clientes con coincidencias exactas, antes que aquellos con coincidencias parciales.
AC-05 [FR-06]: Una búsqueda de un cliente inexistente debe mostrar el mensaje de error y no retornar ningún dato.


## Test Scenarios
TS-01 -> AC-01
TS-02 -> AC-02
TS-03 -> AC-03
TS-04 -> VR-01
TS-05 -> VR-02
TS-06 -> EH-01
TS-07 -> EH-02

## Constraints
C-01: El sistema se desarrollará utilizando Python 3.11+ y se ejecutará de manera local mediante línea de comandos (CLI).
C-02: La persistencia de datos se manejará exclusivamente en memoria o a través de un archivo JSON local, sin utilizar motores de bases de datos.

## Open Questions
Q-01: ¿Es necesario soportar búsquedas difusas (fuzzy search) para tolerar errores ortográficos de los usuarios?
Q-02: ¿Qué código de salida (exit code) específico debe retornar la herramienta CLI cuando la búsqueda ocurra sin errores pero no devuelva ningún resultado?
