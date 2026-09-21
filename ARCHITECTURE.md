# Architecture

## Overview
Aplicación CLI local en Python que lee datos de clientes desde un archivo JSON. Usa una arquitectura simple de tres capas para separar la interacción del usuario de la lógica de negocio.

## Components
1. **CLI:** Interpreta los comandos del usuario.
2. **CustomerService:** Aplica reglas de negocio y validaciones.
3. **Storage:** Lee el archivo de datos JSON.

## Responsibilities
- **CLI:** Recibir texto del usuario y mostrar los resultados.
- **CustomerService:** Filtrar y ordenar los clientes.
- **Storage:** Acceder al archivo de datos de forma segura.

## Data Flow
1. El usuario ejecuta un comando en la CLI.
2. La CLI envía el término al `CustomerService`.
3. El servicio pide todos los datos al `Storage`.
4. El servicio filtra y ordena los datos según las reglas definidas en SPEC.
5. El resultado final se devuelve y la CLI lo imprime.

## Interfaces
- CLI command (ej. `python search.py "termino"`).
- Service function: `search_customers(term: str)`

## Error Handling
La validación pertenece al servicio; la CLI se encarga de atrapar los errores y mostrar mensajes claros al usuario.

## Testing Strategy
- Unit tests for service.
- Persistence tests for storage.
- Minimal CLI verification.

## Dependencies
Python standard library + pytest for development.

## Design Decisions
Mantener la lógica de negocio (CustomerService) totalmente independiente de la CLI para facilitar las pruebas.

## Trade-offs
Cargar el archivo JSON completo en memoria en cada búsqueda es menos eficiente, pero evita la complejidad de instalar y mantener una base de datos.
