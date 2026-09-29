# QUBO Optimization Toolkit

A from-scratch learning project for understanding **Quadratic Unconstrained Binary Optimization (QUBO)** through classical optimization problems.

The project is developed incrementally, starting with binary optimization and Max-Cut.

## Project Goals

- Understand binary optimization problems
- Generate and evaluate binary states
- Implement brute-force optimization
- Formulate graph problems as QUBO
- Represent QUBOs using matrices
- Validate mathematical formulations with Python
- Build a foundation for studying QAOA later

## Current Progress

### Completed

- Binary state generation
- Binary objective-function evaluation
- Brute-force optimization
- Basic Max-Cut formulation
- XOR-based Max-Cut expression
- Max-Cut mathematical formulation
- Symmetric QUBO matrix representation
- Generic NumPy QUBO evaluator
- Exhaustive validation of all 3-bit states

### Next Steps

- Generic QUBO brute-force solver
- Additional QUBO problems
- Number Partitioning
- Knapsack
- QUBO-to-Ising conversion

## Current Example: Triangle Max-Cut

The graph is:

```text
    0
   / \
  /   \
 1-----2
```

Its edges are:

```python
edges = [(0, 1), (0, 2), (1, 2)]
```

Each vertex has a binary variable:

$$
x_i \in \{0,1\}
$$

For an edge \((i,j)\), the cut contribution is:

$$
x_i+x_j-2x_ix_j
$$

Therefore, the total Max-Cut objective is:

$$
C(x)=
2x_0+2x_1+2x_2
-2x_0x_1-2x_0x_2-2x_1x_2
$$

## QUBO Matrix Representation

QUBO is written as a minimization problem, so we use the negative Max-Cut objective:

$$
-C(x)=
-2x_0-2x_1-2x_2
+2x_0x_1+2x_0x_2+2x_1x_2
$$

This expression is represented by the symmetric matrix:

$$
Q=
\begin{bmatrix}
-2 & 1 & 1\\
1 & -2 & 1\\
1 & 1 & -2
\end{bmatrix}
$$

The QUBO objective is:

$$
f(x)=x^TQx
$$

The diagonal entries produce the linear terms because:

$$
x_i^2=x_i
$$

for binary variables.

The off-diagonal entries are `1` because symmetric matrix multiplication includes each cross term twice:

$$
Q_{01}x_0x_1+Q_{10}x_1x_0
=
x_0x_1+x_1x_0
=
2x_0x_1
$$

Thus:

$$
x^TQx=-C(x)
$$

## Phase 2 Implementation

The implementation is located in:

```text
src/qubo_matrix.py
```

The QUBO evaluator calculates:

```python
x.T @ Q @ x
```

which directly corresponds to:

$$
x^TQx
$$

The program also calculates the original Max-Cut objective and verifies that:

```text
QUBO value == -Max-Cut value
```

## Validation

Run the validation script from the project root:

```powershell
python src\qubo_matrix.py
```

All eight possible 3-bit states are tested:

```text
000
001
010
011
100
101
110
111
```

Expected output:

```text
000 Max-Cut = 0 QUBO = 0
001 Max-Cut = 2 QUBO = -2
010 Max-Cut = 2 QUBO = -2
011 Max-Cut = 2 QUBO = -2
100 Max-Cut = 2 QUBO = -2
101 Max-Cut = 2 QUBO = -2
110 Max-Cut = 2 QUBO = -2
111 Max-Cut = 0 QUBO = 0
All states validated.
```

## Project Structure

```text
qubo-optimization-from-scratch/
│
├── readme.md
├── requirements.txt
│
├── src/
│   ├── binary_search.py
│   ├── max_cut.py
│   └── qubo_matrix.py
│
├── experiments/
├── results/
└── tests/
```

## Technology

- Python
- NumPy
- Matplotlib

High-level quantum optimization libraries are intentionally not used during the foundational implementation stages.

## Learning Progression

```text
Binary Optimization
        ↓
Brute-Force Solver
        ↓
Max-Cut
        ↓
Mathematical Formulation
        ↓
QUBO Matrix
        ↓
Generic QUBO Evaluator
        ↓
Generic QUBO Solver
        ↓
Multiple QUBO Problems
        ↓
Ising Formulation
        ↓
QAOA
```

## Status

**Phase 2 complete:** QUBO matrix representation and validation.