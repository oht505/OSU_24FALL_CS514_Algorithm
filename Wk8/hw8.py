############################################################
## Homework Assignment Week 8: Linear Programming and
##                              Network Flow
## Name: Hyuntaek Oh
## Email: ohhyun@oregonstate.edu
## Course: CS 514_400 Algorithms
## Due: Nov. 25, 2024
#############################################################
from heapdict import heapdict
from collections import defaultdict
import numpy as np
import time
import matplotlib.pyplot as plt

def generate_seq(k,length,seed):
    import random; random.seed(seed)
    temp=[tuple(sorted(random.sample(range(k),2))+[random.randint(5,10)]) for _ in range(length)]
    graph=[]
    edge_sets=set()
    for (u,v,l) in temp:
        if (u,v) not in edge_sets and (v,u) not in edge_sets:
            graph.append((u,v,l))
            edge_sets.add((u,v))

    return graph

def finding_maximum_capacity_path(graph, source, sink, parents):
    visited = set()
    visited.add(source)
    heap = heapdict()
    heap[source] = graph[source]

    while heap:
        curr_node, adj_nodes = heap.popitem()
        for v, capacity in adj_nodes:
            if v not in visited and capacity > 0:
                heap[v] = graph[v]
                visited.add(v)
                parents[v] = curr_node
    return sink in visited

def Max_Flow_Fat(source, sink, edges):
    # source, sink, edges = input

    # Convert edges to a graph
    graph = {}
    for u, v, cap in edges:
        if u not in graph: graph[u] = []
        if v not in graph: graph[v] = []
        graph[u].append((v, cap))
        graph[v].append((u, 0))

    parent = {}
    maximum_flow = 0
    set_paths = defaultdict(lambda: defaultdict(int))
    while finding_maximum_capacity_path(graph, source, sink, parent):
        bottleneck = float('inf')
        path = {}
        # Max flow is the lowest capacity in the path
        s = sink
        while s != source:
            parent_node = parent[s]
            for u, capa in graph[parent_node]:
                if u == s:
                    bottleneck = min(bottleneck, capa)
                    path[parent_node] = s
                    break
            s = parent[s]

        # Residual and Reverse edges
        v = sink
        while v != source:
            parent_node = parent[v]
            for u, capa in graph[parent_node]:
                if u == v:
                    parent_node = parent[v]
                    graph[parent_node].remove((v, capa))
                    graph[parent_node].append((v, capa - bottleneck))
                    graph[v].append((u, capa + bottleneck))
                    break
            v = parent[v]

        for curr, ahead in path.items():
            set_paths[curr][ahead] += bottleneck

        maximum_flow += bottleneck
        parent = {}

    assigned_path = []
    for curr in sorted(set_paths.keys()):
        for ahead in sorted(set_paths[curr].keys()):
            assigned_path.append((curr, ahead, set_paths[curr][ahead]))

    return maximum_flow, assigned_path

def bfs_finding_shortest_path(graph, source, sink, parents):
    visited = set()
    visited.add(source)
    q = []
    q.append(source)

    while q:
        previous = q.pop(0)
        for node, capacity in graph[previous]:
            if node not in visited and capacity > 0:
                q.append(node)
                visited.add(node)
                parents[node] = previous
                if node == sink:
                    return True
    return False

def Max_Flow_Short(source, sink, edges):
    #source, sink, edges = input

    # Make a graph with edges
    graph = {}
    for u, v, cap in edges:
        if u not in graph: graph[u] = []
        if v not in graph: graph[v] = []
        graph[u].append((v, cap))
        graph[v].append((u, 0))

    parent = {}
    maximum_flow = 0
    set_paths = defaultdict(lambda: defaultdict(int))
    while bfs_finding_shortest_path(graph, source, sink, parent):
        flow = float('inf')
        path = {}

        # Find the shortest path
        s = sink
        while s != source:
            parent_node = parent[s]
            for u, capa in graph[parent_node]:
                if u == s:
                    flow = min(flow, capa)
                    path[parent_node] = s
                    break
            s = parent[s]

        for node, next_node in path.items():
            set_paths[node][next_node] += flow
        maximum_flow += flow

        # Residual and Reverse graph
        v = sink
        while v != source:
            prev = parent[v]
            for i, (vert, cap) in enumerate(graph[prev]):
                if vert == v:
                    graph[prev][i] = (vert, cap - flow)
                    break
            for i, (vert, cap) in enumerate(graph[v]):
                if vert == prev:
                    graph[v][i] = (vert, cap + flow)
            v = parent[v]

    assigned_path = []
    for node in sorted(set_paths.keys()):
        for next_node in sorted(set_paths[node].keys()):
            assigned_path.append((node, next_node, set_paths[node][next_node]))

    return maximum_flow, assigned_path

def measuring_time(num_nodes, length, seed=0):
    graph = generate_seq(num_nodes, length, seed)
    source, sink = float('inf'), 0
    for edge in graph:
        u, v, w = edge
        source = min(source, u, v)
        sink = max(sink, u, v)

    # print(f'source: {source}, sink: {sink}')
    # print(f'graph: {graph}')
    input_data = (source, sink, graph)

    start_time = time.time()
    max_fat, _ = Max_Flow_Fat(input_data)
    end_time = time.time()

    Max_Flow_Fat_time = end_time - start_time

    start_time = time.time()
    max_short, _ = Max_Flow_Short(input_data)
    end_time = time.time()

    Max_Flow_Short_time = end_time - start_time

    return Max_Flow_Fat_time, Max_Flow_Short_time, max_fat, max_short

# if __name__=="__main__":
#     input_data = (0, 3, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)])
#     input_data = (0, 4, [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)])
#     input_data = (0, 7, [(6, 7, 8), (0, 2, 9), (3, 7, 7), (2, 7, 9), (3, 4, 6), (1, 4, 5), (4, 7, 10), (1, 6, 10), (3, 5, 9),
#                 (1, 2, 8), (4, 5, 10), (0, 4, 9), (0, 7, 10), (5, 6, 10), (1, 5, 10), (5, 7, 5)])
#     print(f'Max_Flow_Fat: {Max_Flow_Fat(input_data)}')
#     print(f'Max_Flow_Short: {Max_Flow_Short(input_data)}')
#
#
#     num_nodes = 1000
#     set_num_edges = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
#     set_time_fat = []
#     set_time_short = []
#     set_estimated_time_fat = []
#     set_estimated_time_short = []
#     print(f"{'Number of edges ':<20}{'Estimated Fat pipes: ':<25}{'Fat pipes: ':<25}{'Estimated Short pipes: ':<25}{'Short pipes: ':<25}")
#     for num_edges in set_num_edges:
#         time_fat, time_short, max_fat, max_short = measuring_time(num_nodes, num_edges)
#         if max_fat <= 0: log_fat = 1
#         else: log_fat = np.log(max_fat)
#         if max_short <= 0: max_short = 1
#         estimated_time_fat = (num_edges**2) * np.log(num_edges) * log_fat
#         estimated_time_short = num_nodes * (num_edges**2)
#         set_time_fat.append(time_fat)
#         set_time_short.append(time_short)
#         set_estimated_time_fat.append(estimated_time_fat)
#         set_estimated_time_short.append(estimated_time_short)
#         print(f"{num_edges:<20}{estimated_time_fat:<25}{time_fat:<25}{estimated_time_short:<25}{time_short:<25}")
#
#     plt.figure(figsize=(10, 6))
#     plt.plot(set_num_edges, set_time_fat, label="Fat pipes", color="Red", marker="o")
#     plt.plot(set_num_edges, set_time_short, label="Short pipes", color="Blue", marker="x")
#     plt.xlabel("Number of edges")
#     plt.ylabel("Runtime (seconds)")
#     plt.title("Running Time comparison of Fat and Short pipes")
#     plt.legend()
#     plt.grid(True)
#     plt.show()
#
#     growth_ratios_fat = []
#     growth_ratios_short = []
#     estimated_growth_ratios_fat = []
#     estimated_growth_ratios_short = []
#     for i in range(1, len(set_num_edges)):
#         ratio_fat = set_time_fat[i] / set_time_fat[i-1]
#         ratio_short = set_time_short[i] / set_time_short[i-1]
#         estimated_growth_ratio_fat = set_estimated_time_fat[i] / set_estimated_time_fat[i-1]
#         estimated_growth_ratio_short = set_estimated_time_short[i] / set_estimated_time_short[i - 1]
#         growth_ratios_fat.append(ratio_fat)
#         growth_ratios_short.append(ratio_short)
#         estimated_growth_ratios_fat.append(estimated_growth_ratio_fat)
#         estimated_growth_ratios_short.append(estimated_growth_ratio_short)
#
#     print()
#     print(f"{'Input Size: ':<20}{'Estimated G.R. Fat: ':<25}{'Real G.R. Fat: ':<25}{'Estimated G.R. Short: ':<25}{'Real G.R. Short: ':<25}")
#     for i in range(1, len(set_num_edges)):
#         print(f"{set_num_edges[i]:<20}{estimated_growth_ratios_fat[i-1]:<25}{growth_ratios_fat[i-1]:<25}{estimated_growth_ratios_short[i-1]:<25}{growth_ratios_short[i-1]:<25}")


