# Auditoría contra la consigna

La revisión se realizó con el CSV original y la copia descargada desde GitHub. Esta auditoría no asigna una calificación: la evaluación corresponde al docente.

| Requisito | Estado y evidencia |
|---|---|
| Repositorio creado y clonado | Verificado; repositorio público examen-1. |
| Entorno .venv y dependencias | Verificado en dos copias en el entorno Linux de asistencia. Sin dependencias externas. |
| CSV original en data | Verificado: identidad byte a byte con el archivo proporcionado. |
| .gitignore | Incluye .venv/ y __pycache__/. |
| Registros y sensores distintos | Verificado: 100,000 y 40. |
| Promedios por planta | Calculados y documentados para las cuatro plantas. |
| Máxima con sensor y fecha | Verificado: 104.99 °C y cuatro registros empatados. |
| Conteo > 85 °C | Verificado: 6,954; 85 exactos queda excluido. |
| Planta con más alertas | Verificado: Planta_3, 1,777. Se probaron empates con un caso sintético temporal separado del CSV original. |
| Exportación de alertas | Verificado: todas las filas esperadas, sin filas adicionales, con columnas y valores originales. |
| Rutas relativas y resultados calculados | Verificado; rutas a partir del archivo del programa y resultados derivados del CSV. |
| Cuatro commits significativos | Publicados: configuración, análisis, informe y documentación. La evidencia añade otro commit. |
| README y requirements | Incluyen objetivo, datos simulados, instalación, ejecución y ausencia de dependencias externas. |
| Segunda clonación y entorno nuevo | Verificado desde GitHub; ver reproducibilidad.txt. La exportación coincide con la publicada. |
| Captura de ejecución | PENDIENTE: tomar una captura auténtica en la computadora del alumno y subirla a evidencias/. El registro de texto no sustituye la captura solicitada. |
| 5 V | Tabla completa; distingue datos actuales y ejemplos futuros. |
| Tipos de datos y escala | Cuatro clasificaciones y explicación de por qué el tamaño por sí solo no implica Big Data. |
| Batch y streaming | Se relacionan con el archivo guardado, alertas en segundos y resumen diario. |
| Lambda y Kappa | Escenarios A y B justificados con diagramas Mermaid. |
| Analíticas | Dos hallazgos reales con valores, pregunta predictiva y datos adicionales, acción prescriptiva condicionada. |
| Advertencia sobre el umbral | Aclara que una alerta didáctica no demuestra una falla. |
| Acceso docente | El repositorio es público; confirmar que el docente recibe la URL. |
| Datos del alumno | Nombre incluido; grupo pendiente de confirmar. |

## Pasos pendientes en la computadora del alumno

1. Confirmar el grupo en informe.md.
2. Seguir los comandos de Windows del README para clonar y ejecutar el proyecto.
3. Seguir la sección de reproducibilidad para crear la segunda copia con otro entorno.
4. Tomar una captura real con la ruta de examen-1-reproducibilidad, el comando y los resultados visibles. Guardarla como evidencias/reproducibilidad_windows.png. Si hace falta, usar dos capturas para incluir toda la salida.
5. Subir la captura y la corrección del grupo a GitHub. No subir .venv/.
6. Entregar la URL y volver a revisar esta auditoría.

Los commits y las ejecuciones aquí documentados fueron realizados con asistencia. La prueba Linux no acredita que el alumno ya haya ejecutado los comandos en su propia computadora.
