# Customer Search CLI

Aplicación de línea de comandos (CLI) desarrollada en Python para buscar clientes de forma rápida en una base de datos local JSON.

## Requisitos
- Python 3.11+
- `pytest` y `pytest-cov` (para las pruebas y medición de cobertura)

## Instrucciones de Ejecución

Para realizar una búsqueda desde la raíz del proyecto, cuentas con dos opciones pasando el término a buscar entre comillas:

**Opción 1: Usar el script rápido**
Si utilizas la terminal de Windows (CMD), puedes escribir directamente:
```cmd
search "ale"
```

**Opción 2: Ejecución estándar con Python**
```bash
python src/cli.py "ale"
```

El sistema admite búsquedas por fragmentos de nombre, apellido o correo electrónico, y las ordenará automáticamente dándole prioridad a las coincidencias exactas.
## Pruebas Automatizadas

El proyecto cuenta con una batería de pruebas diseñada con enfoque SDD (Spec-Driven Development) para garantizar el 100% de cumplimiento de los Escenarios de Prueba.

Para ejecutar todas las pruebas y mostrar la cobertura de código, ejecuta:

```bash
pytest --cov=src tests/
```
