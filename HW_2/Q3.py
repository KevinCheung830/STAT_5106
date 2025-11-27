import numpy as np

# Create the matrices
A = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])

B = np.array([[4, 3, 2, 1],
              [3, 6, 4, 2],
              [2, 4, 6, 3],
              [1, 2, 3, 4]])

C = np.array([[4, 3, 2, 1],
              [5, 6, 7, 8],
              [8, 7, 6, 5],
              [4, 3, 2, 1]])


def part_3a():
    trace_ABC = np.trace(A @ B @ C)
    trace_CAB = np.trace(C @ A @ B)
    trace_BCA = np.trace(B @ C @ A)
    return np.allclose(trace_ABC, trace_CAB) and np.allclose(trace_ABC, trace_BCA)
print("Part 3a:", part_3a())

def part_3b():
    LHS = A.T @ B.T @ C.T
    RHS = (C @ B @ A).T
    return np.allclose(LHS, RHS)
print("Part 3b:", part_3b())

def part_3c():
    I_4 = np.eye(4)
    D = I_4 + A
    LHS =  np.linalg.inv(D @ B)
    RHS = np.linalg.inv(B) @ np.linalg.inv(D)
    return np.allclose(LHS, RHS)
print("Part 3c:", part_3c())