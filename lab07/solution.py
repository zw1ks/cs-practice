import numpy as np

def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if width <= 0 or len(values) % width != 0:
        return []
    arr = np.asarray(values, dtype = float)
    reshaped = arr.reshape(-1, width)
    return reshaped.tolist()


def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    if not matrix or not rows or not columns:
        return []
    arr = np.asarray(matrix, dtype=float)
    sub_matrix = arr[np.ix_(rows, columns)]
    return sub_matrix.tolist()


def column_means(matrix):
    if not matrix or not matrix[0]:
        return []
    arr = np.asarray(matrix, dtype=float)
    means = np.mean(arr, axis=0)
    rounded_means = np.round(means, 6)
    return rounded_means.tolist()


def column_range(matrix: list[list[float]], column: int) -> float:
    if not matrix or not matrix[0]:
        return 0.0
    arr = np.asarray(matrix, dtype=float)
    col_data = arr[:, column]
    rng = np.max(col_data) - np.min(col_data)
    return float(np.round(rng, 6))
