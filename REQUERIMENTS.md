# Requirements — Customer Search

## User Story
As a user,
I want to search customers by name or email,
so that I can quickly find the customer record I need.

## Functional Requirements
FR-01: El sistema debe rechazar las peticiones de búsqueda y no procesar consultas cuando el término ingresado contenga únicamente espacios en blanco o carezca de caracteres alfanuméricos.
FR-02: El sistema debe evaluar el término de búsqueda comparándolo exclusivamente contra los datos de "nombre", "apellido" y "correo electrónico" del cliente.
FR-03: El sistema debe identificar una coincidencia parcial cuando el término de búsqueda ingresado forme parte del inicio (prefijo) o del interior (subcadena) de cualquiera de los campos permitidos del cliente.
FR-04: El sistema debe retornar los mismos registros de clientes sin distinguir si el término de búsqueda contiene letras mayúsculas, minúsculas o una combinación de ambas.
FR-05: El sistema debe ordenar los resultados retornando primero los clientes que tengan una coincidencia exacta con el término de búsqueda, seguidos por aquellos con coincidencias parciales ordenados alfabéticamente por apellido.
FR-06: El sistema debe retornar el mensaje estandarizado "No se encontraron clientes" cuando la consulta no produzca ninguna coincidencia en los registros.

## Non-Functional Requirements
NFR-01: El sistema debe ejecutar las consultas de búsqueda y retornar el listado de resultados en un tiempo máximo de 150 milisegundos para el 95% de las peticiones locales, operando sobre un archivo de datos estructurado en formato JSON con un volumen de hasta 50,000 registros de clientes.
NFR-02: El sistema debe validar la integridad estructural del esquema de datos durante su lectura inicial en memoria, rechazando archivos corruptos o malformados en un tiempo máximo de 500 milisegundos y notificando el fallo mediante un código de salida de error estándar acompañado de un mensaje descriptivo en la consola.
NFR-03: El código fuente del sistema debe alcanzar una cobertura de pruebas automatizadas mínima del 90% mediante el framework pytest sobre la lógica de búsqueda, superando simultáneamente el análisis de tipado estático estricto sin emitir advertencias.

## Open Questions
Q-01: ¿Es necesario soportar búsquedas difusas (fuzzy) para tolerar pequeños errores ortográficos de los usuarios?
Q-02: ¿El sistema debería guardar un historial de búsquedas recientes del usuario en la máquina local?

## Constraints / Assumptions
C-01: El sistema se desarrollará utilizando Python 3.11+ y se ejecutará de manera local mediante CLI.
C-02: La persistencia de datos se manejará exclusivamente en memoria o a través de un archivo JSON local, sin utilizar motores de bases de datos.
A-01: Se asume que el archivo JSON de origen con los clientes reales estará codificado correctamente en UTF-8.
