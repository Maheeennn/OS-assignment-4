#!/usr/bin/env python3
import sys

def shape(path):
    rows = 0
    cols = None
    with open(path, 'r') as f:
        for i, line in enumerate(f, start=1):
            s = line.strip()
            if not s:
                continue
            parts = s.replace('\t', ' ').split()
            if cols is None:
                cols = len(parts)
            elif len(parts) != cols:
                print(f"ERROR: inconsistent column count in {path} at line {i}", file=sys.stderr)
                sys.exit(2)
            rows += 1
    return rows, cols or 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: check_dims.py fileA [fileB ...]")
        sys.exit(1)
    for p in sys.argv[1:]:
        r, c = shape(p)
        print(f"{p}: {r} x {c}")
