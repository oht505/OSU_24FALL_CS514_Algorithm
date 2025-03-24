import heapq
import random
import time

def MST_Prim(edges):
    graph = {}
    for u, v, weight in edges:
        if u not in graph:
            graph[u] = {}
        if v not in graph:
            graph[v] = {}
        graph[u][v] = weight
        graph[v][u] = weight

    start_node = edges[0][0]

    key = {node: float('inf') for node in graph}
    parent = {node: None for node in graph}
    if start_node is not None:
        key[start_node] = 0

    min_queue = [(0, start_node)]
    mst_edges = []
    mst_weights = 0
    while min_queue:
        min_key, u = heapq.heappop(min_queue)

        for v, weight in graph[u].items():
            if weight < key[v]:
                key[v] = weight
                parent[v] = u
                heapq.heappush(min_queue, (key[v], v))

    for v in parent:
        if parent[v] is not None:
            mst_edges.append((parent[v], v))
            mst_weights += key[v]

    return mst_weights, mst_edges


#Create a new u containing only the element u.
def make_set(u, parent):
    parent[u] = u
#Given an element u, which set does it belong to
def find(u, parent):
    if parent[u] != u:
        parent[u] = find(parent[u], parent)  # Path compression
    return parent[u]

#replace the set containing u and the set containing v by their union.
def union(u, v, parent, rank):
    root_u = find(u, parent)
    root_v = find(v, parent)

    if root_u != root_v:
        if rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        elif rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        else:
            parent[root_v] = root_u
            rank[root_u] += 1


def MST_Kruskal(edges):
    parent = {}
    rank = {}

    for u, v, weight in edges:
        make_set(u, parent)
        make_set(v, parent)
        rank[u] = 0
        rank[v] = 0
    #sort edges in non-decreasing order of their weights
    edges.sort(key=lambda edge: edge[2])

    mst = []
    mst_weight = 0
    for u, v, weight in edges:
        if find(u, parent) != find(v, parent):
            mst.append((u, v))
            mst_weight+= weight
            union(u, v, parent, rank)

    return mst_weight,mst

if __name__=="__main__":
    file_names = ['generate1000_19607_7.txt', 'generate1000_19607_8.txt', 'generate1000_315745_1.txt',
                  'generate1000_315745_2.txt',
                  'generate1500_4994_9.txt', 'generate1500_4994_10.txt', 'generate1500_140359_3.txt',
                  'generate1500_140359_4.txt',
                  'generate2000_49370_5.txt']

    # file_names = ['test.txt']
    import ast

    for file_name in file_names:
        with open(file_name, 'r') as file:
            content = file.read().strip()
            edges = ast.literal_eval(content)
            print(MST_Kruskal(edges))
            print(MST_Prim(edges))
            # num_edges = len(edges)
            # print(num_edges)