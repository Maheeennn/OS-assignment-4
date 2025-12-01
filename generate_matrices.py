import os
import numpy as np

# Folder for matrices
os.makedirs("data", exist_ok=True)

# Define matrix sizes as (rows_A, cols_A, rows_B, cols_B)
matrix_pairs = [
    (5, 4, 4, 5),
    (10, 10, 10, 10),
    (500, 500, 500, 500),
    (2000, 2000, 2000, 2000)
]

for rA, cA, rB, cB in matrix_pairs:
    A = np.random.randint(0, 10, size=(rA, cA))
    B = np.random.randint(0, 10, size=(rB, cB))

    # Save matrix A
    with open(f"data/matrixA_{rA}x{cA}.txt", "w") as f:
        f.write(f"{rA} {cA}\n")
        for row in A:
            f.write(" ".join(map(str, row)) + "\n")

    # Save matrix B
    with open(f"data/matrixB_{rB}x{cB}.txt", "w") as f:
        f.write(f"{rB} {cB}\n")
        for row in B:
            f.write(" ".join(map(str, row)) + "\n")

print("All matrices generated with correct format.")
