import numpy as np


def zigzag_traverse(matrix):
    zigzag = []
    for m in matrix:
        temp = np.array(m)
        zigzag_vector = np.concatenate(
            [
                np.diagonal(temp[::-1, :], i)[:: (2 * (i % 2) - 1)]
                for i in range(1 - temp.shape[0], temp.shape[0])
            ]
        )
        zigzag.append(list(zigzag_vector))
    return zigzag
