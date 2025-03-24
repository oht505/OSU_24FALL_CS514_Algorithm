from heapdict import heapdict
from collections import deque, defaultdict

# Graph generation function provided
def generate_seq(num_vertices, num_edges, random_seed):
    import random
    random.seed(random_seed)
    temp = [tuple(sorted(random.sample(range(num_vertices), 2)) + [random.randint(1, 20)]) for _ in range(num_edges)]
    graph = []
    edge_sets = set()
    for (u, v, w) in temp:
        if (u, v) not in edge_sets and (v, u) not in edge_sets:
            graph.append((u, v, w))
            edge_sets.add((u, v))
    return graph

def dijkstra_max_bottleneck_path(source,sink, capacities, residual_graph):
    pq = heapdict()
    pq[source] = float('inf')
    parent = {source: None}
    max_cap = {source: float('inf')}

    while pq:
        current, capacity = pq.popitem()
        if current == sink:
            path = []
            bottleneck = capacity
            i=0
            while current != source:
                prev = parent[current]
                path.append((prev, current))
                bottleneck = min(bottleneck, capacities[(prev, current)])
                current = prev
            return path[::-1], bottleneck

        for neighbor in residual_graph[current]:
            residual_cap = capacities[(current, neighbor)]
            if residual_cap > 0:
                new_cap = min(capacity, residual_cap)
                if neighbor not in max_cap or new_cap > max_cap[neighbor]:
                    max_cap[neighbor] = new_cap
                    pq[neighbor] = -new_cap  # Negate for max-priority
                    parent[neighbor] = current

    return None, 0

def bfs_find_augmenting_path(source,sink, capacities, residual_graph):
    parent = {source: None}
    queue = deque([source])
    while queue:
        current = queue.popleft()
        print(current)
        for neighbor in residual_graph[current]:
            if neighbor not in parent and capacities[(current, neighbor)] > 0:
                parent[neighbor] = current
                if neighbor == sink:
                    path = []
                    bottleneck = float('inf')
                    while neighbor != source:
                        prev = parent[neighbor]
                        path.append((prev, neighbor))
                        bottleneck = min(bottleneck, capacities[(prev, neighbor)])
                        neighbor = prev
                    return path[::-1], bottleneck
                queue.append(neighbor)
    return None, 0


def ford_fulkerson_short_pipes(graph,isFat):
    source = graph[0];
    sink = graph[1];
    edges = graph[2];

    residual_graph = defaultdict(list)
    capacities = {}
    for u, v, w in edges:
        residual_graph[u].append(v)
        residual_graph[v].append(u)  # Reverse edge
        capacities[(u, v)] = w
        capacities[(v, u)] = 0  # Initially, reverse edge has 0 capacity

    #print(capacities)
    max_flow = 0
    while True:
        # Find shortest augmenting path using BFS
        if isFat:
            augmenting_path, bottleneck = dijkstra_max_bottleneck_path(source,sink, capacities, residual_graph)
        else:
            augmenting_path, bottleneck = bfs_find_augmenting_path(source,sink, capacities, residual_graph)

        if not augmenting_path:  # No more augmenting paths
            break
        max_flow += bottleneck  # Add bottleneck value to max flow
        # Update the residual graph
        for u, v in augmenting_path:
            capacities[(u, v)] -= bottleneck
            capacities[(v, u)] += bottleneck

    # Extract flow assignments
    flow_assignment = []
    for u, v, w in edges:
        flow = w - capacities[(u, v)]
        if flow > 0:
            flow_assignment.append((u, v, flow))

    return max_flow, flow_assignment

# Example usage
Fat = True;
Short = False;
graph = (0,3,[(0, 1, 1), (0, 2, 5), (1, 2, 1), (2, 3, 2), (1, 3, 6)])
# graph = (0, 4,  [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)])

res_fat = ford_fulkerson_short_pipes(graph, Fat)
res_short = ford_fulkerson_short_pipes(graph,Short)

print("Max Flow:", res_fat)
print("Max Flow:", res_short)
