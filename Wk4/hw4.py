############################################################
## Homework Assignment Week 4: Graph
## Name: Hyuntaek Oh
## Email: ohhyun@oregonstate.edu
## Course: CS 514_400 Algorithms
## Due: Oct. 28, 2024
#############################################################

direction = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

def find_blank_position(state):
    # Find the position of zero
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

    return None

def move_blank(state, dir):
    i, j = find_blank_position(state)
    di, dj = direction[dir]
    ni, nj = i + di, j + dj

    # Swap the values after moving if the move is within boundary
    if 0 <= ni < 3 and 0 <= nj < 3:
        new_state = [row[:] for row in state]
        new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
        return new_state

    return None

def bfs(state):
    q = [(state, 0)]
    visited = {tuple(map(tuple, state)): 0}

    while q:
        curr_state, path_length = q.pop(0)

        # Try all possible paths
        for dir in direction:
            new_state = move_blank(curr_state, dir)
            if new_state is not None:
                new_state_tuple = tuple(map(tuple, new_state))
                if new_state_tuple not in visited:
                    visited[new_state_tuple] = path_length + 1
                    q.append((new_state, path_length + 1))

    return visited

def ShortestPath(goal_state, init_state):

    ans = []

    # Reshape goal_state into 2-D array (3x3)
    goal_matrix = [goal_state[i:i+3] for i in range(0, len(goal_state), 3)]

    # By using bfs, search the possible paths
    visited = bfs(goal_matrix)

    # Find the length of paths for each init_state
    for init_i in init_state:
        init_matrix = [init_i[i:i+3] for i in range(0, len(init_i), 3)]
        init_tuple = tuple(map(tuple, init_matrix))

        # Append the shortest path, otherwise -1
        ans.append(visited.get(init_tuple, -1))

    return ans

