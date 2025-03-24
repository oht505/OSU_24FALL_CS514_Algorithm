

def shortest_cycle(graph):

    # Get the shape of graph
    n = 0
    for edge in graph:
        i, j, w = edge
        n = max(n, i+1, j+1)

    # Initialize all distances to infinite value
    dist = [[float('inf')] * n for _ in range(n)]

    # Assign weights to edges
    for i, j, w in graph:
        dist[i][j] = w

    # Find the shortest path
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

    # Find the length of shortest cycle
    shortest_length = float('inf')
    for i in range(n):
        shortest_length = min(shortest_length, dist[i][i])

    return shortest_length if shortest_length != float('inf') else None

if __name__ == "__main__":
    # graph = {(0, 1, 5),
    #          (0, 2, 3),
    #          (1, 3, 6),
    #          (1, 4, 2),
    #          (2, 4, 4),
    #          (3, 5, 1),
    #          (4, 3, 7),
    #          (4, 5, 2),
    #          (5, 0, 1)} # 0->1->4->5->0

    graph = {
        (0, 1, 1),
        (1, 2, 1),
        (2, 3, 1),
        (3, 1, 1),  # 1 → 2 → 3 → 1
        (2, 4, 1)
    }

    # graph = {
    #     (0,1,2),
    #     (0,2,4),
    #     (1,2,1),
    #     (1,3,7),
    #     (2,3,3),
    #     (3,4,5),
    #     (4,1,6) # 1->2->3->4->1
    # }

    # graph = {
    #     (0, 1, 1),
    #     (0, 2, 1),
    #     (1, 2, 1),
    #     (1, 3, 1),
    #     (2, 3, 1),
    #     #(2, 0, 1),
    #     (3, 4, 1),
    #     (4, 0, 1)
    # }

    # graph = {
    #
    #     (2, 3, 1),
    #     (3, 4, 1),
    #     (4, 5, 1),
    #     (4, 6, 1),
    #     (5, 6, 1),
    #     (6, 7, 1),
    #     (7, 8, 1),
    #     (8, 2, 1),
    #
    # }

    # graph = {
    #     (0, 2, 1),
    #     (1, 0, 1),
    #     (2, 4, 1),
    #     (3, 1, 1),
    #     (3, 2, 1),
    #     (4, 5, 1),
    #     (4, 6, 1),
    #     (5, 3, 1),
    #     (6, 5, 1),
    # }

    print(shortest_cycle(graph))