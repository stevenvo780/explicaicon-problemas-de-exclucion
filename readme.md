## Notas Importantes:

- **Tasa de Baneos Ajustada**: En el sistema de exclusión, la tasa de baneos es más alta debido a la ambigüedad en las reglas. Se ha multiplicado la tasa base por un factor (en este caso, 2) para reflejar esto.

- **Duraciones de Sanción**: Las sanciones temporales tienen duraciones de 1, 6 y 12 meses, con probabilidades asignadas de 70% para 1 mes, 20% para 6 meses y 10% para 12 meses, reflejando que las sanciones de 1 mes son más probables.

- **Baneos Permanentes**: En el sistema de exclusión, los baneos son permanentes y más frecuentes que en el sistema solucionado.

- **Reintegración**: En el sistema solucionado, los usuarios sancionados temporalmente pueden reintegrarse después de cumplir su sanción.

---

## README Actualizado: Explicación Científica del Ejercicio

# Simulación de Gestión de Conflictos en Comunidades Virtuales

Este proyecto presenta una simulación que modela el impacto de diferentes políticas de sanciones en la dinámica de una comunidad virtual. Se comparan dos escenarios:

1. **Exclusión**: Aplicación de baneos permanentes con una tasa de baneos más alta debido a la ambigüedad en las reglas y falta de tipificación.

2. **Reintegración**: Uso de sanciones temporales con una tasa de baneos más baja, permitiendo a los usuarios sancionados regresar a la comunidad.

## Objetivo

Analizar cómo las políticas de sanciones afectan el crecimiento y la cohesión de una comunidad virtual, incorporando consideraciones como la probabilidad de diferentes duraciones de sanción y las tasas de baneo ajustadas según la claridad normativa.

## Fundamentos Científicos

### Teoría de Sistemas Sociales

Las comunidades virtuales son sistemas sociales complejos donde las normas y su claridad afectan significativamente el comportamiento de los individuos y el sistema en su conjunto. La ambigüedad normativa puede conducir a una mayor tasa de conflictos y sanciones.

### Teoría de Agentes

Los usuarios se modelan como agentes individuales que interactúan dentro del sistema, y cuyas acciones y estados (activo, sancionado, baneado) influyen en la dinámica global.

### Análisis de Redes Sociales

La comunidad se representa mediante grafos para analizar cómo la estructura de la red cambia con diferentes políticas de sanciones y cómo afecta la cohesión de la comunidad.

## Descripción del Modelo

- **Ingreso de Usuarios**: Cada mes, entre 20 y 60 nuevos usuarios se unen a la comunidad.

- **Sanciones**:
  - **Exclusión**:
    - Baneos permanentes.
    - Tasa de baneos más alta debido a la ambigüedad en las reglas.
  - **Reintegración**:
    - Sanciones temporales de 1, 6 o 12 meses.
    - Probabilidades de duración: 70% para 1 mes, 20% para 6 meses, 10% para 12 meses.
    - Tasa de baneos más baja gracias a reglas claras y tipificadas.

- **Estados de Usuarios**:
  - **Activo**: Usuario participando en la comunidad.
  - **Sancionado Temporalmente**: Usuario inactivo por un período específico, con posibilidad de reintegración.
  - **Baneado Permanentemente**: Usuario expulsado sin posibilidad de retorno.

## Consideraciones Adicionales

- **Tasa de Baneos**:
  - En el sistema de exclusión, la tasa de baneos es el doble que en el sistema solucionado para reflejar la mayor probabilidad de sanciones debido a la ambigüedad normativa.
  - Se asegura que haya al menos entre 3 y 12 baneos por mes en ambos sistemas, acorde con los datos reales.

- **Duraciones de Sanción**:
  - Las sanciones temporales tienen duraciones de 1, 6 y 12 meses, con mayor probabilidad para las sanciones de menor duración.

## Interpretación de Resultados

Los resultados muestran que:

- **Exclusión**:
  - La comunidad crece más lentamente y puede estancarse debido a la alta tasa de baneos permanentes.
  - La ambigüedad en las reglas conduce a más conflictos y sanciones, afectando negativamente la cohesión.

- **Reintegración**:
  - La comunidad crece de manera más sostenida gracias a una menor tasa de baneos y la posibilidad de reintegración.
  - Reglas claras y sanciones proporcionales reducen conflictos y mejoran la percepción de justicia entre los usuarios.

## Implicaciones Prácticas

- **Claridad Normativa**: Establecer reglas claras y tipificadas reduce la tasa de baneos y mejora la gestión de conflictos.

- **Sanciones Proporcionales**: Aplicar sanciones temporales con duraciones ajustadas a la gravedad de la falta promueve la rehabilitación y mantiene la cohesión comunitaria.

- **Gestión Efectiva**: Un enfoque racional y basado en datos permite identificar fallas internas y desarrollar soluciones efectivas que beneficien al sistema en su conjunto.

## Cómo Ejecutar el Proyecto

### Requisitos

- Python 3.x
- Bibliotecas:
  - `cupy`
  - `networkx`
  - `matplotlib`

### Pasos

1. **Instalar las bibliotecas necesarias**:
   ```
   pip install cupy networkx matplotlib
   ```
2. **Ejecutar el script**:
   - Guarda el código en un archivo, por ejemplo, `problema.py`.
   - Ejecuta el script:
     ```
     python simulacion_comunidad.py
     ```
3. **Visualizar los resultados**:
   - Se generará una gráfica comparando ambos escenarios en la misma ventana.