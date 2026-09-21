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
Prompt/goal: Instruir a la IA para que simplificara el borrador inicial de la arquitectura porque estaba sobre-diseñado y demasiado técnico.
AI contribution: Reescribió ARCHITECTURE.md usando extrema simplicidad (3 capas centrales: CLI, Service, Storage) imitando el enfoque minimalista del PDF de clase.
Student decision: Acepté la versión simplificada. Esto reduce el riesgo de que el agente de IA alucine patrones de diseño innecesarios al programar.
Impact: ARCHITECTURE.md fue reemplazado por una versión limpia y directa.

## Entry 04 - Corrección de Criterios de Aceptación
Stage: Specification
Prompt/goal: Eliminar el Manejo de Errores (EH) y Reglas de Validación (VR) envueltos erróneamente como Criterios de Aceptación (AC).
AI contribution: Removió los AC redundantes y mapeó directamente los escenarios de prueba a los bloques de validación y error.
Student decision: Acepté la corrección para mantener una estricta adherencia a la metodología SDD y a los contenidos de la presentación de la asignatura.
Impact: SPEC.md fue actualizado con el mapeo correcto de escenarios de prueba.
