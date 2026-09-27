import itertools

edges = [(0, 1), (0, 2), (1, 2)]

for state in itertools.product([0, 1], repeat=3):

    cut_value = 0

    for i, j in edges:
        xi = state[i]
        xj = state[j]
        edge_value = xi + xj - 2 * xi * xj

        cut_value += edge_value

    print(state, cut_value)