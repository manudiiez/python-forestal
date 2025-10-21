#!/usr/bin/env python3
"""
Script helper para evaluacion automatizada.
Uso: python evaluador_automatico.py --proyecto /path/to/proyecto --config config.json
"""

import json
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Any

class EvaluadorAutomatico:
    def __init__(self, proyecto_path: str, config_path: str):
        self.proyecto_path = Path(proyecto_path)
        self.config = self._cargar_config(config_path)
        self.resultados = []

    def _cargar_config(self, config_path: str) -> Dict:
        with open(config_path, 'r') as f:
            return json.load(f)

    def ejecutar_comando(self, comando: str) -> Dict[str, Any]:
        """Ejecuta comando y retorna resultado."""
        try:
            resultado = subprocess.run(
                comando,
                shell=True,
                cwd=self.proyecto_path,
                capture_output=True,
                text=True,
                timeout=30
            )
            return {
                'exitcode': resultado.returncode,
                'stdout': resultado.stdout,
                'stderr': resultado.stderr,
                'exito': resultado.returncode == 0
            }
        except subprocess.TimeoutExpired:
            return {
                'exitcode': -1,
                'stdout': '',
                'stderr': 'Timeout',
                'exito': False
            }

    def evaluar_criterio(self, criterio: Dict) -> Dict:
        """Evalua un criterio individual."""
        resultado_cmd = self.ejecutar_comando(criterio['comando'])

        # Contar coincidencias
        coincidencias = resultado_cmd['stdout'].count('\n')

        # Evaluar segun threshold
        inverted = criterio.get('inverted', False)
        if inverted:
            pasado = coincidencias <= criterio['threshold']
        else:
            pasado = coincidencias >= criterio['threshold']

        return {
            'id': criterio['id'],
            'categoria': criterio['categoria'],
            'pasado': pasado,
            'coincidencias': coincidencias,
            'threshold': criterio['threshold'],
            'puntaje_max': criterio['puntaje'],
            'puntaje_obtenido': criterio['puntaje'] if pasado else 0,
            'peso': criterio['peso'],
            'output': resultado_cmd['stdout'][:500]  # Primeros 500 chars
        }

    def evaluar_todos(self) -> Dict:
        """Evalua todos los criterios."""
        for criterio in self.config['evaluacion']['criterios']:
            resultado = self.evaluar_criterio(criterio)
            self.resultados.append(resultado)

        # Calcular totales
        puntaje_total = sum(r['puntaje_obtenido'] for r in self.resultados)
        puntaje_maximo = self.config['evaluacion']['puntaje_maximo']
        porcentaje = (puntaje_total / puntaje_maximo) * 100

        # Determinar calificacion
        if porcentaje >= 90:
            calificacion = 'Excelente'
        elif porcentaje >= 80:
            calificacion = 'Muy Bueno'
        elif porcentaje >= 70:
            calificacion = 'Bueno'
        elif porcentaje >= 60:
            calificacion = 'Suficiente'
        else:
            calificacion = 'Insuficiente'

        return {
            'puntaje_total': puntaje_total,
            'puntaje_maximo': puntaje_maximo,
            'porcentaje': round(porcentaje, 2),
            'calificacion': calificacion,
            'aprobado': porcentaje >= 70,
            'criterios_pasados': sum(1 for r in self.resultados if r['pasado']),
            'criterios_fallados': sum(1 for r in self.resultados if not r['pasado']),
            'resultados': self.resultados
        }

    def generar_reporte_json(self, output_path: str):
        """Genera reporte en formato JSON."""
        resumen = self.evaluar_todos()
        with open(output_path, 'w') as f:
            json.dump(resumen, f, indent=2)

    def generar_reporte_markdown(self, output_path: str):
        """Genera reporte en formato Markdown."""
        resumen = self.evaluar_todos()

        markdown = f"""# Reporte de Evaluacion Automatizada

**Proyecto**: {self.proyecto_path.name}
**Fecha**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Resumen

- **Puntaje Total**: {resumen['puntaje_total']}/{resumen['puntaje_maximo']}
- **Porcentaje**: {resumen['porcentaje']}%
- **Calificacion**: {resumen['calificacion']}
- **Estado**: {'APROBADO' if resumen['aprobado'] else 'NO APROBADO'}

## Detalles

| Criterio | Categoria | Pasado | Puntaje | Peso |
|----------|-----------|--------|---------|------|
"""
        for r in self.resultados:
            estado = '✓' if r['pasado'] else '✗'
            markdown += f"| {r['id']} | {r['categoria']} | {estado} | {r['puntaje_obtenido']}/{r['puntaje_max']} | {r['peso']} |\n"

        with open(output_path, 'w') as f:
            f.write(markdown)


if __name__ == '__main__':
    import argparse
    from datetime import datetime

    parser = argparse.ArgumentParser(description='Evaluador automatico de proyectos')
    parser.add_argument('--proyecto', required=True, help='Path al proyecto')
    parser.add_argument('--config', required=True, help='Path al archivo de configuracion')
    parser.add_argument('--output-json', help='Path para reporte JSON')
    parser.add_argument('--output-md', help='Path para reporte Markdown')

    args = parser.parse_args()

    evaluador = EvaluadorAutomatico(args.proyecto, args.config)

    if args.output_json:
        evaluador.generar_reporte_json(args.output_json)
        print(f"Reporte JSON generado: {args.output_json}")

    if args.output_md:
        evaluador.generar_reporte_markdown(args.output_md)
        print(f"Reporte Markdown generado: {args.output_md}")

    # Imprimir resumen en consola
    resumen = evaluador.evaluar_todos()
    print(f"\n=== RESUMEN ===")
    print(f"Puntaje: {resumen['puntaje_total']}/{resumen['puntaje_maximo']} ({resumen['porcentaje']}%)")
    print(f"Calificacion: {resumen['calificacion']}")
    print(f"Estado: {'APROBADO' if resumen['aprobado'] else 'NO APROBADO'}")

    sys.exit(0 if resumen['aprobado'] else 1)