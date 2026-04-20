import time
import numpy as np

def run_test(size=2000):
    print(f"Matrix size: {size} x {size}")
    matrix = np.random.rand(size, size)

    # Row-wise traversal
    start = time.time()
    row_sum = 0
    for i in range(size):
        for j in range(size):
            row_sum += matrix[i][j]
    row_time = time.time() - start
    print(f"Row-wise traversal time: {row_time:.4f} seconds")

    # Column-wise traversal
    start = time.time()
    col_sum = 0
    for j in range(size):
        for i in range(size):
            col_sum += matrix[i][j]
    col_time = time.time() - start
    print(f"Column-wise traversal time: {col_time:.4f} seconds")

    print("\nPerformance Difference:")
    print(f"Column-wise is {col_time / row_time:.2f}x slower than row-wise")

if __name__ == "__main__":
    run_test()