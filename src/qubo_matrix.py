import itertools

import numpy as np


EDGES = [(0, 1), (0, 2), (1, 2)]

Q = np.array([
    [-2, 1, 1],
    [1, -2, 1],
    [1, 1, -2],
], dtype=int)


def qubo_value(Q, x):
    """Calculate the QUBO objective x.T @ Q @ x."""
    Q = np.asarray(Q)
    x = np.asarray(x)

    return x.T @ Q @ x


def max_cut_value(edges, x):
    """Calculate the original Max-Cut objective."""
    return sum(
        x[i] + x[j] - 2 * x[i] * x[j]
        for i, j in edges
    )


def validate_all_states():
    """Validate the QUBO matrix against Max-Cut for every 3-bit state."""
    for state in itertools.product([0, 1], repeat=3):
        x = np.array(state)

        cut_value = max_cut_value(EDGES, x)
        q_value = qubo_value(Q, x)

        assert q_value == -cut_value

        print(
            "".join(map(str, state)),
            f"Max-Cut = {cut_value}",
            f"QUBO = {q_value}",
        )


if __name__ == "__main__":
    validate_all_states()
    print("All states validated.")