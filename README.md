# QUBO Optimization From Scratch

A hands-on learning repository for building **Quadratic Unconstrained Binary Optimization (QUBO)** intuition from first principles using Python.

The current focus is on binary optimization and a complete Max-Cut-to-QUBO walkthrough on a triangle graph.

## What this project covers

- Binary state generation with exhaustive search
- Objective evaluation for binary optimization
- Max-Cut formulation with binary variables
- QUBO matrix construction for Max-Cut
- Numerical validation of \(x^TQx = -C(x)\)

## Repository structure

```text
qubo-optimization-from-scratch/
├── README.md
├── requirements.txt
└── src/
    ├── binary_search.py
    ├── max_cut.py
    └── qubo_matrix.py
```

## Quick start

1. Create and activate a virtual environment (optional but recommended).
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the QUBO validation example:

```bash
python src/qubo_matrix.py
```

## Current worked example: Triangle Max-Cut

Graph:

```text
    0
   / \
  /   \
 1-----2
```

Edges:

```python
edges = [(0, 1), (0, 2), (1, 2)]
```

For binary variables \(x_i \in \{0,1\}\), each edge contributes:

\[
x_i + x_j - 2x_ix_j
\]

So the Max-Cut objective is:

\[
C(x)=2x_0+2x_1+2x_2-2x_0x_1-2x_0x_2-2x_1x_2
\]

QUBO is written as minimization, so we use \(-C(x)\) and map it to:

\[
f(x)=x^TQx,\quad
Q=
\begin{bmatrix}
-2 & 1 & 1\\
1 & -2 & 1\\
1 & 1 & -2
\end{bmatrix}
\]

The validation script checks every 3-bit state and confirms:

```text
QUBO value == -Max-Cut value
```

## Learning roadmap

- [x] Binary optimization basics
- [x] Max-Cut formulation
- [x] QUBO matrix representation
- [ ] Generic QUBO brute-force solver
- [ ] Additional QUBO problems (e.g., Number Partitioning, Knapsack)
- [ ] QUBO-to-Ising conversion
- [ ] QAOA experimentation

## Status

**Phase 2 complete:** Max-Cut QUBO matrix construction and exhaustive state validation.