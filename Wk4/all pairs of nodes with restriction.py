def add_edge(graph, u, v, weight):
    graph[u].append((v, weight))

def dijkstra(graph, start, n):
    dist = [float('inf')] * n
    dist[start] = 0
    visited = [False] * n

    q = [(0, start)]

    while q:
        min_idx = 0
        for i in range(1, len(q)):
            print("q: ", q)
            if q[i][0] < q[min_idx][0]:
                min_idx = i

        current_dist, u = q.pop(min_idx)

        visited[u] = True

        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                q.append((dist[v], v))

    return dist

def reverse_graph(graph, n):
    reversed_graph = [[] for _ in range(n)]
    for u in range(n):
        for v, weight in graph[u]:
            add_edge(reversed_graph, v, u, weight)

    return reversed_graph

def all_pairs_shortest_path_through_A(graph, n, A):

    dist_from_A = dijkstra(graph, A, n)
    print("dist_from_A: ", dist_from_A)

    reversed_graph = reverse_graph(graph, n)
    print("reversed_graph: ", reversed_graph)

    dist_to_A = dijkstra(reversed_graph, A, n)
    print("dist_to_A: ", dist_to_A)

    shortest_paths = [[float('inf')] * n for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if dist_to_A[u] < float('inf') and dist_from_A[v] < float('inf'):
                shortest_paths[u][v] = dist_to_A[u] + dist_from_A[v]

    return shortest_paths

if __name__=="__main__":
    n = 4
    A = 0
    graph = [[] for _ in range(n)]
    add_edge(graph, 0, 1, 2)
    add_edge(graph, 0, 2, 1)
    add_edge(graph, 1, 0, 1)
    add_edge(graph, 1, 2, 1)
    add_edge(graph, 1, 3, 2)
    add_edge(graph, 2, 0, 2)
    add_edge(graph, 2, 1, 1)
    add_edge(graph, 2, 3, 1)
    add_edge(graph, 3, 2, 2)
    add_edge(graph, 3, 1, 1)

    shortest_paths = all_pairs_shortest_path_through_A(graph, n, A)
    for row in shortest_paths:
        print(row)
