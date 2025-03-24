from hw4 import ShortestPath


initial_states = [[1, 2, 3, 4, 5, 6, 8, 7, 0]]
goal_state = [1, 2, 3, 4, 5, 6, 8, 7, 0]
shortest_paths = ShortestPath(goal_state, initial_states)
if shortest_paths != [0]:
    raise Exception("Failed test")
else:
    print("Passed")

initial_states = [[1, 2, 3, 8, 0, 4, 7, 6, 5]]
goal_state = [1, 3, 4, 8, 6, 2, 7, 0, 5]
shortest_paths = ShortestPath(goal_state, initial_states)
if shortest_paths != [5]:
    raise Exception("Failed test")
else:
    print("Passed")

initial_states = [[1, 2, 3, 8, 0, 4, 7, 6, 5]]
goal_state = [2, 8, 1, 0, 4, 3, 7, 6, 5]
shortest_paths = ShortestPath(goal_state, initial_states)
if shortest_paths != [9]:
    raise Exception("Failed test")
else:
    print("Passed")

initial_states = [[1, 2, 3, 8, 0, 4, 7, 6, 5]]
goal_state = [2, 8, 1, 4, 6, 3, 0, 7, 5]
shortest_paths = ShortestPath(goal_state, initial_states)
if shortest_paths != [12]:
    raise Exception("Failed test")
else:
    print("Passed")

initial_states = [[1, 3, 4, 8, 0, 5, 7, 2, 6],
                  [2, 3, 1, 7, 0, 8, 6, 5, 4],
                  [2, 3, 1, 8, 0, 4, 7, 6, 5]]
goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
shortest_paths = ShortestPath(goal_state, initial_states)
if shortest_paths != [6, 14, 16]:
    raise Exception("Failed test")
else:
    print("Passed")

initial_states = [[1, 2, 3, 8, 0, 4, 7, 6, 5]]
goal_state = [2, 3, 1, 8, 0, 4, 7, 6, 5]
shortest_paths = ShortestPath(goal_state, initial_states)
if shortest_paths != [16]:
    raise Exception("Failed test")
else:
    print("Passed")

initial_states = [[2, 8, 3, 1, 0, 4, 7, 6, 5],
                  [8, 7, 6, 1, 0, 5, 2, 3, 4]]
goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
shortest_paths = ShortestPath(goal_state, initial_states)
if shortest_paths != [4, 28]:
    raise Exception("Failed test")
else:
    print("Passed")

initial_states = [[8, 6, 7, 2, 5, 4, 3, 0, 1],
                  [6, 4, 7, 8, 5, 0, 3, 2, 1]]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
shortest_paths = ShortestPath(goal_state, initial_states)
if shortest_paths != [31, 31]:
    raise Exception("Failed test")
else:
    print("Passed")

initial_states = [[1, 2, 3, 8, 0, 4, 7, 6, 5]]
goal_state = [5, 6, 7, 4, 0, 8, 3, 2, 1]
shortest_paths = ShortestPath(goal_state, initial_states)
if shortest_paths != [30]:
    raise Exception("Failed test")
else:
    print("Passed")


initial_states = [[8, 0, 6, 5, 4, 7, 2, 3, 1],
                  [6, 4, 1, 3, 0, 2, 7, 5, 8],
                  [1, 5, 8, 3, 2, 7, 0, 6, 4],
                  [3, 2, 8, 4, 5, 1, 6, 7, 0],
                  [0, 3, 5, 4, 2, 8, 6, 1, 7],
                  [7, 2, 5, 3, 1, 0, 6, 4, 8]]
goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
shortest_paths = ShortestPath(goal_state, initial_states)
if shortest_paths != [31, 14, 12, 12, 10, 15]:
    raise Exception("Failed test")
else:
    print("Passed")

initial_states = [[4, 1, 2, 0, 8, 7, 6, 3, 5],
                  [1, 6, 2, 5, 7, 3, 0, 4, 8]]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
shortest_paths = ShortestPath(goal_state, initial_states)
if shortest_paths != [17, 10]:
    raise Exception("Failed test")
else:
    print("Passed")