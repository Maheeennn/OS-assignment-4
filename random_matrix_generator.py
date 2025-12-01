#!/usr/bin/env python3
import sys
import random

if len(sys.argv) != 3:
    print("Usage: python3 random_matrix_generator.py ROWS COLS")
    sys.exit(1)

rows = int(sys.argv[1])
cols = int(sys.argv[2])

for _ in range(rows):
    print(' '.join(f"{random.uniform(0,10):.2f}" for _ in range(cols)))

