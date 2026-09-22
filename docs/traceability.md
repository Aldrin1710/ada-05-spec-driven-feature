# Matriz de Trazabilidad

| Requirement | SPEC / AC | Task | Files | Test | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| FR-01 | AC-01, VR-01 (TS-01, TS-04) | T-04 | `src/cli.py` | `test_cli_empty_term`, `test_cli_non_alphanumeric` | Completado | |
| FR-02 | AC-02 (TS-02) | T-03 | `src/service.py` | `test_search_unallowed_fields` | Completado | |
| FR-03, FR-04 | AC-03 (TS-03) | T-03 | `src/service.py` | `test_search_case_insensitive` | Completado | |
| FR-05 | AC-04 | T-03 | `src/service.py` | `test_search_exact_and_partial_order` | Completado | |
| FR-06 | AC-05, EH-01 (TS-06) | T-04 | `src/cli.py` | `test_cli_no_match` | Completado | |
| NFR-02 | EH-02 (TS-07) | T-02 | `src/storage.py` | `test_load_customers_file_not_found`, `test_load_customers_invalid_json` | Completado | |
| NFR-01 | N/A (Métrica de rendimiento) | T-03 | `src/service.py` | Verificación teórica (Arquitectura lineal en memoria) | Completado | |
| NFR-03 | N/A (Métrica de calidad) | T-05 | Todo el proyecto | Verificado mediante el reporte automatizado de `pytest-cov` (96%) | Completado | |
