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
| Captura de ejecución | Verificado: reproducibilidad_windows.png muestra la segunda carpeta, .venv activo, el comando y los resultados completos en Windows. |
| 5 V | Tabla completa; distingue datos actuales y ejemplos futuros. |
| Tipos de datos y escala | Cuatro clasificaciones y explicación de por qué el tamaño por sí solo no implica Big Data. |
| Batch y streaming | Se relacionan con el archivo guardado, alertas en segundos y resumen diario. |
| Lambda y Kappa | Escenarios A y B justificados con diagramas Mermaid. |
| Analíticas | Dos hallazgos reales con valores, pregunta predictiva y datos adicionales, acción prescriptiva condicionada. |
| Advertencia sobre el umbral | Aclara que una alerta didáctica no demuestra una falla. |
| Acceso docente | El repositorio es público; confirmar que el docente recibe la URL. |
| Datos del alumno | Nombre incluido; grupo IDIA 224 confirmado por el alumno. |

## Cierre de reproducibilidad en Windows

El alumno proporcionó la salida de la primera clonación y ejecución en Windows y una captura de la ejecución en `C:\Users\alfon\examen-1-reproducibilidad`. La captura muestra `.venv` activo, `Get-Location`, `python analisis.py` y los resultados completos, coincidentes con los verificados. Está guardada sin modificaciones en [reproducibilidad_windows.png](reproducibilidad_windows.png).

La comparación byte a byte de la exportación se realizó en el entorno Linux de asistencia. La captura de Windows acredita la ejecución y sus resultados visibles; no muestra el comando de comparación de archivos.

Nombre y grupo IDIA 224 confirmados. Código, documentación, CSV, exportación y captura se encuentran publicados. Queda entregar al docente la URL del repositorio.

Los commits y las pruebas automatizadas se realizaron con asistencia; la captura de Windows fue proporcionada por el alumno.
