# AI Usage Log

## Entry 01 - Revisión del alcance de la especificación
Stage: Requirements / Specification
Prompt/goal: Consultar a la IA si los 12 requisitos del ADA-04 debían usarse para el ADA-05, dada la restricción de hacer solo una CLI local.
AI contribution: La IA confirmó que el ADA-05 tiene un alcance mínimo (CLI + JSON) y sugirió descartar requisitos de interfaz (Paginación) y autenticación (Ofuscación por roles).
Student decision: Acepté la sugerencia. Eliminé los requisitos fuera de alcance para evitarsobrecarga y consolidé los Requisitos Funcionales centrales.
Impact: REQUIREMENTS.md y SPEC.md fueron actualizados para encajar perfectamente con las restricciones.

## Entry 02 - Adaptación de Requisitos No Funcionales
Stage: Requirements
Prompt/goal: Adaptar los requisitos no funcionales generados en el ada 4 para el contexto de una CLI local en Python.
AI contribution: Propuso enfocarse en la Integridad de Datos (validar el esquema JSON al cargar) y Mantenibilidad (forzar Type Hints estrictos y cobertura con pytest).
Student decision: Acepté las propuestas ya que representan prácticas de ingeniería reales el contexto del proyecto.
Impact: La sección NFR de REQUIREMENTS.md se actualizó con límites realistas y verificables.

## Entry 03 - Simplificación de la Arquitectura 
Stage: Architecture
Prompt/goal: Instruir a la IA para que simplificara la arquitectura porque estaba sobre-diseñada y demasiada técnica para un problema sencillo.
AI contribution: Reescribió ARCHITECTURE.md usando extrema simplicidad (3 capas centrales: CLI, Service, Storage) imitando el enfoque minimalista del PDF de clase.
Student decision: Acepté la versión simplificada. Esto reduce el riesgo de que el agente de IA alucine patrones de diseño innecesarios al programar.
Impact: ARCHITECTURE.md fue reemplazado por una versión limpia y directa.

## Entry 04 - Corrección de Criterios de Aceptación
Stage: Specification
Prompt/goal: Eliminar el Manejo de Errores (EH) y Reglas de Validación (VR) envueltos erróneamente como Criterios de Aceptación (AC).
AI contribution: Removió los AC redundantes y mapeó directamente los escenarios de prueba a los bloques de validación y error.
Student decision: Acepté la corrección para mantener una estricta adherencia a la metodología SDD y a los contenidos de la presentación de la asignatura.
Impact: SPEC.md fue actualizado con el mapeo correcto de escenarios de prueba.

## Entry 05 - Implementación guiada por SDD 
Stage: Implementation & Testing
Prompt/goal: Instruir al agente de IA para implementar el sistema siguiendo las tareas (T-01 a T-06) descritas en la documentación. Posteriormente, se le ordenó expandir con mayor diversidad de datos el archivo 'customers.json' y proveer comandos para ejecutar casos de prueba manuales.
AI contribution: El agente interpretó el modelo de dominio, implementó el almacenamiento en JSON, la lógica de búsqueda en servicio y la aplicación CLI. Refactorizó la simulación de terminal en 'test_cli.py' logrando un 96% de cobertura total. Además, generó un set de datos enriquecido para validar empíricamente los filtros y el ordenamiento de búsqueda.
Student decision: Revisó los cambios del agente en cada iteración, verificando que archivos como SPEC.md y REQUERIMENTS.md no se modificaran. Se cercioró de que las pruebas cubrieran los nuevos archivos generados y validó personalmente en consola el funcionamiento real del proyecto con los nuevos datos.
Impact: Proyecto finalizado exitosamente. Todos los escenarios de prueba son verificables de forma automatizada y manual, y la trazabilidad demuestra la conexión completa desde los requerimientos hasta el código implementado.
