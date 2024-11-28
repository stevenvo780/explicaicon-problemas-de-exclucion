## Notas Importantes:

- **Ajuste de Datos**: Las tasas de entrada y sanción de usuarios se han ajustado para reflejar los datos reales proporcionados (20 a 60 usuarios nuevos por mes y 3 a 12 baneos por mes).
- **Aleatoriedad**: Se utiliza la función `random.randint` para introducir variabilidad en las entradas y sanciones, simulando fluctuaciones reales en la actividad de la comunidad.
- **Duración de Sanciones**: Las sanciones temporales tienen duraciones de 1 a 3 meses, permitiendo la reintegración de usuarios sancionados en el escenario de solución.
- **Visualización**: Ambos escenarios se grafican en la misma ventana para facilitar la comparación.

---

## README: Explicación Científica del Ejercicio

# Simulación de Gestión de Conflictos en Comunidades Virtuales

Este proyecto presenta una simulación que modela el impacto de diferentes políticas de sanciones en la dinámica de una comunidad virtual. Se comparan dos escenarios:

1. **Exclusión**: Aplicación de baneos permanentes sin posibilidad de reintegración.
2. **Reintegración**: Uso de sanciones temporales que permiten a los usuarios sancionados regresar a la comunidad.

## Objetivo

Analizar cómo las políticas de sanciones afectan el crecimiento y la cohesión de una comunidad virtual, utilizando un enfoque racional y basado en datos.

## Fundamentos Científicos

### Teoría de Sistemas Sociales

Las comunidades virtuales se pueden modelar como sistemas sociales complejos donde las interacciones entre individuos y las normas establecidas influyen en el comportamiento colectivo. Cambios en las políticas de sanciones pueden tener efectos significativos en la estructura y dinámica del sistema.

### Teoría de Agentes

Cada usuario se considera un agente individual con estados y comportamientos específicos. La teoría de agentes permite simular cómo las decisiones a nivel individual (por ejemplo, abandonar la comunidad tras ser sancionado) afectan al sistema en su conjunto.

### Análisis de Redes Sociales

La comunidad se representa mediante grafos, donde los nodos son usuarios y las aristas representan interacciones. Este enfoque facilita el análisis de la estructura de la comunidad y cómo evoluciona con el tiempo.

## Descripción del Modelo

- **Ingreso de Usuarios**: Cada mes, entre 20 y 60 nuevos usuarios se unen a la comunidad, reflejando el crecimiento orgánico.
- **Sanciones**: Cada mes, entre 3 y 12 usuarios activos son sancionados, ya sea de forma permanente o temporal.
  - **Exclusión**: Los usuarios sancionados son baneados permanentemente.
  - **Reintegración**: Los usuarios sancionados temporalmente pueden reintegrarse tras cumplir su sanción.
- **Estados de Usuarios**:
  - **Activo**: Usuario participando en la comunidad.
  - **Sancionado Temporalmente**: Usuario temporalmente inactivo pero con posibilidad de regresar.
  - **Baneado Permanentemente**: Usuario expulsado sin posibilidad de retorno.

## Interpretación de Resultados

Los resultados de la simulación muestran cómo diferentes políticas afectan al tamaño y crecimiento de la comunidad:

- **Exclusión**:
  - El crecimiento es más lento debido a la pérdida permanente de usuarios.
  - Puede generar una percepción negativa y disminuir la cohesión.
- **Reintegración**:
  - Mantiene un crecimiento más estable y rápido.
  - Promueve la rehabilitación y reduce la exclusión social.
  - Mejora la cohesión al permitir que los usuarios aprendan de sus errores y continúen contribuyendo.

## Implicaciones Prácticas

- **Políticas Inclusivas**: Implementar sanciones temporales favorece un ambiente más inclusivo y puede mejorar la retención de usuarios.
- **Reducción de Conflictos**: La posibilidad de reintegración puede disminuir la hostilidad y el resentimiento entre usuarios sancionados.
- **Cohesión Comunitaria**: Al mantener a más usuarios activos, se fortalece la red social y se fomenta un sentido de pertenencia.

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
   - Guarda el código en un archivo, por ejemplo, `simulacion_comunidad.py`.
   - Ejecuta el script:
     ```
     python simulacion_comunidad.py
     ```
3. **Visualizar los resultados**:
   - Se generará una gráfica comparando ambos escenarios en la misma ventana.

## Conclusión

Esta simulación demuestra que las políticas de gestión de conflictos basadas en la reintegración y sanciones temporales pueden ser más efectivas para el crecimiento y cohesión de comunidades virtuales. Un enfoque racional y basado en datos permite tomar decisiones informadas que benefician al sistema en su conjunto.

---

Espero que este script corregido y el README proporcionen una visión clara y científicamente respaldada del problema y su solución.