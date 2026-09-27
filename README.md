# QUBO Optimization Toolkit

A from-scratch implementation and study project for understanding **Quadratic Unconstrained Binary Optimization (QUBO)** through classical optimization problems.

The project is being developed incrementally, starting from binary optimization and Max-Cut, with the eventual goal of building a reusable QUBO optimization toolkit and using it as a foundation for studying **QAOA (Quantum Approximate Optimization Algorithm)**.

## Project Goals

This project focuses on understanding the concepts behind QUBO rather than relying entirely on high-level quantum computing libraries.

The main goals are:

* Understand binary optimization problems
* Implement brute-force optimization
* Formulate graph problems as QUBO
* Understand QUBO objective functions
* Represent QUBO problems using matrices
* Validate mathematical formulations using Python
* Compare different optimization approaches
* Build a foundation for implementing QAOA

## Current Progress

### Completed

* Binary state generation
* Binary objective function evaluation
* Brute-force search for optimal solutions
* Basic Max-Cut formulation
* Max-Cut edge contribution using binary variables
* Derivation of the XOR-based Max-Cut expression

For an edge \((i,j)\), the cut contribution is represented as:

$$
x_i + x_j - 2x_ix_j
$$

The current implementation evaluates all possible binary states and calculates the corresponding Max-Cut value.

### In Progress

* QUBO matrix formulation
* Generic QUBO evaluator
* QUBO brute-force solver
* Multiple graph examples
* Visualization of optimization results

### Planned

* Number Partitioning as a QUBO problem
* Knapsack formulation
* Generic QUBO problem representation
* QUBO benchmarking
* QUBO → Ising conversion
* QAOA implementation from scratch
* Qiskit-based validation
* Noise experiments

## Current Example: Max-Cut

The current implementation uses a triangle graph:

```text
    0
   / \
  /   \
 1-----2
```

Edges:

```text
(0, 1)
(0, 2)
(1, 2)
```

Each vertex is assigned a binary variable:

$$
x_i \in \{0,1\}
$$

where:

```text
0 → Group A
1 → Group B
```

For each edge, the contribution to the cut is:

$$
x_i + x_j - 2x_ix_j
$$

The total cut value is:

$$
C(x)=
\sum_{(i,j)\in E}
(x_i+x_j-2x_ix_j)
$$

The implementation currently enumerates all possible binary assignments and calculates the cut value for each assignment.

## Technology

* Python
* NumPy
* Matplotlib

Quantum computing frameworks will be introduced later for validation and comparison rather than being used as a replacement for understanding the underlying implementation.

## Project Structure

```text
qubo-optimization-toolkit/
│
├── README.md
├── requirements.txt
│
├── src/
│   ├── binary_search.py
│   └── max_cut.py
│
├── experiments/
│
├── results/
│
└── tests/
```

The structure will evolve as additional QUBO problems and optimization methods are implemented.

## Learning Approach

The project follows a bottom-up approach:

```text
Mathematical formulation
        ↓
Manual calculation
        ↓
Python implementation
        ↓
Testing
        ↓
QUBO formulation
        ↓
Matrix representation
        ↓
Optimization
        ↓
Quantum implementation
```

The core algorithms are intentionally implemented manually before introducing high-level quantum optimization libraries.

## Future Direction

The long-term goal is to connect classical QUBO optimization with quantum optimization:

```text
Optimization Problem
        ↓
QUBO Formulation
        ↓
QUBO Matrix
        ↓
Classical Brute Force
        ↓
Ising Formulation
        ↓
QAOA
        ↓
Quantum Simulation
        ↓
Performance Analysis
```

This project will serve as a foundation for further work in quantum optimization and quantum machine learning.

## Status

**Work in Progress**

The repository is being developed incrementally as part of a hands-on study of quantum optimization.
