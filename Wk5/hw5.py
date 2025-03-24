############################################################
## Homework Assignment Week 5: Greedy algorithms
## Name: Hyuntaek Oh
## Email: ohhyun@oregonstate.edu
## Course: CS 514_400 Algorithms
## Due: Nov. 4, 2024
#############################################################
import heapq
import time
import random
import matplotlib.pyplot as plt
import numpy as np

def MST_Prim(edges):
    # Create adjacent graph
    graph = {}
    for u, v, weight in edges:
        if u not in graph:
            graph[u] = {}
        if v not in graph:
            graph[v] = {}
        graph[u][v], graph[v][u] = weight, weight

    # Initialization
    key = {node: float('inf') for node in graph}
    parent = {node: -1 for node in graph}
    start_node = edges[0][0]
    key[start_node] = 0
    min_queue = [(0, start_node)]

    while min_queue:
        _, u = heapq.heappop(min_queue)

        # Update to smaller weight based on adjacent nodes
        for v, weight in graph[u].items():
            if weight < key[v]:
                key[v] = weight
                parent[v] = u
                heapq.heappush(min_queue, (key[v], v))

    # Find MST and the sum of minimum weights
    mst = []
    min_cost = 0
    for i in parent:
        if parent[i] != -1:
            mst.append((parent[i], i))
            min_cost += key[i]

    return (min_cost, mst)

def union(parent, rank, u, v):
    rootU = find(parent, u)
    rootV = find(parent, v)

    # Compare the rank of two parents
    if rootU != rootV:
        if rank[rootU] > rank[rootV]:
            parent[rootV] = rootU
        elif rank[rootU] < rank[rootV]:
            parent[rootU] = rootV
        else:
            parent[rootV] = rootU
            rank[rootU] += 1

def find(parent, u):
    # Find parent of a node
    if parent[u] != u:
        parent[u] = find(parent, parent[u])
    return parent[u]

def MST_Kruskal(graph):
    # Get the number of vertices
    n = 0
    for u, v, w in graph:
        n = max(n, u+1, v+1)

    # Sort edges into non-decreasing order by weight w
    graph.sort(key=lambda edge: edge[2])

    # Initialize disjoint set
    parent = [i for i in range(n)]
    rank = [0] * n

    # Find minimum spanning tree and minimum cost
    mst = []
    min_cost = 0
    for u, v, weight in graph:
        if find(parent, u) != find(parent, v):
            mst.append((u, v))
            min_cost += weight
            union(parent, rank, u, v)

    return (min_cost, mst)

def generate_graph(num_nodes, num_edges, max_weight):
    edges = set()
    while len(edges) < num_edges:
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)
        if u != v:
            weight = random.randint(1, max_weight)
            if ((min(u, v), max(u, v), weight)) not in edges:
                edges.add((min(u, v), max(u, v), weight))
    return list(edges)


def measuring_runtime(input_size):

    num_edges = input_size
    num_node_sparse = input_size
    max_weight = input_size

    graph_sparse = generate_graph(num_node_sparse, num_edges, max_weight)

    num_node_dense = int(np.sqrt(num_edges))-1
    graph_dense = generate_graph(num_node_dense, num_edges, max_weight)

    start_time_Kruskal_sparse = time.time()
    MST_Kruskal(graph_sparse)
    end_time_Kruskal_sparse = time.time()
    Kruskal_time_sparse = end_time_Kruskal_sparse - start_time_Kruskal_sparse

    start_time_Prim_sparse = time.time()
    MST_Prim(graph_sparse)
    end_time_Prim_sparse = time.time()
    Prim_time_sparse = end_time_Prim_sparse - start_time_Prim_sparse

    start_time_Kruskal_dense = time.time()
    MST_Kruskal(graph_dense)
    end_time_Kruskal_dense = time.time()
    Kruskal_time_dense = end_time_Kruskal_dense - start_time_Kruskal_dense

    start_time_Prim_dense = time.time()
    MST_Prim(graph_dense)
    end_time_Prim_dense = time.time()
    Prim_time_dense = end_time_Prim_dense - start_time_Prim_dense

    return Kruskal_time_sparse, Prim_time_sparse, Kruskal_time_dense, Prim_time_dense

# if __name__=="__main__":
    # edges = [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]
    # edges = [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]
    # print(MST_Prim(edges))

    # print("Real time taken in each case")
    # print(f"{'Number of edges: ':<20}{'Kruskal_sparse (s): ':<25}{'Prim_sparse (s): ':<25}{'Kruskal_dense (s): ':<25}{'Prim_dense (s): ':<25}")
    # runtime_data = {
    #     "Graph size (Edges): ": [],
    #     "Kruskal's Sparse Time (s): ": [],
    #     "Prim's Sparse Time (s): ": [],
    #     "Kruskal's Dense Time (s): ": [],
    #     "Prim's Dense Time (s): ": []
    # }
    # size_set = [n for n in range(3, 8)]
    # for size in size_set:
    #     K_sparse, P_sparse, K_dense, P_dense = measuring_runtime(10**size)
    #     print(f'10^{size:<20}{K_sparse:<25.6f}{P_sparse:<25.6f}{K_dense:<25.6f}{P_dense:<25.6f}')
    #     runtime_data["Graph size (Edges): "].append(10**size)
    #     runtime_data["Kruskal's Sparse Time (s): "].append(K_sparse)
    #     runtime_data["Prim's Sparse Time (s): "].append(P_sparse)
    #     runtime_data["Kruskal's Dense Time (s): "].append(K_dense)
    #     runtime_data["Prim's Dense Time (s): "].append(P_dense)
    #
    # plt.figure(figsize=(10, 6))
    # plt.plot(size_set, runtime_data["Kruskal's Sparse Time (s): "], label="Kruskal_sparse", color="Red", marker="o")
    # plt.plot(size_set, runtime_data["Prim's Sparse Time (s): "], label="Prim_sparse", color="Blue", marker="o")
    # plt.plot(size_set, runtime_data["Kruskal's Dense Time (s): "], label="Kruskal_dense", color="Red", marker="x")
    # plt.plot(size_set, runtime_data["Prim's Dense Time (s): "], label="Prim_dense", color="Blue", marker="x")
    # plt.xlabel("Number of edges 10^N")
    # plt.ylabel("Runtime (seconds)")
    # plt.title("Running Time comparison of Kruskal's and Prim's Algorithms")
    # plt.legend()
    # plt.grid(True)
    # plt.show()
    