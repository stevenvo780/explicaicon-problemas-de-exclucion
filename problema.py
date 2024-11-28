import cupy as cp
import networkx as nx
import matplotlib.pyplot as plt
import random

# Función para crear un grafo inicial representando la comunidad
def crear_grafo_inicial(num_nodos):
    """
    Crea un grafo inicial con un número determinado de nodos.

    Parámetros:
    - num_nodos: Número de nodos iniciales en la comunidad.

    Retorna:
    - G: Grafo de NetworkX representando la comunidad inicial.
    """
    G = nx.Graph()
    for i in range(num_nodos):
        G.add_node(i)
        if i > 0:
            # Conectar cada nuevo nodo con uno anterior al azar
            G.add_edge(i, random.choice(range(0, i)))
    return G

# Función para simular la evolución de la comunidad
def simular_red_gpu(G, duraciones_sancion=None, iteraciones=12, reintegracion=False, tasa_baneos_base=0.05):
    """
    Simula la evolución de una comunidad virtual aplicando diferentes políticas de sanciones.

    Parámetros:
    - G: Grafo de NetworkX representando la comunidad inicial.
    - duraciones_sancion: Lista de posibles duraciones de sanción temporal.
    - iteraciones: Número de iteraciones (por ejemplo, meses) a simular.
    - reintegracion: Indica si los usuarios sancionados pueden reintegrarse.
    - tasa_baneos_base: Tasa base de baneos para el sistema solucionado.

    Retorna:
    - tamanos: Lista del tamaño de la comunidad en cada iteración.
    """
    # Estados de los usuarios
    # 0 = activo, 1 = sancionado temporalmente, 2 = baneado permanentemente
    nodos = cp.array(list(G.nodes()))
    estados = cp.zeros(len(nodos), dtype=cp.int32)
    tiempos_sancion = cp.zeros(len(nodos), dtype=cp.int32)

    tamanos = []  # Registro del tamaño de la comunidad en cada iteración

    for t in range(iteraciones):
        # Nuevos usuarios se unen a la comunidad (entre 20 y 60 por mes)
        nuevos_usuarios = random.randint(20, 60)
        nuevos_nodos = cp.arange(len(nodos), len(nodos) + nuevos_usuarios)
        for nodo in nuevos_nodos:
            G.add_node(nodo.item())
            # Conectar con un nodo existente al azar
            G.add_edge(nodo.item(), random.choice(nodos.get()))
        nodos = cp.concatenate([nodos, nuevos_nodos])
        estados = cp.concatenate([estados, cp.zeros(len(nuevos_nodos), dtype=cp.int32)])
        tiempos_sancion = cp.concatenate([tiempos_sancion, cp.zeros(len(nuevos_nodos), dtype=cp.int32)])

        # Reducir tiempos de sanción y reintegrar si corresponde
        sancionados = estados == 1
        tiempos_sancion[sancionados] -= 1
        estados[(sancionados) & (tiempos_sancion <= 0)] = 0  # Reintegrar a usuarios cuya sanción terminó

        # Aplicar sanciones
        activos = estados == 0
        num_activos = cp.sum(activos).item()

        if reintegracion:
            # En el sistema solucionado, la tasa de baneos es menor
            tasa_baneos = tasa_baneos_base
        else:
            # En el sistema de exclusión, la tasa de baneos es mayor debido a la ambigüedad en las reglas
            tasa_baneos = tasa_baneos_base * 2  # Por ejemplo, el doble

        num_baneos = int(num_activos * tasa_baneos)
        num_baneos = max(num_baneos, random.randint(3, 12))  # Asegurar al menos entre 3 y 12 baneos
        num_baneos = min(num_baneos, num_activos)  # No se puede sancionar a más usuarios de los que están activos

        if num_baneos > 0:
            baneados = cp.random.choice(nodos[activos], num_baneos, replace=False)
            if reintegracion:
                estados[baneados] = 1  # Sancionado temporalmente
                # Asignar duraciones de sanción con probabilidades diferentes
                duraciones_prob = [0.7, 0.2, 0.1]  # Probabilidades para 1, 6 y 12 meses
                duraciones = cp.random.choice(duraciones_sancion, size=num_baneos, p=duraciones_prob)
                tiempos_sancion[baneados] = duraciones
            else:
                estados[baneados] = 2  # Baneado permanentemente

        # Registrar el tamaño actual de la comunidad
        tamanos.append((t, cp.sum(estados == 0).item()))  # Solo contar usuarios activos

    return tamanos

# Parámetros de simulación
num_nodos_inicial = 100  # Tamaño inicial de la comunidad
duraciones_sancion = [1, 6, 12]  # Duración de sanciones temporales en meses
iteraciones = 24  # Número de meses a simular
tasa_baneos_base = 0.05  # Tasa base de baneos para el sistema solucionado

# Escenario 1: Exclusión (baneos permanentes con tasa de baneos más alta)
G_exclusion = crear_grafo_inicial(num_nodos_inicial)
resultados_exclusion = simular_red_gpu(
    G_exclusion, duraciones_sancion, iteraciones, reintegracion=False, tasa_baneos_base=tasa_baneos_base
)

# Escenario 2: Reintegración (sanciones temporales con tasa de baneos más baja)
G_solucion = crear_grafo_inicial(num_nodos_inicial)
resultados_solucion = simular_red_gpu(
    G_solucion, duraciones_sancion, iteraciones, reintegracion=True, tasa_baneos_base=tasa_baneos_base
)

# Preparar datos para graficar
df_exclusion = list(map(lambda x: (x[0], x[1]), resultados_exclusion))
df_solucion = list(map(lambda x: (x[0], x[1]), resultados_solucion))

# Graficar resultados
plt.figure(figsize=(10, 6))
plt.plot([x[0] for x in df_exclusion], [x[1] for x in df_exclusion], label="Exclusión (baneos permanentes)", color="red", marker='o')
plt.plot([x[0] for x in df_solucion], [x[1] for x in df_solucion], label="Reintegración (sanciones temporales)", color="green", marker='o')
plt.xlabel("Mes")
plt.ylabel("Número de Usuarios Activos")
plt.title("Simulación de Comunidad Virtual: Exclusión vs. Reintegración")
plt.legend()
plt.grid(True)
plt.show()
