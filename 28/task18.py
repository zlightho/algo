from typing import List

def MatrixTurn(Matrix: List[str], M: int, N: int, T: int) -> None:
    """
    Rotates a given matrix clockwise by T steps.

    The function takes a matrix represented as a list of strings,
    its dimensions M and N, and the number of steps T. The matrix is
    rotated in-place, so the original matrix is modified.

    Args:
        Matrix (List[str]): A list of strings representing the matrix.
            The matrix has M rows and N columns.
        M (int): The number of rows in the matrix.
        N (int): The number of columns in the matrix.
        T (int): The number of steps to rotate the matrix clockwise.

    Returns:
        None
    """
    matrix = [list(row) for row in Matrix]
    layers = min(M, N) // 2    
    for layer in range(layers):
        row_len = M - 2 * layer - 1
        col_len = N - 2 * layer - 1
        layer_elements = 2 * (row_len + col_len)
        steps = T % layer_elements
        for _ in range(steps):
            temp = matrix[layer][layer]
            # Rotate left column
            for row in range(layer, M - layer - 1):
                matrix[row][layer] = matrix[row + 1][layer]
            # Rotate bottom row
            for col in range(layer, N - layer - 1):
                matrix[M - layer - 1][col] = matrix[M - layer - 1][col + 1]
            # Rotate right column
            for row in range(M - layer - 1, layer, -1):
                matrix[row][N - layer - 1] = matrix[row - 1][N - layer - 1]
            # Rotate top row
            for col in range(N - layer - 1, layer + 1, -1):
                matrix[layer][col] = matrix[layer][col - 1]
            matrix[layer][layer + 1] = temp
    # Update the original Matrix
    for i in range(M):
        Matrix[i] = "".join(matrix[i])
