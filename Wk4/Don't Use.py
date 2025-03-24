from collections import deque, defaultdict
import math


def shortest_cycle_length_bfs_backtracking(n, graph):
    shortest_cycle = math.inf

    # Perform BFS from each node to detect cycles
    for start in range(n):
        queue = deque([(start, 0)])  # Queue of (node, distance from start)
        distance = {start: 0}  # Tracks distance from the start node for each BFS call
        parent = {start: None}  # To track the path and avoid revisiting the parent node

        while queue:
            node, dist = queue.popleft()

            # Explore neighbors
            for neighbor in graph[node]:
                if neighbor not in distance:
                    # Visit the neighbor for the first time
                    distance[neighbor] = dist + 1
                    parent[neighbor] = node  # Set the parent to avoid immediate backtracking
                    queue.append((neighbor, dist + 1))
                elif parent[node] != neighbor:  # Detects a cycle without immediately backtracking
                    # Found a cycle back to the start node
                    cycle_length = dist + distance[neighbor] + 1
                    shortest_cycle = min(shortest_cycle, cycle_length)

    return shortest_cycle if shortest_cycle != math.inf else -1


if __name__=="__main__":
    n = 5
    # graph = defaultdict(list, {
    #     0: [1],
    #     1: [2,3],
    #     2: [0],
    #     3: []
    # })

    graph = defaultdict(list, {
        0: [1,2],
        1: [2,3],
        2: [3],
        3: [4],
        4: [1]
    })
    # graph = {
    #     (0, 1),
    #     (0, 2),
    #     (1, 2),
    #     (1, 3),
    #     (2, 3),
    #     (3, 4),
    #     (4, 1)  # 1->2->3->4->1
    # }

    print(shortest_cycle_length_bfs_backtracking(n, graph))