# Análisis de sensores industriales

Proyecto del primer parcial. El objetivo es analizar las temperaturas de cuatro plantas, identificar alertas y relacionar los resultados con los fundamentos de Big Data.

## Datos

El archivo `data/sensores_industriales.csv` contiene **datos simulados**, no mediciones reales de una empresa. El archivo entregado contiene 100,000 registros de 40 sensores distribuidos en cuatro plantas (25,000 registros por planta). Las fechas van del 1 de septiembre de 2026 a las 00:00 al 2 de septiembre de 2026 a las 17:39. Se interpreta la fecha como día/mes/año.

| Columna | Descripción |
|---|---|
| id_registro | Identificador de la medición |
| fecha_hora | Fecha y hora de la lectura, día/mes/año hora:minuto |
| id_sensor | Identificador del sensor |
| planta | Planta donde está instalado |
| temperatura_c | Temperatura en grados Celsius |
| vibracion_mm_s | Vibración en milímetros por segundo |

La regla didáctica de alerta es **temperatura > 85 °C**. Una lectura igual a 85 °C no genera alerta. Una alerta no demuestra que una máquina vaya a fallar.

## Requisitos

Git y Python 3.10 o posterior. Se utiliza exclusivamente la biblioteca estándar (`csv`, `collections`, `decimal` y `pathlib`), por lo que **no se necesitan dependencias externas**. `requirements.txt` contiene una aclaración y su instalación no agrega paquetes. No hay versiones de paquetes externos que fijar.

## Instalación y ejecución en Windows (PowerShell)

Ejecutar estos comandos uno por uno:

```powershell
git clone https://github.com/diegoponchotrejo-png/examen-1.git
cd examen-1
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python analisis.py
```

Si PowerShell bloquea la activación, se puede habilitar únicamente para la ventana actual y repetirla:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Si `py` no está disponible pero `python --version` muestra Python 3.10 o posterior, utilizar `python -m venv .venv`.

## Instalación y ejecución en Linux o macOS

```bash
git clone https://github.com/diegoponchotrejo-png/examen-1.git
cd examen-1
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python analisis.py
```

En Linux se requiere que la instalación de Python incluya el módulo `venv`.

## Resultados y archivos

`analisis.py` calcula todos los resultados a partir del CSV; no contiene resultados precargados. Muestra registros, sensores distintos, promedios, todas las lecturas empatadas en el máximo y todas las plantas empatadas en alertas. Exporta las lecturas con alerta a `resultados/alertas.csv`, manteniendo las columnas y valores originales, sin columna de índice. Crear la carpeta de resultados y sobrescribir la exportación es parte de cada ejecución.

Las rutas son relativas a la ubicación del programa; no dependen de una carpeta personal. Los promedios se muestran con cuatro decimales y los cálculos usan `Decimal`.

- `data/sensores_industriales.csv`: archivo original sin modificaciones.
- `analisis.py`: programa de análisis.
- `resultados/alertas.csv`: exportación calculada.
- `informe.md`: respuestas de los apartados 5 al 9, con diagramas.
- `requirements.txt`: declaración de ausencia de dependencias externas.
- `.gitignore`: excluye `.venv/`, `__pycache__/` y archivos `.pyc`.
- `evidencias/`: evidencia de reproducibilidad y auditoría.

## Reproducibilidad desde otra carpeta

Salir de la primera copia y del entorno. En PowerShell:

```powershell
deactivate
cd ..
git clone https://github.com/diegoponchotrejo-png/examen-1.git examen-1-reproducibilidad
cd examen-1-reproducibilidad
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python analisis.py
git diff --exit-code -- resultados/alertas.csv
```

En Linux o macOS:

```bash
deactivate
cd ..
git clone https://github.com/diegoponchotrejo-png/examen-1.git examen-1-reproducibilidad
cd examen-1-reproducibilidad
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python analisis.py
git diff --exit-code -- resultados/alertas.csv
```

El último comando no debe mostrar diferencias y debe terminar correctamente. Guardar una captura con la ruta de la segunda copia y la salida del programa en `evidencias/`. La prueba en otro entorno no sustituye realizar estos pasos en la computadora del alumno si el docente lo exige.

## Historial

```bash
git log --oneline
```

El historial registra por separado configuración y datos, análisis, informe y documentación/verificación. El repositorio es público para facilitar la revisión del docente.
