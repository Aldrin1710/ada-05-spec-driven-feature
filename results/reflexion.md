# Reflexión 

1. **¿Qué diferencia hay entre requirement, specification y prompt?**
Un requerimiento es lo que el cliente necesita, expresado de forma general y en palabras cotidianas. La especificación traduce esa necesidad a reglas claras, indicando exactamente cómo debe comportarse el sistema para considerarlo terminado. Por último, un prompt es la instrucción que se le da a la Inteligencia Artificial.

2. **¿Qué información fue indispensable antes de programar?**
Fue indispensable contar con los requerimientos generales del proyecto, una especificación detallada de las reglas a seguir y una visión clara de cómo se estructuraría el programa (arquitectura) para no programar a ciegas.

3. **¿Qué decisiones debieron resolverse antes de programar?**
- Definir qué tipo de aplicación se iba a construir.
- Aclarar qué funciones estaban dentro del proyecto y cuáles no se iban a incluir.
- Establecer exactamente cómo iba a funcionar la búsqueda de clientes.
- La arquitectura del sistema y decisiones de diseño.

4. **¿Qué errores evitó SPEC.md?**
- Evitó que se inventarán reglas del negocio.
- Previno que el agente trabajara de más al delimitar exactamente el alcance del proyecto.
- Impidió que el sistema creara sus propios criterios para decir si el trabajo estaba "terminado".
- Garantizó que existieran pruebas para verificar cada función del sistema, ya que los escenarios estaban predefinidos.

5. **¿Qué problema evita separar REQUIREMENTS.md de SPEC.md?**
Evita la confusión entre lo que el cliente quiere y cómo debe funcionar técnicamente. Al separarlos, nos aseguramos de que el documento técnico (SPEC) contenga instrucciones precisas para programar, sin mezclarlo con las ideas generales del cliente, lo que evita contradicciones o que el desarrollador (o la IA) interprete las cosas a su manera.

6. **¿Qué papel tuvo AGENTS.md?**
Funcionó como el jefe o supervisor de la IA. Le dio pautas de comportamiento, le prohibió modificar documentos clave para hacer trampa en las pruebas y la obligó a hacer cambios pequeños, enfocados y organizados.

7. **¿Qué cambió durante la revisión humana?**
Durante la revisión humana se corrigió el rumbo cuando la IA intentó adelantarse y crear archivos fuera de su tarea actual. También sirvió para obligar a la IA a crear datos de prueba más reales en el archivo JSON (para comprobar manualmente que los filtros y el orden alfabético funcionaban).

8. **¿La arquitectura coincidió con el código final?**
Sí.

9. **¿Qué requisito fue más difícil de probar?**
El requisito más complejo fue el de ordenar los resultados primero por coincidencia exacta y luego alfabéticamente por apellido. Por otro lado, los requerimientos no funcionales  RNF-01 Y RNF-03 no se pudieron probar con código estándar del sistema, sino que dependieron de la arquitectura elegida y del reporte externo de cobertura.

10. **¿Qué mejorarías en tu proceso spec-driven?**
Mejoraría la forma en que redacto los requerimientos iniciales. Al principio escribí las ideas de forma demasiado técnica, en lugar de escribirlas de manera natural y sencilla, tal y como lo pediría un usuario o cliente real.

11. **¿Por qué SPEC.md puede funcionar como contrato verificable sin duplicar los requisitos?**
Porque traduce las intenciones del cliente en "criterios de aceptación" y "escenarios de prueba". Es decir, proporciona las condiciones exactas y medibles que deben cumplirse para decir que el trabajo funciona, sirviendo de puente directo entre lo que se pidió y las pruebas del código.

12. **¿Qué decisiones importantes aparecen en tu AI Usage Log y cómo cambió tu criterio después de revisar las sugerencias de la IA?**
Destaca la decisión de simplificar drásticamente la arquitectura del sistema, pasando de un diseño inicial complejo a uno directo de tres capas. Mi criterio cambió al entender que hacer las cosas demasiado complejas sin necesidad solo iba a confundir a la IA a la hora de programar. También resalta cómo delegué en la IA la generación de las pruebas, interviniendo yo únicamente para supervisar que siguiera la metodología correcta.
