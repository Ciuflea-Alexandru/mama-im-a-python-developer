def add_matrices(A, B):
    """Adds two matrices of the same dimensions."""
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")
    
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiply_matrices(A, B):
    """Multiplies two matrices: A (m x n) and B (n x p)."""
    if len(A[0]) != len(B):
        raise ValueError("Columns of A must equal rows of B for multiplication.")
    
    # Initialize result matrix with zeros
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Example Usage
if __name__ == "__main__":
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]
    
    print("Addition:", add_matrices(matrix_a, matrix_b))
    print("Multiplication:", multiply_matrices(matrix_a, matrix_b))