"""Analiza las mediciones simuladas y exporta las alertas de temperatura."""
import csv
from collections import Counter, defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path

# Todas las rutas se construyen a partir de la carpeta del proyecto.
BASE = Path(__file__).resolve().parent
ENTRADA = BASE / 'data' / 'sensores_industriales.csv'
SALIDA = BASE / 'resultados' / 'alertas.csv'
UMBRAL = Decimal('85')
COLUMNAS = ['id_registro', 'fecha_hora', 'id_sensor', 'planta',
            'temperatura_c', 'vibracion_mm_s']


def analizar(entrada=ENTRADA, salida=SALIDA):
    sensores = set()
    sumas = defaultdict(Decimal)
    cantidades = Counter()
    alertas_por_planta = Counter()
    alertas = []
    maximas = []
    maxima = None
    total = 0

    with entrada.open(newline='', encoding='utf-8-sig') as archivo:
        lector = csv.DictReader(archivo)
        columnas = lector.fieldnames
        if columnas is None or not set(COLUMNAS).issubset(columnas):
            raise ValueError('El CSV no contiene todas las columnas requeridas.')
        for fila in lector:
            total += 1
            if None in fila or any(fila[c] is None or not fila[c].strip() for c in COLUMNAS):
                raise ValueError(f'Registro {total}: fila incompleta o mal formada.')
            try:
                temperatura = Decimal(fila['temperatura_c'])
            except InvalidOperation as error:
                raise ValueError(f'Registro {total}: temperatura no numerica.') from error
            if not temperatura.is_finite():
                raise ValueError(f'Registro {total}: temperatura no finita.')
            planta = fila['planta']
            sensores.add(fila['id_sensor'])
            sumas[planta] += temperatura
            cantidades[planta] += 1
            if maxima is None or temperatura > maxima:
                maxima = temperatura
                maximas = [fila]
            elif temperatura == maxima:
                maximas.append(fila)
            if temperatura > UMBRAL:
                alertas.append(fila)
                alertas_por_planta[planta] += 1

    salida.parent.mkdir(parents=True, exist_ok=True)
    with salida.open('w', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()
        escritor.writerows(alertas)

    print(f'Registros: {total:,}')
    print(f'Sensores distintos: {len(sensores)}')
    print('\nTemperatura promedio por planta:')
    for planta in sorted(cantidades):
        print(f'  {planta}: {sumas[planta] / cantidades[planta]:.4f} grados C')
    if maxima is None:
        print('\nNo hay lecturas para calcular una temperatura maxima.')
    else:
        print(f'\nTemperatura maxima: {maxima} grados C')
        for fila in maximas:
            print(f"  Sensor {fila['id_sensor']} | Fecha {fila['fecha_hora']} | "
                  f"{fila['planta']} | Registro {fila['id_registro']}")
    print(f'\nLecturas con temperatura mayor que 85 grados C: {len(alertas):,}')
    print('Alertas por planta:')
    for planta in sorted(cantidades):
        print(f'  {planta}: {alertas_por_planta[planta]}')
    if cantidades:
        mayor = max(alertas_por_planta[p] for p in cantidades)
        ganadoras = [p for p in sorted(cantidades) if alertas_por_planta[p] == mayor]
        print(f"Planta(s) con mas alertas: {', '.join(ganadoras)} ({mayor} cada una)")
        if not alertas:
            print('No se detectaron alertas; todas las plantas empatan en cero.')
    print(f'\nArchivo exportado: {salida.name} (carpeta resultados)')


if __name__ == '__main__':
    try:
        analizar()
    except (OSError, ValueError, csv.Error) as error:
        raise SystemExit(f'Error: {error}')
