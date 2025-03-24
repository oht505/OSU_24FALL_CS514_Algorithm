from hw8 import Max_Flow_Fat, Max_Flow_Short

assert Max_Flow_Fat(0, 5, [(0, 1, 16), (0, 2, 13), (1, 3, 12), (2, 1, 4), (2, 4, 14), (3, 2, 9), (3, 5, 20), (4, 3, 7), (4, 5, 4)]) == (23, [(0, 1, 12), (0, 2, 11), (1, 3, 12), (2, 4, 11), (3, 5, 19), (4, 3, 7), (4, 5, 4)])

assert Max_Flow_Short(0, 5, [(0, 1, 16), (0, 2, 13), (1, 3, 12), (2, 1, 4), (2, 4, 14), (3, 2, 9), (3, 5, 20), (4, 3, 7), (4, 5, 4)]) == (23, [(0, 1, 12), (0, 2, 11), (1, 3, 12), (2, 4, 11), (3, 5, 19), (4, 3, 7), (4, 5, 4)])

# Generated:

assert Max_Flow_Fat(1, 4, [(1, 2, 3), (1, 3, 2), (2, 3, 1), (2, 4, 2), (3, 4, 3)]) == (5, [(1, 2, 3), (1, 3, 2), (2, 3, 1), (2, 4, 2), (3, 4, 3)])

assert Max_Flow_Fat(1, 5, [(1, 2, 2), (1, 3, 3), (2, 3, 1), (2, 4, 2), (3, 4, 2), (3, 5, 3), (4, 5, 2)]) == (5, [(1, 2, 2), (1, 3, 3), (2, 4, 2), (3, 5, 3), (4, 5, 2)])

assert Max_Flow_Fat(1, 3, [(1, 2, 2), (1, 3, 1), (2, 3, 1)]) == (2, [(1, 2, 1), (1, 3, 1), (2, 3, 1)])

assert Max_Flow_Fat(1, 5, [(1, 2, 2), (1, 3, 2), (2, 3, 3), (2, 4, 2), (3, 4, 1), (3, 5, 2), (4, 5, 3)]) == (4, [(1, 2, 2), (1, 3, 2), (2, 4, 2), (3, 5, 2), (4, 5, 2)])

assert Max_Flow_Fat(1, 5, [(1, 2, 2), (1, 3, 3), (2, 3, 3), (2, 4, 2), (3, 4, 1), (3, 5, 2), (4, 5, 3)]) == (5, [(1, 2, 2), (1, 3, 3), (2, 4, 2), (3, 4, 1), (3, 5, 2), (4, 5, 3)])

assert Max_Flow_Short(1, 4, [(1, 2, 3), (1, 3, 2), (2, 3, 1), (2, 4, 2), (3, 4, 3)]) == (5, [(1, 2, 3), (1, 3, 2), (2, 3, 1), (2, 4, 2), (3, 4, 3)])

assert Max_Flow_Short(1, 5, [(1, 2, 2), (1, 3, 3), (2, 3, 1), (2, 4, 2), (3, 4, 2), (3, 5, 3), (4, 5, 2)]) == (5, [(1, 2, 2), (1, 3, 3), (2, 4, 2), (3, 5, 3), (4, 5, 2)])

assert Max_Flow_Short(1, 3, [(1, 2, 2), (1, 3, 1), (2, 3, 1)]) == (2, [(1, 2, 1), (1, 3, 1), (2, 3, 1)])

assert Max_Flow_Short(1, 5, [(1, 2, 2), (1, 3, 2), (2, 3, 3), (2, 4, 2), (3, 4, 1), (3, 5, 2), (4, 5, 3)]) == (4, [(1, 2, 2), (1, 3, 2), (2, 4, 2), (3, 5, 2), (4, 5, 2)])

assert Max_Flow_Short(1, 5, [(1, 2, 2), (1, 3, 3), (2, 3, 3), (2, 4, 2), (3, 4, 1), (3, 5, 2), (4, 5, 3)]) == (5, [(1, 2, 2), (1, 3, 3), (2, 4, 2), (3, 4, 1), (3, 5, 2), (4, 5, 3)])