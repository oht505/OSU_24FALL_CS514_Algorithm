from collections import defaultdict, deque

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
def Max_Flow_Fat(input):
    source, sink, edges = input

    graph = defaultdict(list)
    for u, v, capacity in edges:
        graph[u].append((v, capacity))
        graph[v].append((u, 0))  # add reverse edges with 0 capacity

    print(f'graph: {graph}')

    flow_parents = {}  # for the given path, key=node and value=node's parent
    max_flow = 0       # max flow for all discovered paths

    # all paths added during augmentation; key=parent, value: dictionary of node/capacity for each child of parent
    all_paths = defaultdict(lambda: defaultdict(int))
    while dfs(graph, source, sink, flow_parents):
        path_flow = float("inf")  # maximum flow for current path (constrained by min capacity of each pipe)
        s = sink                    # work backwards from sink towards source
        path = {}

        # constrain max flow as lowest capacity in the augmenting path
        while s != source:
            parent_node = flow_parents[s]
            for u, capacity in graph[parent_node]:
                if u == s:
                    path_flow = min(path_flow, capacity)
                    path[parent_node] = s
                    break
            s = flow_parents[s]

        # Update residual capacities and reverse edges along the path
        v = sink
        while v != source:
            parent_node = flow_parents[v]
            for u, capacity in graph[parent_node]:
                if u == v:
                    parent_node = flow_parents[v]
                    # remove previous capacity and add with updated value
                    graph[parent_node].remove((v, capacity))
                    graph[parent_node].append((v, capacity - path_flow))
                    graph[v].append((u, capacity + path_flow))
                    break
            v = flow_parents[v]

        # save the discovered path to be returned at end
        for node, child in path.items():
            all_paths[node][child] += path_flow
            print(f'all_paths: {all_paths.items()}')
            # print(f"adding path flow ({path_flow}) to all paths {node=}, {child=}")

        max_flow += path_flow
        flow_parents = {}  # clear parents for next loop

    path_list = []
    for node in sorted(all_paths.keys()):
        for child in sorted(all_paths[node].keys()):
            path_list.append((node, child, all_paths[node][child]))

    return max_flow, path_list


def dfs(graph, source, sink, flow_parents):
    visited = set()
    queue = deque()
    queue.append(source)
    visited.add(source)

    while queue:
        parent = queue.popleft()
        for child, capacity in graph[parent]:
            if child not in visited and capacity > 0:
                queue.append(child)
                visited.add(child)
                flow_parents[child] = parent
    return sink in visited


def Max_Flow_Short(input):
    source, sink, edges = input

    graph = defaultdict(list)
    for u, v, capacity in edges:
        graph[u].append((v, capacity))  # forward: capacity of each edge
        graph[v].append((u, 0))  # reverse: residual

    flow_parents = {}       # for the given path, key=node and value=node's parent
    max_flow = 0            # cumulative flow, increases with each augmentation

    # all paths added during augmentation; key=parent, value: dictionary of node/capacity for each child of parent
    all_paths = defaultdict(lambda: defaultdict(int))

    while bfs(graph, source, sink, flow_parents):
        path_flow = float("inf")
        s = sink
        path = {}
        while s != source:
            parent_node = flow_parents[s]
            for u, capacity in graph[parent_node]:
                if u == s:
                    path_flow = min(path_flow, capacity)
                    path[parent_node] = s
                    break
            s = flow_parents[s]

        for node, child in path.items():
            all_paths[node][child] += path_flow
            # print(f"adding path flow ({path_flow}) to all paths {node=}, {child=}")
        max_flow += path_flow
        v = sink
        while v != source:
            u = flow_parents[v]
            for i, (vertex, capacity) in enumerate(graph[u]):
                if vertex == v:
                    graph[u][i] = (vertex, capacity - path_flow)
                    break
            for i, (vertex, capacity) in enumerate(graph[v]):
                if vertex == u:
                    graph[v][i] = (vertex, capacity + path_flow)
                    break
            v = flow_parents[v]

    path_list = []
    for node in sorted(all_paths.keys()):
        for child in sorted(all_paths[node].keys()):
            path_list.append((node, child, all_paths[node][child]))

    return max_flow, path_list

def bfs(graph, source, sink, flow_parents):
    visited = set()
    queue = deque()
    queue.append(source)
    visited.add(source)

    while queue:
        u = queue.popleft()
        for v, capacity in graph[u]:
            if v not in visited and capacity > 0:
                queue.append(v)
                visited.add(v)
                flow_parents[v] = u
                if v == sink:
                    return True
    return False


# Explanation: The source node is 0, the sink node is 3;
# the capacity of edge (0->1) is 1; the capacity of edge (0->2) is 5; etc.
input_1 = (0, 3, [(0, 1, 1), (0, 2, 5), (1, 2, 1), (2, 3, 2), (1, 3, 6)])
# Explanation: "3" is the maximum flow;
# [(0, 1, 1), (0, 2, 2), (1, 3, 1), (2, 3, 2)]
# is an assignment of flows to edges.
expected_1 = (3, [(0, 1, 1), (0, 2, 2), (1, 3, 1), (2, 3, 2)])

input_2 = (0, 4,  [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)])
expected_2 = (8, [(0, 1, 2), (0, 3, 6), (1, 4, 2), (3, 4, 6)])

# generated test cases, some hand editing
input_3 = (0, 7, [(6, 7, 8), (0, 2, 9), (3, 7, 7), (2, 7, 9), (3, 4, 6), (1, 4, 5),
                  (4, 7, 10), (1, 6, 10), (3, 5, 9), (1, 2, 8), (4, 5, 10), (0, 1, 3)])
expected_3 = (12, [(0, 1, 3), (0, 2, 9), (1, 4, 3), (2, 7, 9), (4, 7, 3)])

input_4 = (0, 7, [(6, 7, 8), (0, 2, 9), (3, 7, 7), (2, 7, 9), (3, 4, 6), (1, 4, 5), (4, 7, 10), (1, 6, 10), (3, 5, 9), (1, 2, 8), (4, 5, 10), (0, 4, 9), (0, 7, 10), (5, 6, 10), (1, 5, 10), (5, 7, 5)])
expected_4 = (28, [(0, 2, 9), (0, 4, 9), (0, 7, 10), (2, 7, 9), (4, 7, 9)])

if __name__ == '__main__':

    graph = generate_seq(8, 20, 0)
    source, sink = float('inf'), 0
    for edge in graph:
        u, v, w = edge
        source = min(source, u, v)
        sink = max(sink, u, v)

    print(f'source: {source}, sink: {sink}')
    print(f'graph: {graph}')
    print(Max_Flow_Fat((source, sink, graph)))
    print(Max_Flow_Short((source, sink, graph)))