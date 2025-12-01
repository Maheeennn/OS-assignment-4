import subprocess
import time
import csv
import os

# -----------------------------
# Settings
# -----------------------------
SIZES = [(5, 4), (10, 10), (500, 500), (2000, 2000)]
BINS = {
    "seq": "./bin/seq",
    "openmp": "./bin/omp",
    "pthreads": "./bin/thread2",
    "mpi": "mpirun -np 2 ./bin/mpi"
}
DATA_DIR = "./data"
RESULTS_DIR = "./results"
RESULTS_FILE = os.path.join(RESULTS_DIR, "results.csv")
SRC_DIR = "./src"
NUM_RUNS = 3

# Create directories if they don't exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)

# -----------------------------
# Create CSV with header
# -----------------------------
with open(RESULTS_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["matrix_size", "program", "run", "real_sec"])

# -----------------------------
# Benchmarking loop
# -----------------------------
for rows, cols in SIZES:
    size_str = f"{rows}x{cols}"

    # Generate matrices
    matrix_a = os.path.join(DATA_DIR, f"matrixA_{size_str}.txt")
    matrix_b = os.path.join(DATA_DIR, f"matrixB_{size_str}.txt")

    subprocess.run(["python3", f"{SRC_DIR}/random_matrix_generator.py", str(rows), str(cols)],
                   stdout=open(matrix_a, "w"))
    subprocess.run(["python3", f"{SRC_DIR}/random_matrix_generator.py", str(cols), str(cols)],
                   stdout=open(matrix_b, "w"))

    print(f"Generated {matrix_a} and {matrix_b}")

    # Run all implementations NUM_RUNS times
    for run in range(1, NUM_RUNS + 1):
        for program, exe in BINS.items():
            print(f"Running {program}, iteration {run} for size {size_str}...")
            start = time.time()
            cmd = exe.split() + [matrix_a, matrix_b] if "mpi" in program else [exe, matrix_a, matrix_b]
            subprocess.run(cmd)
            end = time.time()
            elapsed = end - start

            # Save result in CSV
            with open(RESULTS_FILE, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([size_str, program, run, elapsed])

    print(f"=== Finished benchmark for size {size_str} ===")

print(f"All benchmarks completed. Results saved to {RESULTS_FILE}")
